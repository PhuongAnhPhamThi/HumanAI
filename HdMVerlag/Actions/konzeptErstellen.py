from metagpt.actions import Action


class konzeptErstellen(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Erstelle auf der Grundlage deiner Notizen im Context eine detaillierte Anleitung für die Autorin oder den Autor, wie sie dieses Buch schreiben soll. Wiederhole in der Anleitung zusätzlich deine Ausarbeitungen wie z.B.: Arbeitstitel, ausführliche Beschreibung der Zielgruppe, Gliederung, Inhaltsverzeichnis, Tonalität.
# Output: Aufgabenstellung für Autorin:
    """

    name: str = "konzeptErstellen"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        #rsp = await self._aask(prompt)
        rsp = """
        Liebe Autorin,

ich freue mich, dass Sie sich dazu entschieden haben, das Buch "Haiku Harmony: Poems of Nature and Serenity" zu schreiben. Basierend auf Ihrem Konzept und den ausgearbeiteten Details, m�chte ich Ihnen eine detaillierte Anleitung f�r die Erstellung dieses Buches geben.

Arbeitstitel:
"Haiku Harmony: Poems of Nature and Serenity"

Zielgruppe:
Ihre Zielgruppe sind Liebhaber der Natur und Menschen, die nach Ruhe und Inspiration suchen. Das Buch soll Leser aller Altersgruppen ansprechen und eine zeitlose Thematik aufgreifen, die die Sch�nheit der Natur und die menschliche Erfahrung einf�ngt, um sie zu beruhigen und zu inspirieren.

Tonalit�t des Buches:
Die Tonalit�t sollte ruhig, meditativ und inspirierend sein, um die Leser zu beruhigen und sie mit der Sch�nheit der Natur in Einklang zu bringen.

Gliederung des Buches:
1. Einf�hrung: Die Kunst des haiku
   - Was ist haiku?
   - Die Geschichte des haiku
   - Die Bedeutung von haiku in der heutigen Zeit

2. Jahreszeiten: Gedichte �ber Natur und Jahreszeiten
   - Fr�hlingserwachen
   - Sommerhitze
   - Herbstmelancholie
   - Winterstille

3. Menschliche Erfahrung: Gedichte �ber Emotionen und menschliche Beziehungen
   - Liebe und Verlust
   - Freude und Trauer
   - Hoffnung und Sehnsucht

4. Stille und Meditation: Gedichte, die zur Ruhe und Besinnung einladen
   - Naturverbundenheit
   - Innere Ruhe
   - Achtsamkeit und Meditation

5. Abschluss: Die Kraft der haiku-Gedichte
   - Die Kraft der haiku-Gedichte
   - Anregungen zum eigenen Schreiben von haiku

Grobes Inhaltsverzeichnis:
I. Einf�hrung
II. Jahreszeiten
III. Menschliche Erfahrung
IV. Stille und Meditation
V. Abschluss

Schreibstil:
Ihr Schreibstil sollte die Sch�nheit der Natur und die Ruhe, die sie vermittelt, widerspiegeln. Die haiku-Gedichte sollten pr�gnant und einf�hlsam sein, um die Leser zu ber�hren und zu inspirieren.

Ich bin �berzeugt, dass Ihr Buch "Haiku Harmony: Poems of Nature and Serenity" eine wunderbare Sammlung von haiku-Gedichten sein wird, die die Leser in die Welt der Natur und der menschlichen Erfahrung eintauchen l�sst. Ich freue mich darauf, Ihr Buch zu lesen und bin sicher, dass es viele Menschen inspirieren wird.

Mit freundlichen Gr��en,
Bob 
        """
        return rsp
