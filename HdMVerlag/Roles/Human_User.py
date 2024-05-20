from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.illustrieren import illustrieren
from Actions.coverKonzipieren import coverKonzipieren
from Archive.titelEmpfehlen import titelEmpfehlen
from Archive.titelErstellen import titelErstellen
from Actions.konzeptErstellen import konzeptErstellen
from Actions.recherchieren import Recherchieren
from Actions.ideaEmpfehlen import ideaEmpfehlen
from workspace.Utils.json_handle import write_to_json_file
from workspace.Utils.text_handle import write_to_txt_file


class Human_User(Role):
    name: str = "Human_User"
    profile: str = "Human_User"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([titelEmpfehlen, illustrieren])
        self._watch([titelErstellen, coverKonzipieren, konzeptErstellen,ideaEmpfehlen,Recherchieren])

    async def _think(self) -> bool:

        last_memory = self.get_memories(k=1)

        if last_memory[0].role == "Editor" and len(self.rc.memory.get_by_action(Recherchieren)) > 0 and len(
                self.rc.memory.get_by_action(ideaEmpfehlen)) == 0:
            self.set_actions([ideaEmpfehlen])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Editor" and len(self.rc.memory.get_by_action(coverKonzipieren)) > 0 and len(
                self.rc.memory.get_by_action(illustrieren)) == 0:
            self.set_actions([illustrieren])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo

        if isinstance(todo, ideaEmpfehlen):
            rslt = await todo.run(ideas=self.rc.memory.get_by_action(Recherchieren)[0].content)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg


        elif isinstance(todo, illustrieren):
            rslt = await todo.run(prompt_fur_bookcover=self.rc.memory.get_by_action(coverKonzipieren)[0].content)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_json_file(jsonfile="ebookInfo.json", jsonvalue={"cover_link": rslt})
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg

        else:
            self._set_state(-1)
