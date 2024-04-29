from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.illustrieren import illustrieren
from Actions.coverKonzipieren import coverKonzipieren
from Editor import file_path

class Illustrator(Role):
    name: str = "Frida"
    profile: str = "Illustrator"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([illustrieren])
        self._watch([coverKonzipieren])

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        rslt = await todo.run(prompt_fur_bookcover=self.rc.memory.get_by_action(coverKonzipieren)[0].content)
        msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
        with open(file_path + "conversation.txt", 'a') as file:
            file.write("******" + self.profile + " - " + self.rc.todo.name + " :\n")
            file.write(
                rslt + " \n\n" + "-------------------------------------------------------------------------------------------------" + "\n\n\n")
        return msg
