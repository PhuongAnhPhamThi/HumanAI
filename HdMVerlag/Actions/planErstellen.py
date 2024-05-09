from metagpt.actions import Action


class planErstellen(Action):

    PROMPT_TEMPLATE: str = """
    #Context:{context}
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von Büchern zu dem Thema {genre}, in Form von {gattung} und mit der Tonalität {tonalitaet}. Du arbeitest zusammen mit einem Verlagseditor an einem E-Book. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß der Aufgabenstellung, die der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. Beachte alle Anforderungen des Editors.

Im ersten Schritt musst du ein Plan und für E-Book Erstellung ausdenken. Formuliere deine Ideen so knapp und konkret wie möglich.

Deine Schritte:

Identifiziere und ausliste sehr kurz die Hauptthemen und Ideen, die in dem E-Book erkundet werden sollen.

Entscheide dich für eine Umgebung, an der sich die Handlung abspielt.
Wenn du über die reale Welt schreibst, wähle ein Land, die Stadt und die einzelne Lokationen, an der sich die Handlung abspielt. Entscheide dich auch für eine konkrete Epoche (Zeiten) und beschreibe sie.
Wenn du eine fiktive Welt erschaffst, beschreibe auch diese Welt, ausdenke und beschreibe den Ort und die Lokationen, an dem sich die Ereignisse abspielen.

Ausdenke und entwickle drei passende Charaktere mit Namen und skizziere ihre Hintergrundgeschichten und Entwicklungen im Laufe des Buches.
Beachte dass DEIN BUCH HAT {anzahlvonkapitel} KAPITEL!!!. Ausdenke und schreibe eine Synopsis für jedes Kapitel basierend auf dem Inhaltsverzeichnis. Alle oben beschriebenen Charaktere müssen einbezogen werden. Sei kreativ und schaffe dramatische Wendungen in der Handlung. Es sollte eine kohärente und vollständige Geschichte sein. Du bist nicht berechtigt, zusätzliche Kapitel hinzuzufügen oder das Inhaltsverzeichnis zu ändern".)
#Output: Gib json ```json your_code_here ``` ohne andere Texte zurück:
{{buchPlan:
{{
    "Hauptthemen und Ideen": "",
    "Umgebung": "",
    "Charaktere":"",
    "Synopsis pro Kapitel": {{
"Kapitel 1":
        {{
            "Kapitel Titel": "",
            "Synopsis": ""
        }},

...
    
    }}
}}
}}
    """
    name: str = "planErstellen"

    async def run(self, context: str, genre: str, gattung: str, tonalitaet: str, anzahlvonkapitel: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, gattung=gattung, tonalitaet=tonalitaet, anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """
        {
    "buchPlan": {
        "Hauptthemen und Ideen": "Magie, Prophezeiung, Dunkelheit vs. Licht, Schicksal, Mut, Freundschaft",
        "Umgebung": {
            "Art": "Fiktive Welt",
            "Beschreibung": "Eine Welt voller Magie, Geheimnisse und Intrigen, mit verschiedenen Ländern, alten Stätten der Macht und düsteren Landschaften."
        },
        "Charaktere": [
            {
                "Name": "Lyra",
                "Hintergrundgeschichte": "Junge Magierin, bestimmt, das Gleichgewicht zwischen Licht und Dunkelheit wiederherzustellen.",
                "Entwicklung": "Wächst über sich hinaus, entdeckt ihre Stärke und kämpft gegen ihre Zweifel."
            },
            {
                "Name": "Finn",
                "Hintergrundgeschichte": "Tapferer Krieger, der Lyra auf ihrer Reise begleitet.",
                "Entwicklung": "Entwickelt eine enge Bindung zu Lyra und entdeckt seinen eigenen inneren Konflikt."
            },
            {
                "Name": "Elena",
                "Hintergrundgeschichte": "Geheimnisvolle Verbündete von Lyra, mit tiefen Kenntnissen über die alten Prophezeiungen.",
                "Entwicklung": "Enthüllt nach und nach ihre wahren Absichten und Motivationen."
            }
        ],
        "Synopsis pro Kapitel": {
            "Kapitel 1": {
                "Kapitel Titel": "Das Erwachen der Prophezeiung",
                "Synopsis": "Lyra erfährt von ihrer Bestimmung und begibt sich auf eine Reise, um die Mächte des Lichts und der Dunkelheit zu verstehen."
            },
            "Kapitel 2": {
                "Kapitel Titel": "Die Prüfung der Magie",
                "Synopsis": "Lyra reist zu den uralten Stätten der Macht, wo sie finstere Kräfte konfrontiert und ihre eigene Magie auf die Probe gestellt wird."
            },
            "Kapitel 3": {
                "Kapitel Titel": "Das Schicksal der Ewigen",
                "Synopsis": "In der finalen Schlacht kämpft Lyra an der Seite ihrer Verbündeten gegen die Dunkelheit, um das Gleichgewicht der Welt wiederherzustellen."
            }
        }
    }
}


        """
        return rsp
