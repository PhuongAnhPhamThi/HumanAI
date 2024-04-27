import json
from metagpt.actions import UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.textErstellen import textErstellen
from Actions.recherchieren import Recherchieren
from Actions.konzeptErstellen import konzeptErstellen
from Actions.textUeberpruefen import textUeberpruefen
from Actions.rezensionErstellen import rezensionErstellen
from Actions.textUeberpruefenZiklus import textUeberpruefenZiklus
from Actions.textEditieren import textEditieren
from Actions.textEditierenZiklus import textEditierenZiklus
from Actions.coverKonzipieren import coverKonzipieren
from Actions.illustrieren import illustrieren
from Actions.buchZusammenfassen import buchZusammenfassen
from Actions.layoutKonzipieren import layoutKonzipieren

# file_path to save the conversation
file_path: str = "C:/Users/admin/Desktop/conversation.txt"

# track loop of editor at tetxüberprüfenzyklus. max = 2

track_editor: int = 0
max_round = 2
print("track_editor")
print(track_editor)


class Editor(Role):
    name: str = "Bob"
    profile: str = "Editor"
    language: str = "German"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch(
            [UserRequirement, Recherchieren, konzeptErstellen, textErstellen, textUeberpruefen, rezensionErstellen,
             textEditieren, textEditierenZiklus, textUeberpruefenZiklus,illustrieren,coverKonzipieren,buchZusammenfassen,layoutKonzipieren])

    async def _think(self) -> bool:
        global track_editor
        last_memory = self.get_memories(k=1)

        # check if memory is only request from human & content is not leer => do the research & create concept
        # request for autor.
        if last_memory[0].role == "Human" and len(
                self.get_memories()) < 2 and last_memory[0].content != "":
            await self._actRecherchieren()
            self.set_actions([konzeptErstellen])
            self._set_state(0)
            return True

        # check if last message is from autor and there is no rezension => textUeberpruefen, rezensionErstellen
        elif last_memory[0].role == "Autor" and self.rc.memory.get_by_action(textErstellen)[0].content != "" and \
                len(self.rc.memory.get_by_action(rezensionErstellen)) == 0:
            await self._actTextUeberpruefen()
            self.set_actions([rezensionErstellen])
            self._set_state(0)
            return True

        # check if last message is from autor and there is a recension, a edited text => textUeberpruefenZiklus
        elif last_memory[0].role == "Autor" and self.rc.memory.get_by_action(textEditieren)[0].content != "" and \
                self.rc.memory.get_by_action(rezensionErstellen)[0].content != "" and track_editor <= max_round:
            self.set_actions([textUeberpruefenZiklus])
            self._set_state(0)
            track_editor += 1
            return True

        elif track_editor > max_round and len(self.rc.memory.get_by_action(coverKonzipieren)) == 0:
            self.set_actions([coverKonzipieren])
            self._set_state(0)
            return True

        elif self.rc.memory.get_by_action(coverKonzipieren)[0].content != "" \
                and len(self.rc.memory.get_by_action(illustrieren)) != 0:
            await self._actBuchZusammenfassen()
            self.set_actions([layoutKonzipieren])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        self.set_actions([Recherchieren, konzeptErstellen])
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        logger.info(todo)
        if isinstance(todo, konzeptErstellen):
            context = self.rc.memory.get_by_action(Recherchieren)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, rezensionErstellen):
            context2 = self.rc.memory.get_by_action(textErstellen)[0].content
            context1 = self.rc.memory.get_by_action(textUeberpruefen)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, textUeberpruefenZiklus):
            context2 = self.rc.memory.get_by_action(rezensionErstellen)[0].content
            context1 = self.get_memories(k=1)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, coverKonzipieren):
            context = self.rc.memory.get_by_action(textEditierenZiklus)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, layoutKonzipieren):
            context1 = self.rc.memory.get_by_action(buchZusammenfassen)[0].content
            context2 = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            context3 = self.rc.memory.get_by_action(coverKonzipieren)[0].content
            rslt = await todo.run(context1=context1,context2=context2,context3=context3)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        else:
            self._set_state(-1)
            rslt = ""
            msg = None
            pass

        global file_path
        with open(file_path, 'a') as file:
            file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
            file.write(
                rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
        return msg

    async def _actRecherchieren(self) -> Message:
        # genre = self.rc.memory.get_by_action(UserRequirement)[0].content
        json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["genre"]
        gattung = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["gattung"]
        self.set_actions([Recherchieren])
        todo = self.set_todo(Recherchieren())
        todo = self.rc.todo
        logger.info(todo)
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, Recherchieren):
            rslt = await todo.run(genre=genre, gattung=gattung)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            global file_path
            with open("C:/Users/admin/Desktop/conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(
                    rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
            return msg
        else:
            self._set_state(-1)
            pass

    async def _actTextUeberpruefen(self) -> Message:
        # genre = self.rc.memory.get_by_action(UserRequirement)[0].content
        genre = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["genre"]
        gattung = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["gattung"]
        self.set_actions([textUeberpruefen])
        todo = self.set_todo(textUeberpruefen())
        todo = self.rc.todo
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, textUeberpruefen):
            context1 = self.rc.memory.get_by_action(textErstellen)[0].content
            context2 = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context1=context1, context2=context2, genre=genre, gattung=gattung)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            global file_path
            with open("C:/Users/admin/Desktop/conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(
                    rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
            return msg

        else:
            self._set_state(-1)
            pass

    async def _actBuchZusammenfassen(self) -> Message:
        self.set_actions([buchZusammenfassen])
        todo = self.set_todo(buchZusammenfassen())
        todo = self.rc.todo
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, buchZusammenfassen):
            context1 = self.rc.memory.get_by_action(textEditierenZiklus)[0].content
            context2 = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            global file_path
            with open("C:/Users/admin/Desktop/conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(
                    rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
            return msg

        else:
            self._set_state(-1)
            pass

