from metagpt.actions import Action


class buchZusammenfassen(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: {context1}
# Um mit dem Layout-Design fortzufahren, musst du als Editor alle Elemente des E-Books in einem einzigen Dokument zusammenfassen. Verwende Context 1 und Context 2 und kombiniere alle Elemente des zukünftigen E-Books in der folgenden Reihenfolge:

1. die Autorenvita (benutze Context 1)
2. das Inhaltsverzeichnis (benutze Context 2, aber nehme nur die Kapitelüberschriften, ohne Erklärung.)
3. der Text des Manuskripts (benutze Context 1, nehme die Titeln der Kapiteln und ALLE Texte. Du darf die Texten nicht verkürzen oder verpassen)
4. der Name des Buches (benutze Context 2)
5 Name des Autors (benutze Context 1)
6 Name des Herausgebers (benutze Name: Mark Zimmermann)
7. der Name des Verlags (benutze Name: HdM AI Technologies),
8. Adresse des Verlags (benutze Adresse: Nobelstraße 10, 70569 Stuttgart),
9. Datum der Veröffentlichung (benutze heutiges Datum)

Alle obengenannte Elemente müssen vorhanden sein.
# Output: Buch zusammengefasst:
    """

    name: str = "buchZusammenfassen"

    async def run(self, context1: str, context2: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        #rsp = await self._aask(prompt)
        rsp = """
        
**Autorenvita**
Maja ist eine leidenschaftliche Autorin von haiku-Gedichten und Naturpoesie, die sich von der Sch�nheit der Natur inspirieren l�sst. Ihre Werke laden die Leser ein, in die Welt der Poesie einzutauchen und Ruhe sowie Inspiration zu finden.

**Inhaltsverzeichnis**
- Haiku Harmony: Poems of Nature and Serenity
- Autorenvita
- Haiku, eine alte Kunst
- Fr�hlingserwachen
- Liebe und Verlust
- Naturverbundenheit
- Die Kraft der haiku-Gedichte

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

**Name des Buches**
Haiku Harmony: Poems of Nature and Serenity

**Name des Autors**
Maja

**Name des Herausgebers**
Mark Zimmermann

**Name des Verlags**
HdM AI Technologies

**Adresse des Verlags**
Nobelstra�e 10, 70569 Stuttgart

**Datum der Ver�ffentlichung**
[Heutiges Datum] 

        """
        return rsp
