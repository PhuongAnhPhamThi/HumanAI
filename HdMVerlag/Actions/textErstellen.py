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
        rsp = await self._aask(prompt)
        return rsp
