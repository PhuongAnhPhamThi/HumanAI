import fire

import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team


class konzeptErstellen(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Erstelle auf der Grundlage deiner Notizen im Context eine detaillierte Anleitung für die Autorin oder den Autor, wie sie dieses Buch schreiben soll. Wiederhole in der Anleitung zusätzlich deine Ausarbeitungen wie z.B.: Arbeitstitel, ausführliche Beschreibung der Zielgruppe, Gliederung, Inhaltsverzeichnis, Tonalität.
# Output: Aufgabenstellung für Autorin:
    """

    name: str = "konzeptErstellen"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp
