from metagpt.actions import Action


class rezensionErstellen(Action):

    PROMPT_TEMPLATE: str = """
    # Context 1:{context1}
    # Context 2:{context2}
    # Jetzt musst du eine Rezension zu dem Manuskript (siehe Context 2) schreiben. Eine Rezension ist eine Übersicht über die Fehler, die du im Manuskript früher gefunden hast, und eine Liste von konkreten Empfehlungen zur Verbesserung des Buches für die Autorin. Auf der Grundlage deiner Notizen schreibe eine Rezension. Die Notizen  findest du im Context 1.
    # Output: Rezension:
    """
    name: str = "rezensionErstellen"

    async def run(self, context1: str, context2: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2)
        #rsp = await self._aask(prompt)
        rsp = """
        Liebe Maja,

ich habe mit gro�em Interesse Ihr neues Buch "Haiku Harmony: Poems of Nature and Serenity" gelesen und m�chte Ihnen meine Eindr�cke mitteilen.

Zun�chst einmal m�chte ich betonen, dass Ihr Manuskript weitgehend der Aufgabenstellung und Gliederung entspricht, die Sie erhalten haben. Die Kunst des haiku, die Jahreszeiten, die menschliche Erfahrung, Stille und Meditation sowie die Kraft der haiku-Gedichte werden einf�hlsam behandelt. Der Schreibstil ist pr�gnant und passt gut zur Zielsetzung des Buches, die Leser zu ber�hren und zu inspirieren.

Die haiku-Gedichte sind gut strukturiert und fangen die Sch�nheit der Natur sowie die menschliche Erfahrung ein. Sie vermitteln die gew�nschte Ruhe und Inspiration und erzeugen eine ruhige und meditative Atmosph�re, die die Leser in die Welt der Natur und der menschlichen Erfahrung eintauchen l�sst.

Allerdings habe ich auch einige Anregungen zur Verbesserung. Die haiku-Gedichte k�nnten noch etwas mehr Vielfalt in Bezug auf Emotionen und Themen bieten, um die Leser noch st�rker zu ber�hren. Vielleicht k�nnten Sie die Auswahl der Themen und Emotionen in den Gedichten �berdenken, um eine breitere Palette von Gef�hlen und Erfahrungen abzudecken.

Insgesamt ist "Haiku Harmony: Poems of Nature and Serenity" eine gelungene Sammlung von haiku-Gedichten, die die Sch�nheit der Natur und die menschliche Erfahrung einfangen. Mit einigen Anpassungen k�nnte das Buch jedoch noch st�rker auf die Leser wirken und eine noch tiefere emotionale Resonanz erzeugen.

Ich hoffe, dass meine Anregungen Ihnen bei der weiteren Gestaltung des Buches hilfreich sind und freue mich darauf, Ihre �berarbeitete Version zu lesen.

Mit freundlichen Gr��en,
Bob 
        """
        return rsp
