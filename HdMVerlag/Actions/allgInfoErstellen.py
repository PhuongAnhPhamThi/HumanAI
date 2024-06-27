from metagpt.actions import Action


class allgInfoErstellen(Action):
    PROMPT_TEMPLATE: str = """
    #Context:{context} 
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von {genre} Büchern zu dem Thema "{thema}" und mit der Tonalität {tonalitaet}. Du arbeitest zusammen mit einem 
    Verlagseditor an einem E-Book. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß 
    der Aufgabenstellung, die der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. 
    Beachte alle Anforderungen des Editors. 
    # Dein erster Schritt - allgemeine Teile des Manuskripts 
    zusammenzufassen: Titel und Name der Autorin. Zusätzlich dazu verfasse einen kurzen Text über dich selbst - die 
    Autorenvita - um sich dem potenziellen Leser des Buches vorzustellen. Anschließend platziere das 
    Inhaltsverzeichnis ({anzahlvonkapitel} Kapitel(n)). Inhaltsverzeichnis darf nur aus den Titeln der Kapitel bestehen.
    # Output: Gib json ```json your_code_here ``` ohne andere Texte zurück:
    {{
        autor: "",
        autorenvita: "",
        titel: nimm den Titel des Buchs aus Context,
        inhaltverzeichnis: "",
    }}
    """
    name: str = "allgInfoErstellen"

    async def run(self, context: str, genre: str, thema: str, tonalitaet: str, anzahlvonkapitel: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet,
                                             anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        return rsp
