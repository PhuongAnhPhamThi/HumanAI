
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team

from Actions.recherchieren import Recherchieren
from Actions.konzeptErstellen import konzeptErstellen
from Actions.textErstellen import textErstellen


class Researcher(Role):
    name: str = "Mavier"
    profile: str = "Researcher"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([Recherchieren, konzeptErstellen])
        self._set_react_mode(react_mode="by_order")
        self._watch([UserRequirement, Recherchieren])
"""
    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        context = self.get_memories(k=1)[0]  # use last memories as context
        rslt = await todo.run(context)  # specify arguments
        msg = Message(content=rslt, role=self.profile, cause_by=type(todo))
        self.rc.memory.add(msg)
        return msg
"""
