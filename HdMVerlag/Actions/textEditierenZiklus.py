from metagpt.actions import Action

track_Autor: int = 0


class textEditierenZiklus(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Du bist eine Autorin, die bzw. der bereits von einem Editor eine Rezension deines Manuskripts erhalten hat und das Buch entsprechend den Empfehlungen des Editors überarbeitet hat. Du hast das überarbeitete Manuskript erneut eingesandt (siehe Context 2) und eine Antwort des Editors erhalten (siehe Context 1). Wenn Editor zufriedend mit deiner Manuskript ist und keine Verbesserungsidee vorschlagt, musst du nichts weiteres machen, gebe im # Output nur deine letztes Manuskript (siehe Context 2) zurück. Wenn die Antwort weitere Punkte zur Verbesserung deines Manuskripts enthält, nimm die Korrekturen vor und zeige das überarbeitete Manuskript
    # Output: letzter Text/neu überarbeiteter Text:
    """
    name: str = "textEditierenZiklus"

    async def run(self, context1: str, context2: str):
        global track_Autor  # Declare track_author as a global variable if you haven't done it outside the class
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        track_Autor += 1  # Increment the value of track_author using self to reference the class variable
        print("Author " + str(track_Autor) + " :::::::::::::::::::::::::::::::::::::::")
        #rsp = await self._aask(prompt)
        rsp = """
        
Vielen Dank f�r die konstruktiven Vorschl�ge. Ich habe die Anregungen des Editors ber�cksichtigt und die Themen und Emotionen in den haiku-Gedichten erweitert, um eine breitere Palette von Gef�hlen und Erfahrungen abzudecken. Hier ist das �berarbeitete Manuskript:

**Haiku Harmony: Poems of Nature and Serenity**

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

        """
        return rsp
