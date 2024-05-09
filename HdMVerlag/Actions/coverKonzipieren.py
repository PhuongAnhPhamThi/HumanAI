from metagpt.actions import Action


class coverKonzipieren(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Du bist Editor in einem Verlag und arbeitest an einem E-Book weiter. Das Manuskript ist bereits fertig (siehe Context). Lies das Manuskript und erstelle einen Prompt für das neuronale Netzwerk DALL E, um ein passendes Cover für dieses Ebook zu generieren. Der Titel des Buches, der Name des Autors und jeglicher Fremdtext müssen nicht auf dem Cover angebracht werden
# Output: Prompt für Erstellung des Covers:
    """

    name: str = "coverKonzipieren"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        rsp1 = """
        
Generiere ein Buchcover f�r das E-Book "Haiku Harmony: Poems of Nature and Serenity" von Maja, das die Sch�nheit der Natur und die Ruhe der Poesie einf�ngt. Verwende nat�rliche Elemente wie Blumen, B�ume, Wasser oder Landschaften, um eine harmonische und beruhigende Atmosph�re zu schaffen. Betone die Einfachheit und zeitlose Sch�nheit der haiku-Gedichte, um die Leser zum Eintauchen in die Welt der Poesie und Natur zu inspirieren. 
        """
        return rsp
