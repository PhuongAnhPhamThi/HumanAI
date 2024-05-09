from metagpt.actions import Action


class layoutKonzipieren(Action):
    PROMPT_TEMPLATE: str = """
# Context 1: {context1}
# Context 2: {context2}
# Context 3: {context3}
# Du bist ein Editor, der gerade die endgültige Version des Ebook-Textes genehmigt hat. Auch das Cover des Ebooks ist bereits auf der Grundlage deinem Prompt gezeichnet worden (siehe Context 3). Nun solltest du alle Materialien an den Layout Designer zur weiteren Bearbeitung weitergeben. Welche Empfehlungen und Anweisungen für die weitere Arbeit kannst du dem Layout Designer auf der Grundlage des Textes des Buches (siehe Context 1) und des Konzepts des Buches (siehe Context 2) geben. Fasse diese in Form einer Liste zusammen.
# Output: Aufgabestellung für Layout Designer:
    """

    name: str = "layoutKonzipieren"

    async def run(self, context1: str, context2: str, context3: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2, context3=context3)
        #rsp = await self._aask(prompt)

        rsp= """
        
**Empfehlungen und Anweisungen f�r die weitere Arbeit:**

1. Das Buchcover sollte nat�rliche Elemente wie Blumen, B�ume, Wasser oder Landschaften enthalten, um die Sch�nheit der Natur zu betonen. Die Atmosph�re sollte harmonisch und beruhigend sein, um die Ruhe der Poesie einzufangen.

2. Betone die Einfachheit und zeitlose Sch�nheit der haiku-Gedichte, um die Leser zum Eintauchen in die Welt der Poesie und Natur zu inspirieren.

3. Verwende eine ruhige und meditative Farbpalette, die die Tonalit�t des Buches widerspiegelt und die Leser anspricht.

4. Achte darauf, dass der Titel "Haiku Harmony: Poems of Nature and Serenity" gut lesbar und ansprechend gestaltet ist, um die Aufmerksamkeit der potenziellen Leser zu gewinnen.

5. Ber�cksichtige die Zielgruppe des Buches, die Liebhaber der Natur und Menschen, die nach Ruhe und Inspiration suchen. Das Cover sollte diese Zielgruppe ansprechen und sie dazu einladen, das Buch zu entdecken.

6. Stelle sicher, dass das Cover eine zeitlose �sthetik hat, die Leser aller Altersgruppen anspricht und die zeitlose Thematik des Buches unterstreicht.

7. Das Cover sollte die Ruhe und Inspiration, die in den haiku-Gedichten zum Ausdruck kommen, visuell vermitteln und die Leser dazu einladen, in die Welt der Natur und Poesie einzutauchen.

Bitte ber�cksichtige diese Empfehlungen und Anweisungen bei der Gestaltung des Buchcovers. Falls weitere Informationen ben�tigt werden, stehe ich gerne zur Verf�gung.

Mit freundlichen Gr��en,
Bob 
        """
        return rsp
