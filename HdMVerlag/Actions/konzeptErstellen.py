from metagpt.actions import Action


class konzeptErstellen(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: {context2}
# Erstelle auf der Grundlage deiner Notizen im Context 1 und einer endgültigen Buchidee im Context 2 eine detaillierte Anleitung für die Autorin oder den Autor, wie sie dieses Buch schreiben soll. Wiederhole in der Anleitung zusätzlich deine Ausarbeitungen w wie sie dieses Buch schreiben soll. Wiederhole in der Anleitung zusätzlich deine Ausarbeitungen wie: Titel des Buches, Beschreibung der Zielgruppe,Inhaltsverzeichnis. Wichtig: Inhaltsverzeichnis muss genau wie im Context 1 sein!!!
# Output: Aufgabenstellung für Autorin:

    """

    name: str = "konzeptErstellen"

    async def run(self, context1: str, context2: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        rsp = await self._aask(prompt)
        return rsp
