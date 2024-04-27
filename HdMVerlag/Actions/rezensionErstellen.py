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
        rsp = await self._aask(prompt)
        return rsp
