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
from Actions.textKorrigieren import textKorrigieren
from Actions.textErstellenKapitel import textErstellenKapitel
from Autor import finishwriting
from workspace.Utils.json_handle import write_to_json_file, extract_json_from_string
from workspace.Utils.text_handle import write_to_txt_file
import os
import json


class Human_User(Role):
    name: str = "Human_User"
    profile: str = "Human_User"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([titelEmpfehlen, illustrieren, textKorrigieren])
        self._watch([titelErstellen, coverKonzipieren, konzeptErstellen, ideaEmpfehlen, Recherchieren,illustrieren,textKorrigieren,textErstellenKapitel])

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

        elif len(self.rc.memory.get_by_action(textErstellenKapitel)) > 0 and len(
                self.rc.memory.get_by_action(textKorrigieren)) == 0:
            self.set_actions([textKorrigieren])
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

        elif isinstance(todo, textKorrigieren):
            file_path = os.path.join("workspace") + "/"
            with open(file_path + "ebookInfo.json", "r", encoding="utf-8") as f:
                json_data = json.load(f)
            # extract the kapiteln value
            kapiteln_value = json_data["kapiteln"]
            # Convert the "kapiteln" value to a JSON string
            kapiteln_json_string = json.dumps(kapiteln_value, indent=4, ensure_ascii=False)
            rslt = await todo.run(text_json=kapiteln_json_string)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            rslt_json = extract_json_from_string(rslt)
            write_to_json_file(jsonfile="ebookInfo.json", jsonvalue=rslt_json, key="kapiteln")
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg

        else:
            self._set_state(-1)
