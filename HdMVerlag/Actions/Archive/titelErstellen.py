from metagpt.actions import Action


class titelErstellen(Action):
    PROMPT_TEMPLATE: str = """
# Context: {context}
# Überlege dir 5 geeignete Arbeitstitel für das Buch, basierend auf Konzept von Context und liste sie aus.
# Output: Geben Sie „json“ ohne andere Texte zurück. dein json Code:
```
{{
"1":"dein 1.Titel",
"2":"dein 2.Titel",
"3":"dein 3.Titel",
...
}}
```
"""

    name: str = "titelErstellen"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        rsp1 = """
        {
  "1": "Schatten der Ewigen",
  "2": "Das Vermächtnis der Magie",
  "3": "Im Bann der Prophezeiung",
  "4": "Die Pfade des Lichts und der Dunkelheit",
  "5": "Das Erwachen der Mystik"
}

"""
        return rsp
