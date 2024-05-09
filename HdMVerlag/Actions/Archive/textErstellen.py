from metagpt.actions import Action


class textErstellen(Action):

    PROMPT_TEMPLATE: str = """
    #Context:{context}
    #Du bist eine bekannte und erfahrene Autorin von Büchern zu dem Thema {genre} und in Form von {gattung}. Du arbeitest zusammen mit einem Verlagseditor an einem E-Book. Schreibe ein hochwertiges und vollständiges Manuskript des Buches gemäß der Aufgabenstellung, die der Editor für dich vorbereitet hat. Die Aufgabenstellung findest du im Context. Beachte alle Anforderungen des Editors. Dein Manuskript muss aus folgenden Teilen bestehen: Titel, Inhaltsverzeichnis, E-Book-Text. Zusätzlich dazu verfasse einen kurzen Text über dich selbst - die Autorenvita -, um sich dem potenziellen Leser des Buches vorzustellen. Vergiss nicht, deinen Namen ausdenken und anzugeben. Deine Autorenvita darf nicht länger als 200 Zeichen sein
    # Output: vollständige Manuskript:
    """
    name: str = "textErstellen"

    async def run(self, context: str, genre: str, gattung: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context, genre=genre, gattung=gattung)
        #rsp = await self._aask(prompt)
        rsp = """
        Als erfahrene Autorin von haiku-Gedichten und Naturpoesie freue ich mich, Ihnen mein neues Buch "Haiku Harmony: Poems of Nature and Serenity" vorzustellen. Dieses Buch ist eine Sammlung von haiku-Gedichten, die die Sch�nheit der Natur und die menschliche Erfahrung einfangen, um Ruhe und Inspiration zu vermitteln.

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

Ich hoffe, dass "Haiku Harmony: Poems of Nature and Serenity" die Leser dazu inspiriert, die Sch�nheit der Natur zu sch�tzen und Momente der Ruhe und Besinnung zu finden. 
"""
        return rsp
