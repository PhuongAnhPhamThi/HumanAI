from metagpt.actions import Action


class coverKonzipieren(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Du bist Editor in einem Verlag und arbeitest an einem E-Book weiter. Der Plan zur Manuskript-Erstellung ist bereits fertig (siehe Context). Lies der Plan und erstelle einen Prompt für das neuronale Netzwerk DALL E, um ein passendes Cover für dieses Ebook zu generieren. Dein Prompt darf nicht länger als 400 Zeichen sein. Der Titel des Buches, der Name des Autors und jeglicher Fremdtext müssen nicht auf dem Cover angebracht werden
# Output: Prompt für Erstellung des Covers:
    """

    name: str = "coverKonzipieren"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        rsp1 = """
 
        """
        return rsp
