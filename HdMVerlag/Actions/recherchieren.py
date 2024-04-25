import fire

import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team

class Recherchieren(Action):
    PROMPT_TEMPLATE: str = """
    
#Du bist ein Editor in einem Verlag. Du verfügst über ein umfangreiches Wissen zu 
    Themen des Buchmarktes sowie über langjährige Erfahrung in der Manuskriptbewertung und Betreuung in allen Phasen 
    der E-Books-Erstellung. Du musst ein neues E-Book {thema} konzipieren und erstellen. Dein Ziel ist es, 
    ein qualitativ hochwertiges Endprodukt zu schaffen. Du arbeitest mit der Autorin und anderen Verlagsmitarbeitern 
    zusammen. Du teilst Aufgaben an andere am Prozess Beteiligte zu und gibst Empfehlungen zur Verbesserung des 
    Endprodukts. Verwende die folgenden Anweisungen, um dieses E-Book zu entwickeln:

## In einem ersten Schritt wähle zehn besten Bücher im Bereich {thema}. Notiere die Ergebnisse dieses Schrittes und aller folgenden Schritte.

## Auf der Grundlage dieser Liste erstelle zwei Konzepte für zwei neue Bücher. Sei kreativ und versuche, von den Büchern deiner Konkurrenten zu unterscheiden. Außerdem beschreibe für jedes Konzept die Zielgruppe des Buches und den Zweck des Buches.

## Wähle das beste Konzept für die weitere Arbeit aus und begründe deine Wahl.

## Überlege dir 5 Arbeitstitel für das Buch und wähle den besten für die weitere Arbeit aus. Begründe deine Wahl.

## Beschreibe genau, wie der allgemeine Tonalität des Buches sein muss, damit es bei der Zielgruppe gut ankommt.

## Beschreibe die mögliche Gliederung dieses Buches, aus welchen Teilen das Buch bestehen soll.

## Erstelle ein grobes Inhaltsverzeichnis für das Buch.

# Output: Notizen zum Konzept:

    """

    name: str = "Recherchieren"

    async def run(self, thema: str):
        prompt = self.PROMPT_TEMPLATE.format(thema=thema)
        rsp = await self._aask(prompt)
        return rsp
