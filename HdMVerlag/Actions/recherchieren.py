from metagpt.actions import Action


class Recherchieren(Action):
    PROMPT_TEMPLATE: str = """
# Du bist ein Editor in einem Verlag. Du verfügst über ein umfangreiches Wissen zu Themen des Buchmarktes sowie über langjährige Erfahrung in der Manuskriptbewertung und Betreuung in allen Phasen der E-Books-Erstellung. Du musst ein neues {genre} E-Book konzipieren und erstellen. Das E-Book sollte in Form von {gattung} geschrieben sein. Dein Ziel ist es, ein qualitativ hochwertiges Endprodukt zu schaffen. Du arbeitest mit der Autorin und anderen Verlagsmitarbeitern zusammen. Du teilst Aufgaben an andere am Prozess Beteiligte zu und gibst Empfehlungen zur Verbesserung des Endprodukts.

Verwende die folgenden Anweisungen, um dieses E-Book zu entwickeln.

In einem ersten Schritt wähle zehn besten Bücher im Bereich {genre} und in Form von {gattung}. Notiere die Ergebnisse dieses Schrittes und aller folgenden Schritte.

Auf der Grundlage dieser Liste erstelle zwei Konzepte für zwei neue Bücher. Sei kreativ und versuche, von den Büchern deiner Konkurrenten zu unterscheiden. Außerdem beschreibe für jedes Konzept die Zielgruppe des Buches und den Zweck des Buches.

Wähle das beste Konzept für die weitere Arbeit aus und begründe deine Wahl.

Überlege dir 5 Arbeitstitel für das Buch und wähle den besten für die weitere Arbeit aus. Begründe deine Wahl.

Beschreibe genau, wie der allgemeine Tonalität des Buches sein muss, damit es bei der Zielgruppe gut ankommt.

Beschreibe die mögliche Gliederung dieses Buches, aus welchen Teilen das Buch bestehen soll.

Erstelle ein grobes Inhaltsverzeichnis für das Buch.
# Output: Notizen zum Konzept:

    """

    name: str = "Recherchieren"

    async def run(self, genre: str, gattung: str):
        prompt = self.PROMPT_TEMPLATE.format(genre=genre, gattung=gattung)
        #rsp = await self._aask(prompt)
        rsp = """
        Schritt 1: Auswahl der besten haiku-B�cher in Gedichtform:
1. "The Essential Haiku: Versions of Basho, Buson, & Issa" von Robert Hass
2. "The Haiku Anthology" von Cor van den Heuvel
3. "Haiku Mind: 108 Poems to Cultivate Awareness and Open Your Heart" von Patricia Donegan
4. "The Classic Tradition of Haiku: An Anthology" von Faubion Bowers
5. "Haiku: An Anthology of Japanese Poems" von Stephen Addiss
6. "Haiku: This Other World" von Richard Wright
7. "The Haiku Handbook: How to Write, Share, and Teach Haiku" von William J. Higginson
8. "Haiku: The Last Poems of an American Icon" von Richard Wright
9. "The Haiku Seasons: Poetry of the Natural World" von William J. Higginson
10. "Haiku: A Poet's Guide" von Lee Gurga

Schritt 2: Erstellung von zwei Konzepten f�r neue B�cher:
Konzept 1: "Haiku Harmony"
- Zielgruppe: Liebhaber der Natur, Menschen, die nach Ruhe und Inspiration suchen
- Zweck: Eine Sammlung von haiku-Gedichten, die die Sch�nheit der Natur und die menschliche Erfahrung einfangen, um Leser zu beruhigen und zu inspirieren.

Konzept 2: "Urban Haiku"
- Zielgruppe: Stadtbewohner, junge Erwachsene, die sich mit dem st�dtischen Leben identifizieren
- Zweck: Eine moderne Interpretation von haiku-Gedichten, die das st�dtische Leben, die Hektik und die Emotionen der Gro�stadt einfangen, um eine Verbindung zu urbanen Lesern herzustellen.

Begr�ndung der Wahl: Das Konzept "Haiku Harmony" wurde ausgew�hlt, da es eine breitere Zielgruppe anspricht und eine zeitlose Thematik aufgreift, die Leser aller Altersgruppen anspricht.

Arbeitstitel: "Haiku Harmony: Poems of Nature and Serenity"
Begr�ndung: Der Titel vermittelt die zentrale Botschaft des Buches, die Natur und Ruhe in Form von haiku-Gedichten zu pr�sentieren.

Tonalit�t des Buches: Die Tonalit�t sollte ruhig, meditativ und inspirierend sein, um die Leser zu beruhigen und sie mit der Sch�nheit der Natur in Einklang zu bringen.

Gliederung des Buches:
1. Einf�hrung: Die Kunst des haiku
2. Jahreszeiten: Gedichte �ber Natur und Jahreszeiten
3. Menschliche Erfahrung: Gedichte �ber Emotionen und menschliche Beziehungen
4. Stille und Meditation: Gedichte, die zur Ruhe und Besinnung einladen
5. Abschluss: Die Kraft der haiku-Gedichte

Grobes Inhaltsverzeichnis:
I. Einf�hrung
- Was ist haiku?
- Die Geschichte des haiku
- Die Bedeutung von haiku in der heutigen Zeit

II. Jahreszeiten
- Fr�hlingserwachen
- Sommerhitze
- Herbstmelancholie
- Winterstille

III. Menschliche Erfahrung
- Liebe und Verlust
- Freude und Trauer
- Hoffnung und Sehnsucht

IV. Stille und Meditation
- Naturverbundenheit
- Innere Ruhe
- Achtsamkeit und Meditation

V. Abschluss
- Die Kraft der haiku-Gedichte
- Anregungen zum eigenen Schreiben von haiku 
"""
        return rsp
