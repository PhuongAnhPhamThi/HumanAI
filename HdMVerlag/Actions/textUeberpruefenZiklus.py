import fire
import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team

class textUeberpruefenZiklus(Action):
    PROMPT_TEMPLATE: str = """
    # Context 1:{context1}
    # Context 2:{context2}
    # Du bist ein Verlagseditor, der einer Autorin bereits Vorschläge gemacht hat, wie sie ihren Text für ein E-Book verbessern kann (siehe Context 2). Du hast gerade eine korrigierte Version des Buches von ihr erhalten - Context 1.   Überprüfe, ob alle deine Anpassungen von der Autorin vorgenommen wurden. Wenn sie nicht alle Punkte, die du in Context 2 angegeben hast, erledigt hat, führe die nicht erledigte Punkte in Listenform auf. Wenn das Manuskript keine weiteren Fehler aufweist und nicht überarbeitet werden muss, schreibe den Satz: "Sieht gut aus.".
    # Output: Antwort von Editor (Bestätigung, dass der Text gut genug ist "Sieht gut aus." / Empfehlung zur weiteren Textverbesserung):
    """
    name: str = "textUeberpruefenZiklus"


    async def run(self, context1: str, context2: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        rsp = await self._aask(prompt)
        return rsp
