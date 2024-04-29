from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.illustrieren import illustrieren
from Actions.layoutErstellenHTML import layoutErstellenHTML
from Actions.layoutKonzipieren import layoutKonzipieren
from Actions.buchZusammenfassen import buchZusammenfassen
from Editor import file_path,Editor


class LayoutDesigner(Role):
    name: str = "Johnny"
    profile: str = "LayoutDesigner"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([layoutErstellenHTML])
        self._watch([layoutKonzipieren, illustrieren, buchZusammenfassen])


    async def _think(self) -> bool:

        if len(self.rc.memory.get_by_action(layoutKonzipieren)) > 0 and len(self.rc.memory.get_by_action(illustrieren)) > 0:
            self.set_actions([layoutErstellenHTML])
            self._set_state(0)
            return True

        else:
            self._set_state(-1)
            return False

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        if isinstance(todo, layoutErstellenHTML):
            #context1 = self.rc.memory.get_by_action(buchZusammenfassen)[0].content
            with open(file_path + "buch_zusammenfassung.txt", 'r',encoding="utf-8") as file:
                context1 = file.read()
            context2 = self.rc.memory.get_by_action(layoutKonzipieren)[0].content
            link = self.rc.memory.get_by_action(illustrieren)[0].content
            rslt = await todo.run(context1=context1, context2=context2, link=link)
            with open(file_path + "ebook.html", "w", encoding="utf-8") as file:
                html_string = rslt.strip()[7:-7]
                file.write(html_string)
            msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
            self.rc.memory.add(msg)

            with open(file_path + "conversation.txt", 'a') as file:
                file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
                file.write(
                    rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")

            self._set_state(-1)
            return msg

        else:
            self._set_state(-1)



