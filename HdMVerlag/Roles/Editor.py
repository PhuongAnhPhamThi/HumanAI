from metagpt.actions import UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.recherchieren import Recherchieren
from Actions.konzeptErstellen import konzeptErstellen
from Actions.coverKonzipieren import coverKonzipieren
from Actions.illustrieren import illustrieren
from Actions.metadatenZusammenfassen import metadatenZusammenfassen
from Archive.titelErstellen import titelErstellen
from Archive.titelEmpfehlen import titelEmpfehlen
from Actions.planErstellen import planErstellen
from Actions.textErstellenKapitel import textErstellenKapitel
from Actions.allgInfoErstellen import allgInfoErstellen
from Actions.ideaEmpfehlen import ideaEmpfehlen
from Actions.konzeptVorbereiten import konzeptVorbereiten
from Actions.textKorrigieren import textKorrigieren
from workspace.Utils.json_handle import extract_json_from_string, write_to_json_file
from workspace.Utils.text_handle import write_to_txt_file

class Editor(Role):
    name: str = "Bob"
    profile: str = "Editor"
    language: str = "German"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch(
            [UserRequirement, Recherchieren, konzeptErstellen, titelErstellen, titelEmpfehlen,
             illustrieren, coverKonzipieren, metadatenZusammenfassen, ideaEmpfehlen,textKorrigieren])

    async def _think(self) -> bool:

        last_memory = self.get_memories(k=1)

        # check if memory is only request from human & content is not leer => do the research & create concept
        # request for autor.
        if last_memory[0].role == "Human" and len(
                self.get_memories()) < 2 and last_memory[0].content != "":
            self.set_actions([Recherchieren])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Human_User" and len(self.rc.memory.get_by_action(ideaEmpfehlen)) > 0 and len(
                self.rc.memory.get_by_action(konzeptVorbereiten)) == 0:
            await self._actKonzeptVorbereiten()
            self.set_actions([konzeptErstellen])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Human_User" and len(self.rc.memory.get_by_action(textKorrigieren)) > 0 and len(
                self.rc.memory.get_by_action(coverKonzipieren)) == 0:
            self.set_actions([coverKonzipieren])
            self._set_state(0)
            return True

        elif last_memory[0].role == "Human_User" and len(self.rc.memory.get_by_action(illustrieren)) > 0 and len(
                self.rc.memory.get_by_action(metadatenZusammenfassen)) == 0:
            self.set_actions([metadatenZusammenfassen])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        logger.info(todo)
        use_input = extract_json_from_string(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = use_input["genre"]
        thema = use_input["thema"]
        tonalitaet = use_input["tonalitaet"]
        anzahlvonkapitel = use_input["anzahlvonkapitel"]

        if isinstance(todo, konzeptErstellen):
            context1 = self.rc.memory.get_by_action(konzeptVorbereiten)[0].content
            context2 = self.rc.memory.get_by_action(ideaEmpfehlen)[0].content
            rslt = await todo.run(context1=context1, context2=context2)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg
        elif isinstance(todo, Recherchieren):
            rslt = await todo.run(genre=genre, thema=thema, tonalitaet=tonalitaet,
                                      anzahlvonkapitel=anzahlvonkapitel)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                                  text=rslt)
            return msg

        elif isinstance(todo, titelErstellen):
            context = self.rc.memory.get_by_action(Recherchieren)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg

        elif isinstance(todo, coverKonzipieren):
            context = self.rc.memory.get_by_action(planErstellen)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg

        elif isinstance(todo, metadatenZusammenfassen):
            context = self.rc.memory.get_by_action(allgInfoErstellen)[0].content
            rslt = await todo.run(context=context)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            rslt_json = extract_json_from_string(rslt)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            write_to_json_file(jsonfile="ebookInfo.json", key="metadaten", jsonvalue=rslt_json)
            return msg

        else:
            self._set_state(-1)

    async def _actRecherchieren(self) -> Message:
        use_input = extract_json_from_string(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = use_input["genre"]
        thema = use_input["thema"]
        tonalitaet = use_input["tonalitaet"]
        anzahlvonkapitel = use_input["anzahlvonkapitel"]
        self.set_actions([Recherchieren])
        todo = self.set_todo(Recherchieren())
        todo = self.rc.todo
        logger.info(todo)
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, Recherchieren):
            rslt = await todo.run(genre=genre, thema=thema, tonalitaet=tonalitaet,
                                  anzahlvonkapitel=anzahlvonkapitel)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg
        else:
            self._set_state(-1)
            pass

    async def _actKonzeptVorbereiten(self) -> Message:
        use_input = extract_json_from_string(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = use_input["genre"]
        thema = use_input["thema"]
        tonalitaet = use_input["tonalitaet"]
        anzahlvonkapitel = use_input["anzahlvonkapitel"]
        self.set_actions([konzeptVorbereiten])
        todo = self.set_todo(konzeptVorbereiten())
        todo = self.rc.todo
        logger.info(todo)
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        if isinstance(todo, konzeptVorbereiten):
            context = self.rc.memory.get_by_action(ideaEmpfehlen)[0].content
            rslt = await todo.run(context=context,genre=genre, thema=thema, tonalitaet=tonalitaet, anzahlvonkapitel=anzahlvonkapitel)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg
        else:
            self._set_state(-1)
            pass

