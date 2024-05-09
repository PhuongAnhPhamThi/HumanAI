from metagpt.actions import Action


class allgInfoErstellen(Action):
    PROMPT_TEMPLATE: str = """
    #Context:{context}
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von Büchern zu dem Thema {genre}, in Form von {gattung} und mit der Tonalität {tonalitaet}. Du arbeitest zusammen mit einem Verlagseditor an einem E-Book. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß der Aufgabenstellung, die der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. Beachte alle Anforderungen des Editors. Dein erster Schritt - allgemeine Teile des Manuskripts zusammenzufassen: arbeitstitel und Name der Autorin. Zusätzlich dazu verfasse einen kurzen Text über dich selbst - die Autorenvita -, um sich dem potenziellen Leser des Buches vorzustellen. Anschließend platziere das Inhaltsverzeichnis ({anzahlvonkapitel} Kapitel(n)".)
    # Output: Gib json ```json your_code_here ``` ohne andere Texte zurück:
    {{
        autor: "",
        autorenvita: "",
        titel: "",
        inhaltverzeichnis: "",
    }}
    """
    name: str = "allgInfoErstellen"

    async def run(self, context: str, genre: str, gattung: str, tonalitaet: str, anzahlvonkapitel: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, gattung=gattung, tonalitaet=tonalitaet,
                                             anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """
{
    "autor": "Maja Schmidt",
    "titel": "",
    "autorenvita": "Maja Schmidt, eine Mystikerin der Worte, fängt in ihren Gedichten die Magie der Fantasie ein.",
    "inhaltverzeichnis": "I. Das Erwachen der Prophezeiung. 1. Einführung in die Welt von Lyra. 2. Die Enthüllung ihrer Bestimmung. I. Die Prüfung der Magie. 1. Lyras Reise zu den uralten Stätten der Macht. 2. Konfrontation mit dunklen Kräften. III. Das Schicksal der Ewigen. 1. Die finale Schlacht um das Gleichgewicht der Welt. 2. Der Triumph des Lichts über die Dunkelheit"
}


        """
        return rsp
