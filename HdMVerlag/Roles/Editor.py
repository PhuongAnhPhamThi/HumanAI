import fire
import asyncio
from metagpt.actions import Action, UserRequirement
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

track_editor: int = 0
print(track_editor)
file_path: str = "C:/Users/admin/Desktop/conversation.txt"


class Editor(Role):
    name: str = "Bob"
    profile: str = "Editor"
    language: str = "German"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch(
            [UserRequirement, Recherchieren, konzeptErstellen, textErstellen, textUeberpruefen, rezensionErstellen,
             textEditieren, textEditierenZiklus, textUeberpruefenZiklus])

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
                self.rc.memory.get_by_action(rezensionErstellen)[0].content != "" and track_editor < 3:
            self.set_actions([textUeberpruefenZiklus])
            self._set_state(0)
            track_editor += 1
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        self.set_actions([Recherchieren, konzeptErstellen])
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        logger.info(todo)
        thema = self.rc.memory.get_by_action(UserRequirement)[0].content
        if isinstance(todo, konzeptErstellen):
            context = self.rc.memory.get_by_action(Recherchieren)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            #return msg
        elif isinstance(todo, textUeberpruefen):
            context1 = self.rc.memory.get_by_action(textErstellen)[0].content
            context2 = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context1=context1, context2=context2, thema=thema)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            #return msg
        elif isinstance(todo, rezensionErstellen):
            context2 = self.rc.memory.get_by_action(textErstellen)[0].content
            context1 = self.rc.memory.get_by_action(textUeberpruefen)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            #return msg
        elif isinstance(todo, textUeberpruefenZiklus):
            context2 = self.rc.memory.get_by_action(rezensionErstellen)[0].content
            context1 = self.get_memories(k=1)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            # return msg
        else:
            self._set_state(-1)
            rslt=""
            msg = None
            pass

        global file_path
        with open(file_path, 'a') as file:
            file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
            file.write(rslt + " \n\n"+ "-------------------------------------------------------------------------------------------------" + "\n\n\n")
        return msg


    async def _actRecherchieren(self) -> Message:
        thema = self.rc.memory.get_by_action(UserRequirement)[0].content
        self.set_actions([Recherchieren])
        todo = self.set_todo(Recherchieren())
        todo = self.rc.todo
        logger.info(todo)
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, Recherchieren):
            rslt = await todo.run(thema=thema)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            global file_path
            with open("C:/Users/admin/Desktop/conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(rslt + " \n\n"+ "-------------------------------------------------------------------------------------------------" + "\n\n\n")
            return msg
        else:
            self._set_state(-1)
            pass



    async def _actTextUeberpruefen(self) -> Message:
        thema = self.rc.memory.get_by_action(UserRequirement)[0].content
        self.set_actions([textUeberpruefen])
        todo = self.set_todo(textUeberpruefen())
        todo = self.rc.todo
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, textUeberpruefen):
            context1 = self.rc.memory.get_by_action(textErstellen)[0].content
            context2 = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context1=context1, context2=context2, thema=thema)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            global file_path
            with open("C:/Users/admin/Desktop/conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
            return msg

        else:
            self._set_state(-1)
            pass


