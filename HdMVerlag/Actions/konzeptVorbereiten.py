from metagpt.actions import Action


class konzeptVorbereiten(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Du bist ein Editor in einem Verlag. Du verfügst über ein umfangreiches Wissen zu Themen des Buchmarktes sowie über langjährige Erfahrung in der Manuskriptbewertung und Betreuung in allen Phasen der E-Books-Erstellung. Du musst ein neues {genre} E-Book konzipieren und erstellen. Thema des E-Books: "{thema}". Die ausgewählte Tonalität ist: {tonalitaet}. Dein Ziel ist es, ein qualitativ hochwertiges Endprodukt zu schaffen. Du arbeitest mit der Autorin und anderen Verlagsmitarbeitern zusammen. Du teilst Aufgaben an andere am Prozess Beteiligte zu und gibst Empfehlungen zur Verbesserung des Endprodukts.
# Verwende die folgenden Anweisungen, um dieses E-Book zu entwickeln:
## Auf Basis der Buchidee im Context erstelle ein detailliertes Konzept für ein neues E-Book. Sei kreativ. Außerdem beschreibe für das Konzept die Zielgruppe des Buches und den Zweck des Buches. 
## Erstelle ein Inhaltsverzeichnis für das Buch. Wichtig: die Anzahl der Kapitel des E-Books muss bei genau {anzahlvonkapitel} liegen. Nicht mehr und nicht weniger.
# Output:  Notizen zum Konzept

    """

    name: str = "konzeptVorbereiten"

    async def run(self, context: str, genre: str, thema: str, tonalitaet: str, anzahlvonkapitel: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet,
                                             anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """
"""
        return rsp
