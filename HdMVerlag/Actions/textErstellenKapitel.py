from metagpt.actions import Action


class textErstellenKapitel(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von {genre} Büchern zu dem Thema {thema} und mit der Tonalität {tonalitaet}. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß deinem Plan im Context.
    # Deine Aufgabe besteht darin, den Teil {teilnummer} des Kapitels {kapitelnummer} zu schreiben. Schreib nur den Text. Wiederhole nicht den Titel des Kapitels, den Titel des Teils und die Beschreibung des Teils. Halte dich klar an das Inhaltsverzeichnis und schreibe genau diesen Teil dieses Kapitels, nach dem ich frage. Der fertige Text sollte so lang wie möglich sein. Benutze alle beschriebene Charaktere. Der fertige Text ist ein interssante Geschichte mit faszinierendes Geschichtenerzählen und muss Dialog zwischen Charakter erhalten. Nimm die Untersynopsis des im Plan beschriebenen Kapitels als Grundlage (siehe Context 1). Benutze alle benannte Charaktere. Alle Informationen aus der Synopse sollten verwendet werden. Wenn Context 2 nicht leer ist, muss dein Text eine Folge von dem vorherigen Kapitel im Context 2 sein. Ich werde dir 10000 Euro schenken wenn du gutes Text schreiben kannst!
    #Output: Geben Sie „json“ ohne andere Texte zurück, dein json Code:
{{
Kapitel {kapitelnummer}:{{
"Kapitel Titel": finde die richtige Kapitel Titel aus Context 1,
"Kapitel Inhalt Teil {teilnummer}":""
}}
}}
    """
    name: str = "textErstellenKapitel"

    async def run(self, context1: str, context2:str, genre: str, thema: str, tonalitaet: str,  teilnummer: int, kapitelnummer: int):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2, genre=genre, thema=thema, tonalitaet=tonalitaet, teilnummer=teilnummer, kapitelnummer=kapitelnummer)
        rsp = await self._aask(prompt)
        rsp1 = """
"""
        return rsp
