from metagpt.actions import Action


class metadatenZusammenfassen(Action):
    PROMPT_TEMPLATE: str = """
# Context : {context}
# Um mit dem Layout-Design fortzufahren, musst du als Editor die Metadaten des E-Books zusammenfassen. Verwende Context und liste die Metadaten des zukünftigen E-Books in der folgenden Reihenfolge auf:

1. Name des Buches (benutze Context)
2. Name des Autors (benutze Context)
3. Name des Herausgebers (benutze Name: Mark Zimmermann)
4. der Name des Verlags (benutze Name: HdM AI Technologies),
5. Adresse des Verlags (benutze Adresse: Nobelstraße 10, 70569 Stuttgart),
6. Datum der Veröffentlichung (benutze heutiges Datum)

Alle obengenannte Elemente müssen vorhanden sein.

# Output: Geben Sie „json“ ohne andere Texte zurück. dein json Code:
{{
 "Name des Buches": "",
 "Name des Autors":"",
 "Name des Herausgebers":"",
 "Name des Verlags": "",
 "Adresse des Verlags",
 "Datum der Veröffentlichung": "",
 }}

    """

    name: str = "metadatenZusammenfassen"

    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        rsp1 = ""
        return rsp
