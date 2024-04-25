import fire
import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team


class textErstellen(Action):

    PROMPT_TEMPLATE: str = """
    #Context:{context}
    #Du bist eine bekannte und erfahrene Autorin von Büchern zu dem Thema {thema}. Du arbeitest zusammen ie dmit einem Verlagseditor an einem E-Book. Schreibe ein hochwertiges und vollständiges Manuskript des Buches gemäß der Aufgabenstellung, der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. Beachte alle Anforderungen des Editors. Dein Manuskript muss aus folgenden Teilen bestehen: Titel, Inhaltsverzeichnis, E-Book-Text. Zusätzlich dazu verfasse einen kurzen Text über dich selbst - die Autorenvita -, um sich dem potenziellen Leser des Buches vorzustellen. Vergiss nicht, deinen Namen ausdenken und anzugeben. Deine Autorenvita darf nicht länger als 200 Zeichen sein.
    # Output: vollständige Manuskript:
    """
    name: str = "textErstellen"

    async def run(self, context: str, thema: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, thema=thema)
        rsp = await self._aask(prompt)
        return rsp
