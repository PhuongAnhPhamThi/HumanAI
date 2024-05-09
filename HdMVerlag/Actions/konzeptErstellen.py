from metagpt.actions import Action


class konzeptErstellen(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: Titel: {context2}
# Erstelle auf der Grundlage deiner Notizen im Context 1 eine detaillierte Anleitung für die Autorin oder den Autor, wie sie dieses Buch schreiben soll. Wiederhole in der Anleitung zusätzlich deine Ausarbeitungen wie z.B.: Arbeitstitel (nimm der Titel im Context 2), ausführliche Beschreibung der Zielgruppe, Inhaltsverzeichnis, Beschreibung der Tonalität.
# Output: Aufgabenstellung für Autorin:

    """

    name: str = "konzeptErstellen"

    async def run(self, context1: str, context2: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        rsp = await self._aask(prompt)
        rsp1 = """
Aufgabenstellung für die Autorin:
Arbeitstitel: "Schatten der Ewigen"

Beschreibung der Zielgruppe:
Das Buch richtet sich an Jugendliche und junge Erwachsene im Alter von 14 bis 25 Jahren, die eine Leidenschaft für fantastische Welten, Magie und Abenteuer hegen. Sowohl männliche als auch weibliche Leser werden angesprochen. Diese Zielgruppe sucht nach einer fesselnden Handlung mit starken Charakteren und einer geheimnisvollen Atmosphäre.

Konzept:
"Schatten der Ewigen" ist eine epische Fantasygeschichte, die in einer Welt voller Magie, Geheimnisse und Intrigen spielt. Die Hauptprotagonistin ist eine junge Magierin namens Lyra, die von einer alten Prophezeiung dazu bestimmt ist, das Gleichgewicht zwischen Licht und Dunkelheit wiederherzustellen. Der Weg zur Erfüllung ihres Schicksals ist von Gefahren gesäumt, und sie muss sich gegen finstere Mächte behaupten, die ihre Pläne durchkreuzen wollen.

Tonalität:
Die mystische Tonalität wird durch eine reiche Sprache, poetische Beschreibungen und eine Atmosphäre des Geheimnisvollen und Unerklärlichen erreicht. Elemente wie verborgene Prophezeiungen, uralte Rituale und mysteriöse Wesen tragen dazu bei, eine Welt zu erschaffen, die die Fantasie der Leser beflügelt und sie in ihren Bann zieht.

Grobes Inhaltsverzeichnis:

I. Das Erwachen der Prophezeiung

Einführung in die Welt von Lyra
Die Enthüllung ihrer Bestimmung
II. Die Prüfung der Magie

Lyras Reise zu den uralten Stätten der Macht
Konfrontation mit dunklen Kräften
III. Das Schicksal der Ewigen

Die finale Schlacht um das Gleichgewicht der Welt
Der Triumph des Lichts über die Dunkelheit
Schreibanweisungen:

Beginne mit einer fesselnden Einführung, die die Leser sofort in die Welt von Lyra einführt und ihre Neugier weckt.
Stelle die Hauptfigur, Lyra, und ihre Motivationen deutlich dar, damit die Leser sich mit ihr identifizieren können.
Baue Spannung durch geschickt platzierte Wendungen und Enthüllungen auf, besonders während Lyras Reise und den Konfrontationen mit dunklen Mächten.
Achte darauf, die mystische Tonalität konsequent durch poetische Beschreibungen und das Einflechten von geheimnisvollen Elementen aufrechtzuerhalten.
Gib den Charakteren Tiefe, indem du ihre Entwicklung im Laufe der Geschichte zeigst und ihre Beziehungen untereinander ausbaust.
Schließe mit einem packenden Finale ab, das die Leser zufriedenstellt und sie auf weitere Abenteuer in dieser faszinierenden Welt hoffen lässt.
Abschluss:
"Schatten der Ewigen" soll die Leser in eine faszinierende Welt entführen, in der das Unmögliche möglich wird. Es bietet Unterhaltung, Spannung und regt zum Nachdenken über die Macht des Schicksals und die Bedeutung von Mut und Freundschaft an.
"""
        return rsp
