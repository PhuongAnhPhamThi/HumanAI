from metagpt.actions import Action


class Recherchieren(Action):
    PROMPT_TEMPLATE: str = """
# Du bist ein Editor in einem Verlag. Du verfügst über ein umfangreiches Wissen zu Themen des Buchmarktes sowie über langjährige Erfahrung in der Manuskriptbewertung und Betreuung in allen Phasen der E-Books-Erstellung. Du musst ein neues {genre} E-Book konzipieren und erstellen. Das E-Book sollte in Form von {gattung} geschrieben sein. Die ausgewählte Tonalität ist: {tonalitaet}. Dein Ziel ist es, ein qualitativ hochwertiges Endprodukt zu schaffen. Du arbeitest mit der Autorin und anderen Verlagsmitarbeitern zusammen. Du teilst Aufgaben an andere am Prozess Beteiligte zu und gibst Empfehlungen zur Verbesserung des Endprodukts.

# Verwende die folgenden Anweisungen, um dieses E-Book zu entwickeln:

## In einem ersten Schritt wähle zehn besten Bücher im Bereich {genre} , in Form von {gattung} und mit der Tonalität {tonalitaet}. Notiere die Ergebnisse dieses Schrittes und aller folgenden Schritte.
##  Auf der Grundlage dieser Liste erstelle ein detailliertes Konzept für ein neues E-Book. Sei kreativ und versuche, von den Büchern deiner Konkurrenten zu unterscheiden. Außerdem beschreibe für das Konzept die Zielgruppe des Buches und den Zweck des Buches.
##  Beschreibe genau, wie der ausgewählte Tonalität des Buches verwendet sein muss, damit es bei der Zielgruppe gut ankommt.
##  Erstelle ein grobes Inhaltsverzeichnis für das Buch. Wichtig: die Anzahl der Kapitel des E-Books muss bei genau {anzahlvonkapitel} liegen. Nicht mehr und nicht weniger.
# Output: Notizen zum Konzept:

    """

    name: str = "Recherchieren"

    async def run(self, genre: str, gattung: str, tonalitaet: str, anzahlvonkapitel: int):
        prompt = self.PROMPT_TEMPLATE.format(genre=genre, gattung=gattung, tonalitaet=tonalitaet,
                                             anzahlvonkapitel=anzahlvonkapitel)
        rsp = await self._aask(prompt)
        rsp1 = """
        Notizen zum Konzept:
1. Die zehn besten Bücher im Bereich Fantasy mit mystischer Tonalität:
"Der Herr der Ringe" von J.R.R. Tolkien
"Die Nebel von Avalon" von Marion Zimmer Bradley
"Harry Potter und der Stein der Weisen" von J.K. Rowling
"Der Name des Windes" von Patrick Rothfuss
"Stadt der träumenden Bücher" von Walter Moers
"Die Chroniken von Narnia" von C.S. Lewis
"Der Dunkle Turm" von Stephen King
"Die Elfen" von Bernhard Hennen
"Die Gilde der schwarzen Magier" von Trudi Canavan
"Die Legenden der Albae" von Markus Heitz
2. Konzept für das neue E-Book:
Titel: "Schatten der Ewigen"

Konzept:
"Schatten der Ewigen" ist eine epische Fantasygeschichte, die in einer Welt voller Magie, Geheimnisse und Intrigen spielt. Im Mittelpunkt steht eine junge Magierin namens Lyra, die von einer alten Prophezeiung dazu bestimmt ist, das Gleichgewicht zwischen Licht und Dunkelheit wiederherzustellen. Doch der Weg zur Erfüllung ihres Schicksals ist von Gefahren gesäumt, und sie muss sich gegen finstere Mächte behaupten, die ihre Pläne durchkreuzen wollen.

Zielgruppe:
Das Buch richtet sich an Jugendliche und junge Erwachsene, die sich für fantastische Welten, Magie und Abenteuer begeistern. Es spricht sowohl männliche als auch weibliche Leser an, die eine fesselnde Handlung mit starken Charakteren und einer geheimnisvollen Atmosphäre suchen.

Zweck:
"Schatten der Ewigen" soll die Leser in eine faszinierende Welt entführen, in der das Unmögliche möglich wird. Es bietet Unterhaltung, Spannung und lässt die Leser über die Macht des Schicksals und die Bedeutung von Mut und Freundschaft nachdenken.

3. Verwendung der mystischen Tonalität:
Die mystische Tonalität wird durch eine reiche Sprache, poetische Beschreibungen und eine Atmosphäre des Geheimnisvollen und Unerklärlichen erreicht. Elemente wie verborgene Prophezeiungen, uralte Rituale und mysteriöse Wesen tragen dazu bei, eine Welt zu erschaffen, die die Fantasie der Leser beflügelt und sie in ihren Bann zieht.

4. Grobes Inhaltsverzeichnis:
I. Das Erwachen der Prophezeiung

Einführung in die Welt von Lyra
Die Enthüllung ihrer Bestimmung
II. Die Prüfung der Magie

Lyras Reise zu den uralten Stätten der Macht
Konfrontation mit dunklen Kräften
III. Das Schicksal der Ewigen

Die finale Schlacht um das Gleichgewicht der Welt
Der Triumph des Lichts über die Dunkelheit
"""
        return rsp
