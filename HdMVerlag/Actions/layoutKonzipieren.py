from metagpt.actions import Action


class layoutKonzipieren(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: {context2}
# Context 3: {context3}
# Du bist ein Editor, der gerade die endgültige Version des Ebook-Textes genehmigt hat. Auch das Cover des Ebooks ist bereits auf der Grundlage deinem Prompt gezeichnet worden (siehe Context 3). Nun solltest du alle Materialien an den Layout Designer zur weiteren Bearbeitung weitergeben. Welche Empfehlungen und Anweisungen für die weitere Arbeit kannst du dem Layout Designer auf der Grundlage des Textes des Buches (siehe Context 1) und des Konzepts des Buches (siehe Context 2) geben. Fasse diese in Form einer Liste zusammen.
# Output: Aufgabestellung für Layout Designer:
    """

    name: str = "layoutKonzipieren"

    async def run(self, context1: str, context2: str, context3: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2, context3=context3)
        rsp = await self._aask(prompt)
        return rsp
