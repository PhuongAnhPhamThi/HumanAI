import json
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from Actions.illustrieren import illustrieren
from Actions.coverKonzipieren import coverKonzipieren


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
        msg = self.rc.memory.get_by_action(coverKonzipieren)[0].content
        text = await todo.run(context=msg)
        msg = Message(content=text, role=self.profile, cause_by=type(todo))
        return msg
