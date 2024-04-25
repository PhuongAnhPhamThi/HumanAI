import fire
import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team


class textEditieren(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Als Autorin arbeitest du weiter mit einem Editor zusammen. Der Editor hat deinen Manuskript (siehe Context 1) gelesen und Empfehlungen in der Rezension gegeben, wie du ihn verbessern und Fehler korrigieren kannst. Die Rezension findest du im Context 2. Lies die Rezension sorgfältig durch und bearbeite deinen Manuskript so, wie der Editor es von dir verlangt. Zeige das Ergebnis deiner Arbeit - den bearbeiteten Manuskript.
    # Output: überarbeiteter/verbesserter Text:
    """
    name: str = "textEditieren"

    track_Autor: int = 0

    async def run(self, context1: str, context2: str):
        global track_Autor  # Declare track_author as a global variable if you haven't done it outside the class
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        self.track_Autor += 1  # Increment the value of track_author using self to reference the class variable
        print("Author " + str(self.track_Autor) + " :::::::::::::::::::::::::::::::::::::::")
        rsp = await self._aask(prompt)
        return rsp
