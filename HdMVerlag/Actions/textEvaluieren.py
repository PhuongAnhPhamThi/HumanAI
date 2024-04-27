from metagpt.actions import Action


class textEvaluieren(Action):
    PROMPT_TEMPLATE_ANH: str = """
    1. Role: You are an editor of a children book. Your task is to review the author's content and give feedback to improve the content. 
    2. Context: {context}
    3. Requirements for good content: 
    - The story must have a funny dialogue between the characters. 
    - The name of the main character must be Tommy. 
    4. Instruction: You get the last content from the author in 2. Context. You read and evaluate the content according to 3. requirements for good content.
    - If the content need to be improved, return a list of things to improve.  DON'T REPEAT YOUR PREVIOUS MESSAGE.
    - Else if no improvement ist required, reply ONLY the keyword "LGTM" and STOP. JUST REPLY "LGTM".
    """

    PROMPT_TEMPLATE_2: str = """
    1. Rolle: Sie sind ein Redakteur eines Buches. Ihre Aufgabe ist es, den Inhalt des Autors zu überprüfen und Feedback zu geben, um den Inhalt zu verbessern. 
    2. Der Kontext: {context}
    4. Anweisung: Sie erhalten den letzten Inhalt vom Autor (Maja) in 2. Context. Du liest und bewertest den Inhalt.
    - Wenn der Inhalt verbessert werden muss, gib eine Liste von Dingen zurück, die verbessert werden sollten.  WIEDERHOLEN SIE NICHT IHRE VORHERIGE NACHRICHT.
    - Wenn keine Verbesserung erforderlich ist, antworten Sie NUR mit dem Stichwort "LGTM" und STOP. ANTWORTEN SIE NUR "LGTM".
    """

    name: str = "Evaluieren"
    track_Evaluieren_round: int = 0

    async def run(self, context: str):
        self.track_Evaluieren_round += 1
        if self.track_Evaluieren_round <= 1:
            prompt = self.PROMPT_TEMPLATE_2.format(context=context)
            print("Editor " + str(self.track_Evaluieren_round) + " :::::::::::::::::::::::::::::::::::::::")
            rsp = await self._aask(prompt)
            return rsp
        else:
            return "Die Manuskript kann man nutzen"

