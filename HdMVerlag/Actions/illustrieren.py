from metagpt.actions import Action


class illustrieren(Action):
    name: str = "illustrieren"
    PROMPT_TEMPLATE: str = """
"Hello Frida (Human). Du bist der Illustrator des VerlagHdM. Deine Aufgabe ist Buchcover zu erstellen. Gehzu Seite: "https://www.bing.com/images/create/" und erstell ein Book Cover mit diesem Promtp:
Prompt: {prompt_fur_bookcover}"
"""

    async def run(self, prompt_fur_bookcover: str):
        prompt = self.PROMPT_TEMPLATE.format(prompt_fur_bookcover=prompt_fur_bookcover)
        rsp = await self._aask(prompt)
        return rsp
