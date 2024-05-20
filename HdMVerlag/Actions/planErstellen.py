from metagpt.actions import Action


class planErstellen(Action):

    PROMPT_TEMPLATE: str = """
    #Context:{context}
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von {genre} Büchern zu dem Thema "{thema}" und mit der Tonalität {tonalitaet}. Du arbeitest zusammen mit einem Verlagseditor an einem E-Book. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß der Aufgabenstellung, die der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. Beachte alle Anforderungen des Editors.

#Im ersten Schritt musst du ein Plan für E-Book Erstellung ausdenken. Formuliere deine Ideen so knapp und konkret wie möglich.

#Deine Schritte:

## Identifiziere und ausliste sehr kurz die Hauptthemen und Ideen, die in dem E-Book erkundet werden sollen.

## Beschreibe kurz eine Umgebung, an der sich die Handlung abspielt:
Wenn du über die reale Welt schreibst, wähle ein Land, die Stadt und die einzelne Lokationen, an der sich die Handlung abspielt. Entscheide dich auch für eine konkrete Epoche (Zeiten) und beschreibe sie.
Wenn du eine fiktive Welt erschaffst, beschreibe auch diese Welt, ausdenke und beschreibe den Ort und die Lokationen, an dem sich die Ereignisse abspielen.

## Ausdenke und entwickle vier passende Charaktere mit Namen und skizziere ihre Hintergrundgeschichten und Entwicklungen im Laufe des Buches.

## Ausdenke und schreibe eine Synopsis für jedes Kapitell basierend auf dem Inhaltsverzeichnis. Wichtig: Jedes Kapitel muss aus drei Teilen bestehen. Du muss auch 3 kleine Synopsen für 3 Teile erstellen. 3 kleine Synopsen müssen mit einander logisch verbunden und bleiben die Synopsis des Kapitels. Alle oben beschriebenen Charaktere müssen einbezogen werden. Sei kreativ und schaffe dramatische Wendungen in der Handlung. Es sollte eine kohärente und vollständige Geschichte sein. Du bist nicht berechtigt, zusätzliche Kapitel hinzuzufügen oder das Inhaltsverzeichnis zu ändern."
#Output: Gib json ```json your_code_here ``` ohne andere Texte zurück (Beachten!!! Kein Syntax Fehler im JSON format):
{{buchPlan:
{{
    "Hauptthemen und Ideen": "",
    "Umgebung": "",
    "Charaktere":"",
    "Synopsis pro Kapitel": {{
"Kapitel 1":
        {{
            "Kapitel Titel": "",
            "Synopsis": "",
            "Untersynopsen": {{"teil 1":"", "teil 2": "", "teil 2": ""}}
        }},

...
    
    }}
}}
}}
    """
    name: str = "planErstellen"

    async def run(self, context: str, genre: str, thema: str, tonalitaet: str, anzahlvonkapitel: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, thema=thema, tonalitaet=tonalitaet, anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """

        """
        return rsp
