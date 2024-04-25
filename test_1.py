import fire

import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.memory import Memory
from metagpt.team import Team
# from Roles.Reseacher import Researcher
# from Roles.Autor import Autor

import re
from metagpt.actions import Action


class Write(Action):
    PROMPT_TEMPLATE: str = """
    {instruction} 
    your content:
    """

    name: str = "Write"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)
        rsp = await self._aask(prompt)
        return rsp


class Edit(Action):
    PROMPT_TEMPLATE: str = """
    Content: {context}
    Read the context and create a title for content.
    Your output here:
    """

    name: str = "Edit"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp


class writeRezension(Action):
    PROMPT_TEMPLATE: str = """
    Content: {context}
    write a comment über content in Context
    Your output here:
    """

    name: str = "writeRezension"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp


class Translate(Action):
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Task: Translate context to Vietnamese.
    Your output here:
    """

    name: str = "Translate"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp


class Translate_to_chinese(Action):
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Task: Translate context to Chinese.
    Your output here:
    """

    name: str = "Translate_to_chinese"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp


class Design(Action):
    PROMPT_TEMPLATE: str = """
    {instruction}
    #Output: Your HTML code: 
    """

    name: str = "Design"
    goal: str = "Design Layout for EBook"

    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)
        rsp = await self._aask(prompt)
        return rsp


class Writer(Role):
    name: str = "Alice"
    profile: str = "Writer"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([Write])
        self._watch([UserRequirement])

    async def _act(self) -> Message:
        if self.rc.memory.get_by_action(UserRequirement)[0].content != "":
            logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
            todo = self.rc.todo
            msg = self.get_memories(k=1)[0]  # find the most recent messages
            text = await todo.run(msg.content)
            msg = Message(content=text, role=self.profile, cause_by=type(todo))
            with open('example.txt', 'a') as file:
                file.write(self.profile + "\n")
                file.write(text + "\n\n")
            return msg
        else:
            self._set_state(-1)


class Editor(Role):
    name: str = "Tom"
    profile: str = "Editor"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([Write,Edit,writeRezension])
        self._watch([UserRequirement,Write, Edit,writeRezension])


    async def _think(self) -> bool:
        last_memory = self.get_memories(k=1)
        logger.info(len(self.get_memories()))
        #if len(self.get_memories()) > 6:
            #self._set_state(-1)
            #return False
        if len(self.get_memories()) < 3:
            self.set_actions([Edit])
            self._set_state(0)
            return True
        elif len(self.get_memories())> 3 :
            self.set_actions([writeRezension])
            self._set_state(0)
            return True

    async def _act(self) -> Message:
        
        print(self.get_memories())
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        msg = self.get_memories(k=1)[0]  # find the most recent messages
        text = await todo.run(msg.content)
        msg = Message(content=text, role=self.profile, cause_by=type(todo))
        return msg



class Translator(Role):
    name: str = "Anh"
    profile: str = "Translator"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([Translate])
        self._watch([Write])

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo
        msg = self.get_memories(k=1)[0]  # find the most recent messages
        text = await todo.run(msg.content)
        msg = Message(content=text, role=self.profile, cause_by=type(todo))
        print("your Info:")
        print(self.rc.memory.get_by_action(Write)[0].role == "Writer")
        return msg


class Designer(Role):
    name: str = "Tom"
    profile: str = "Designer"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([Design])
        self._watch([UserRequirement])


async def main(
        idea: str = """
                    write a haiku poet in 4 lines.
                """,


        investment: float = 0.05,
        n_round: int = 6,
        add_human: bool = False,
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            Editor(),
            #Writer(),
            #Translator(),
            # Designer()
        ]
    )

    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)


if __name__ == "__main__":
    fire.Fire(main)
