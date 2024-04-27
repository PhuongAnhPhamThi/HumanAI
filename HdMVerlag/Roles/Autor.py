import json
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.textErstellen import textErstellen
from Actions.konzeptErstellen import konzeptErstellen
from Actions.rezensionErstellen import rezensionErstellen
from Actions.textEditieren import textEditieren
from Actions.textUeberpruefenZiklus import textUeberpruefenZiklus
from Actions.textEditierenZiklus import textEditierenZiklus
from Roles.Editor import track_editor, max_round
from Roles.Editor import file_path


class Autor(Role):
    name: str = "Maja"
    profile: str = "Autor"
    language: str = "German"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([textErstellen, textEditieren, textEditierenZiklus])
        self._watch([UserRequirement, konzeptErstellen, rezensionErstellen, textUeberpruefenZiklus, textErstellen,
                     textEditieren])

    async def _think(self) -> bool:

        last_memory = self.get_memories(k=1)

        if last_memory[0].role == "Editor" and self.rc.memory.get_by_action(konzeptErstellen)[0].content != "" and \
                len(self.rc.memory.get_by_action(rezensionErstellen)) == 0:
            self.set_actions([textErstellen])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Editor" and self.rc.memory.get_by_action(rezensionErstellen)[0].content != "" \
                and len(self.rc.memory.get_by_action(textUeberpruefenZiklus)) == 0:
            self.set_actions([textEditieren])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Editor" and self.rc.memory.get_by_action(textUeberpruefenZiklus)[0].content != "" \
                and track_editor < max_round-1 and "sieht gut aus" not in last_memory[
            0].content and "Sieht gut aus" not in last_memory[0].content:
            self.set_actions([textEditierenZiklus])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        genre = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["genre"]
        gattung = json.loads(self.rc.memory.get_by_action(UserRequirement)[0].content)["gattung"]
        if isinstance(todo, textErstellen):
            context = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context=context, genre=genre, gattung=gattung)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, textEditieren):
            context2 = self.rc.memory.get_by_action(rezensionErstellen)[0].content
            context1 = self.rc.memory.get_by_action(textErstellen)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        elif isinstance(todo, textEditierenZiklus):
            context1 = self.rc.memory.get_by_action(textUeberpruefenZiklus)[0].content
            context2 = self.rc.memory.get_by_action(textEditieren)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

        else:
            self._set_state(-1)
            rslt = ""
            msg = None
            pass

        with open(file_path, 'a') as file:
            file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
            file.write(
                rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")

        return msg
