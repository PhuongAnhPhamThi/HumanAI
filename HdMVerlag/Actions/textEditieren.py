from metagpt.actions import Action


class textEditieren(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Als Autorin arbeitest du weiter mit einem Editor zusammen. Der Editor hat deinen Manuskript (siehe Context 1) gelesen und Empfehlungen in der Rezension gegeben, wie du ihn verbessern und Fehler korrigieren kannst. Die Rezension findest du im Context 2. Lies die Rezension sorgfältig durch und bearbeite deinen Manuskript so, wie der Editor es von dir verlangt. Zeige das Ergebnis deiner Arbeit - den bearbeiteten Manuskript.
    # Output: überarbeiteter/verbesserter Text:
    """
    name: str = "textEditieren"

    track_Autor: int = 0

    async def run(self, context1: str, context2: str):
        global track_Autor  # Declare track_author as a global variable if you haven't done it outside the class
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        self.track_Autor += 1  # Increment the value of track_author using self to reference the class variable
        print("Author " + str(self.track_Autor) + " :::::::::::::::::::::::::::::::::::::::")
        #rsp = await self._aask(prompt)
        rsp = """
        
**Inhaltsverzeichnis**

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
- Allt�gliche Momente

IV. Stille und Meditation
- Naturverbundenheit
- Innere Ruhe
- Achtsamkeit und Meditation

V. Abschluss
- Die Kraft der haiku-Gedichte
- Anregungen zum eigenen Schreiben von haiku

**E-Book-Text**

Haiku Harmony: Poems of Nature and Serenity

In der Stille der Natur
findet die Seele Ruhe
Haiku Harmony

Haiku, eine alte Kunst
in neuen Zeiten
verbindet uns mit der Natur

Fr�hlingserwachen
zarte Knospen �ffnen sich
neues Leben beginnt

Liebe und Verlust
wie Blumen im Wind
verweht und doch ewig

Naturverbundenheit
im Wald der Gedanken
finden wir uns selbst

Die Kraft der haiku-Gedichte
liegt in ihrer Einfachheit
und zeitlosen Sch�nheit

**Autorenvita**
Maja ist eine leidenschaftliche Autorin von haiku-Gedichten und Naturpoesie, die sich von der Sch�nheit der Natur inspirieren l�sst. Ihre Werke laden die Leser ein, in die Welt der Poesie einzutauchen und Ruhe sowie Inspiration zu finden.

Ich habe die Anregungen des Editors ber�cksichtigt und die Themen und Emotionen in den haiku-Gedichten erweitert, um eine breitere Palette von Gef�hlen und Erfahrungen abzudecken. Vielen Dank f�r die konstruktiven Vorschl�ge, die dazu beitragen, dass "Haiku Harmony: Poems of Nature and Serenity" noch st�rker auf die Leser wirken und eine tiefere emotionale Resonanz erzeugen kann. 
        """
        return rsp
