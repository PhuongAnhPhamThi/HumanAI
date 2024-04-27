
from metagpt.actions import Action


class layoutErstellenHTML(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: {context1}
# Du bist ein Layout Designer und arbeitest in einem Verlag zusammen mit einem Editor an der Erstellung eines E-Books.
Der Lektor hat dir ein fertiges Buchmanuskript (siehe Context 1) und seine Empfehlungen für die weitere Arbeit daran gegeben (siehe Context 2). Unter Berücksichtigung der Empfehlungen des Editors und deiner beruflichen Erfahrung erstelle mit Hilfe geeigneter Markup-Sprachen das Layout des Buches und bereitest es für den nächsten Schritt - die Konvertierung ins EPUB-Format - vor.

Verwende die folgenden Anweisungen:

Fange mit dem Cover an. Gib einen Platz und einen Pfad für das Cover {link} an, das dann dem E-Book beigefügt wird.

Auf der nächsten Seite trag den Titel des Buches und den Namen des Autors ein.

Gestalte und platziere dann auf einer separaten Seite die Autorenvita.

Auf der nächsten Seite platziere das Inhaltsverzeichnis des E-Books. Beachte, dass der Inhalt des E-Books als Links zu den entsprechenden Kapiteln des Buches gestaltet werden sollte.

Formatiere und positioniere dann den Text des E-Books. Verwende den vollständigen Text und kürze nichts ab.

Auf der letzten Seite organisiere und ordne die folgende Metadaten dieses E-Bbooks:
Name des Autors
Name des Buches
Name des Herausgebers
Name des Verlags
Adresse des Verlags
Datum der Veröffentlichung

 Alle Daten im Text des E-Books, die dir der Editor vorgibt (siehe Context 1), müssen korrekt formatiert sein und im endgültigen Layout angezeigt werden.
 
Geben Sie „html dein_code_hier“ ohne andere Texte zurück. dein Code:
    """

    name: str = "layoutErstellenHTML"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp
