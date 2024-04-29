from metagpt.actions import Action


class textUeberpruefen(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1: {context1}
    #Context 2: {context2}
    #Du bist Editor in einem Verlag und arbeitest an einem E-Book zum Thema {genre} und in Form von {gattung}. Zuvor hast du eine Aufgabenstellung für eine Autorin erstellt und nun hast du ihr Manuskript zur Überprüfung erhalten. Du musst das Manuskript lesen und dir Notizen machen, damit du auf dieser Grundlage eine Rezension verfassen kannst. Das Manuskript findest du im Context 1.

Lese zunächst den Text und überprüfe, ob er mit deiner Aufgabenstellung übereinstimmt (benutze Context 2). Wenn dies nicht der Fall ist, schreibe genau auf, worin die Diskrepanz besteht. Mach dir Notizen für diesen Schritt und alle folgenden Schritte.

In einem zweiten Schritt beurteile die Qualität des Textes selbst. Wenn du Probleme findest, schreibe sie auf.

In einem dritten Schritt bewerte die Spannungskurve des Textes. Wenn du Probleme findest, schreibe sie auf.

    # Output: 
    Notizen zum Manuskript:
    """
    name: str = "textUeberpruefen"

    async def run(self, context1: str, context2: str, genre: str, gattung: str):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2, genre=genre, gattung=gattung)
        #rsp = await self._aask(prompt)
        rsp = """
        - Das Manuskript entspricht weitgehend der Aufgabenstellung und der Gliederung, die ich der Autorin gegeben habe. Es behandelt die Kunst des haiku, die Jahreszeiten, die menschliche Erfahrung, Stille und Meditation sowie die Kraft der haiku-Gedichte.
- Der Schreibstil ist pr�gnant und einf�hlsam, was der Zielsetzung des Buches entspricht, die Leser zu ber�hren und zu inspirieren.
- Die haiku-Gedichte sind gut strukturiert und fangen die Sch�nheit der Natur sowie die menschliche Erfahrung ein.

Qualit�t des Textes:
- Die haiku-Gedichte sind gut geschrieben und vermitteln die gew�nschte Ruhe und Inspiration.
- Der Text ist gut strukturiert und leicht verst�ndlich.

Spannungskurve des Textes:
- Die haiku-Gedichte erzeugen eine ruhige und meditative Atmosph�re, die die Leser in die Welt der Natur und der menschlichen Erfahrung eintauchen l�sst.
- Die Gedichte k�nnten jedoch noch etwas mehr Vielfalt in Bezug auf Emotionen und Themen bieten, um die Leser noch st�rker zu ber�hren. 
"""
        return rsp
