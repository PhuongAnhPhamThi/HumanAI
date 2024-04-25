import fire
import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team

track_Autor: int = 0


class textEditierenZiklus(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Du bist eine Autorin, die bzw. der bereits von einem Editor eine Rezension deines Manuskripts erhalten hat und das Buch entsprechend den Empfehlungen des Editors überarbeitet hat. Du hast das überarbeitete Manuskript erneut eingesandt (siehe Context 2) und eine Antwort des Editors erhalten (siehe Context 1). Wenn die Antwort den Satz "sieht gut aus."/"Sieht gut aus." enthält, musst du nichts weiteres machen. Wenn die Antwort weitere Punkte zur Verbesserung deines Manuskripts enthält, nimm die Korrekturen vor und zeige das überarbeitete Manuskript
    # Output: überarbeiteter/verbesserter Text:
    """
    name: str = "textEditierenZiklus"

    async def run(self, context1: str, context2: str):
        global track_Autor  # Declare track_author as a global variable if you haven't done it outside the class
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        track_Autor += 1  # Increment the value of track_author using self to reference the class variable
        print("Author " + str(track_Autor) + " :::::::::::::::::::::::::::::::::::::::")
        rsp = await self._aask(prompt)
        return rsp
