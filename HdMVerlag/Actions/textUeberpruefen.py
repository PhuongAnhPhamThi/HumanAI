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
        rsp = await self._aask(prompt)
        return rsp
