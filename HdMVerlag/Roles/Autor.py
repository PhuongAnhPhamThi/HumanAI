import json
from metagpt.actions import UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.konzeptErstellen import konzeptErstellen
from Actions.allgInfoErstellen import allgInfoErstellen
from Actions.planErstellen import planErstellen
from Actions.textErstellenKapitel import textErstellenKapitel
from workspace.Utils.json_handle import extract_json_from_string, write_to_json_file
from workspace.Utils.text_handle import write_to_txt_file

finishwriting = 0

class Autor(Role):
    name: str = "Maja Schmidt"
    profile: str = "Autor"
    language: str = "German"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([konzeptErstellen, allgInfoErstellen, planErstellen])

    async def _think(self) -> bool:
        last_memory = self.get_memories(k=1)
        if last_memory[0].role == "Editor" and len(self.rc.memory.get_by_action(konzeptErstellen)) > 0 \
                and len(self.rc.memory.get_by_action(allgInfoErstellen)) == 0:
            self.set_actions([allgInfoErstellen])
            self._set_state(0)
            return True
        elif last_memory[0].role == "Autor" and len(self.rc.memory.get_by_action(allgInfoErstellen)) > 0 \
                and len(self.rc.memory.get_by_action(planErstellen)) == 0:
            await self._actPlanErstellen()
            self.set_actions([textErstellenKapitel])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        use_input = extract_json_from_string(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = use_input["genre"]
        thema = use_input["thema"]
        tonalitaet = use_input["tonalitaet"]
        anzahlvonkapitel = use_input["anzahlvonkapitel"]

        if isinstance(todo, allgInfoErstellen):
            context = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet,
                                  anzahlvonkapitel=anzahlvonkapitel)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.env.publish_message(msg)
            rslt_json = extract_json_from_string(rslt)
            write_to_json_file(jsonfile="ebookInfo.json", jsonvalue=rslt_json)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            return msg

        elif isinstance(todo, planErstellen):
            context = self.rc.memory.get_by_action(konzeptErstellen)[0].content
            rslt = await todo.run(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet,
                                  anzahlvonkapitel=anzahlvonkapitel)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)
            write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                              text=rslt)
            self.rc.env.publish_message(msg)
            return msg

        elif isinstance(todo, textErstellenKapitel):
            global finishwriting
            context1 = self.rc.memory.get_by_action(planErstellen)[0].content
            context_json = extract_json_from_string(context1)
            kapitelnummer = len(context_json["buchPlan"]["Synopsis pro Kapitel"])
            text_teil = ""
            for i in range(1, kapitelnummer + 1):
                text = ""
                for j in range(1, 4):
                    if text_teil == "":
                        rslt = await todo.run(context1=context1, context2="", genre=genre, thema=thema,
                                              tonalitaet=tonalitaet,
                                              kapitelnummer=i, teilnummer=j)

                    else:
                        rslt = await todo.run(context1=context1,
                                              context2=text_teil,
                                              genre=genre, thema=thema,
                                              tonalitaet=tonalitaet,
                                              kapitelnummer=i, teilnummer=j)
                    text_teil = rslt
                    msg = Message(content=rslt, role=self.profile, cause_by=type(todo))

                    rslt_json = extract_json_from_string(rslt)
                    kapitel_key = list(rslt_json.keys())[0]
                    teil_key = list(rslt_json[kapitel_key].keys())[1]
                    text = text + " " + rslt_json[kapitel_key][teil_key]
                    write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile,
                                      action=self.rc.todo.name,
                                      text=rslt)

                    # Open file to get current data

                kapitel_json = {kapitel_key: {
                    "Kapitel Titel": rslt_json[kapitel_key]["Kapitel Titel"],
                    "Kapitel Inhalt": text
                }},

                write_to_json_file(jsonfile="ebookInfo.json", key="kapiteln", jsonvalue=kapitel_json[0])
            finishwriting = 1
            self.rc.env.publish_message(msg)
            return msg

        else:
            self._set_state(-1)

    async def _actPlanErstellen(self) -> Message:
        use_input = extract_json_from_string(self.rc.memory.get_by_action(UserRequirement)[0].content)
        genre = use_input["genre"]
        thema = use_input["thema"]
        tonalitaet = use_input["tonalitaet"]
        anzahlvonkapitel = use_input["anzahlvonkapitel"]
        todo = self.set_todo(planErstellen())
        todo = self.rc.todo
        logger.info(todo)
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        context = self.rc.memory.get_by_action(konzeptErstellen)[0].content
        rslt = await todo.run(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet,
                              anzahlvonkapitel=anzahlvonkapitel)
        msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
        self.rc.memory.add(msg)
        write_to_txt_file(txt="conversation.txt", actiontype="a", rolle=self.profile, action=self.rc.todo.name,
                          text=rslt)
        self.rc.env.publish_message(msg)
        return msg
