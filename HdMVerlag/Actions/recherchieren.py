from metagpt.actions import Action


class Recherchieren(Action):
    PROMPT_TEMPLATE: str = """# Du bist ein Editor in einem Verlag. Du verfügst über ein umfangreiches Wissen zu 
    Themen des Buchmarktes sowie über langjährige Erfahrung in der Manuskriptbewertung und Betreuung in allen Phasen 
    der E-Books-Erstellung. Du musst ein neues {genre} E-Book konzipieren und erstellen. Thema des E-Books: {thema} sein. Die ausgewählte Tonalität ist: {tonalitaet}. 
    # Schlage 5 Ideen für das E-Book mit Titeln vor. 
    # Output: Gib json ```json your_code_here ``` ohne andere Texte zurück: 
    {{ "Idea 1": {{ "Titel": "", "Idea": "" }}, 
    "Idea 2": {{ "Titel": "", "Idea": "" }}, "Idea 3": {{ "Titel": "", "Idea": "" }}, "Idea 4": {{ "Titel": "", 
    "Idea": "" }}, "Idea 5": {{ "Titel": "", "Idea": "" }}, }}"""

    name: str = "Recherchieren"

    async def run(self, genre: str, thema: str, tonalitaet: str, anzahlvonkapitel: int):
        prompt = self.PROMPT_TEMPLATE.format(genre=genre, thema=thema, tonalitaet=tonalitaet,
                                             anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """
       
"""
        return rsp
