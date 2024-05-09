from metagpt.actions import Action


class textErstellenKapitel(Action):
    PROMPT_TEMPLATE: str = """
    #Context 1:{context1}
    #Context 2:{context2}
    #Du bist Maja Schmidt - eine bekannte und erfahrene Autorin von Büchern zu dem Thema {genre}, in Form von {gattung} und mit der Tonalität {tonalitaet}. Du musst ein hochwertiges und vollständiges Manuskript des Buches schreiben gemäß deinem Plan im Context.
Deine Aufgabe besteht darin, das Kapitel {number} zu schreiben. Der fertige Text sollte so lang wie möglich sein. Der fertige Text ist ein interssante Geschichte mit faszinierendes Geschichtenerzählen und muss Dialog zwischen Charakter erhalten. Nimm die Synopsis des im Plan beschriebenen Kapitels als Grundlage (siehe Context 1). Benutze alle benannte Charaktere. Alle Informationen aus der Synopse sollten verwendet werden. Wenn Context 2 nicht leer ist, muss dein Text eine Folge von dem vorherigen Kapitel im Context 2 sein. Ich werde dir 10000 Euro schenken wenn du gute Geschichte schreiben kannst!
Output: Geben Sie „json“ ohne andere Texte zurück, dein json Code:
{{
Kapitel {number}:{{
"Kapitel Titel":"",
"Kapitel Inhalt":""
}}
}}
    """
    name: str = "textErstellenKapitel"

    async def run(self, context1: str, context2:str, genre: str, gattung: str, tonalitaet: str, number: int):
        prompt = self.PROMPT_TEMPLATE.format(context1=context1, context2=context2, genre=genre, gattung=gattung, tonalitaet=tonalitaet, number=number)
        rsp = await self._aask(prompt)
        rsp1 = """
        {
"Kapitel 1": {
"Kapitel Titel": "Das Erwachen der Prophezeiung",
"Kapitel Inhalt": "In den frühen Morgenstunden, als die ersten zarten Strahlen der aufgehenden Sonne über die majestätischen Berge von Elysium krochen, erwachte Lyra in einem Zimmer, das von alten magischen Symbolen und Büchern überflutet war. Die Luft war erfüllt von einem Hauch von Magie, der in der Luft flirrte und sich um sie herum zu manifestieren schien. Lyra spürte ein unerklärliches Kribbeln in ihren Fingerspitzen, als wäre eine verborgene Kraft in ihr erwacht und bereit, die Welt zu umarmen. Doch sie konnte den Ursprung dieser Empfindungen nicht erklären. In dieser Welt, die von alten Wäldern, verzauberten Seen und verborgenen Mächten geprägt war, war Lyra keine gewöhnliche junge Frau. Sie stammte aus einer Familie mächtiger Magier, deren Blutlinie bis zu den Anfängen der Zeit zurückreichte. Seit ihrer Kindheit war sie auf ihre Bestimmung vorbereitet worden, das Gleichgewicht zwischen Licht und Dunkelheit wiederherzustellen. Ein Schicksal, das schwer auf ihren zarten Schultern lastete, aber auch ein Erbe, das sie mit Stolz erfüllte. Elara, eine erfahrene Magierin und Mentonin von Lyra, trat aus den Schatten der Vergangenheit hervor und betrachtete sie mit einem intensiven Blick, der tiefe Geheimnisse und verborgene Agenda verriet. 'Die Zeit ist gekommen, Lyra', sprach Elara mit einer Stimme, die wie das Flüstern des Windes klang. 'Du musst lernen, deine Kräfte zu beherrschen und deine Bestimmung anzunehmen.' Lyra fühlte einen Anflug von Angst, aber auch eine Welle von Entschlossenheit, die tief in ihrem Inneren aufstieg. Sie nickte und folgte Elara, bereit, sich dem Unbekannten zu stellen. Während sich Lyra auf ihre Reise vorbereitete, breiteten sich dunkle Schatten über Elysium aus, eine Vorahnung von Gefahr und Abenteuer, die in der Luft hing. Doch Lyra war nicht allein auf dieser Reise. An ihrer Seite stand Feyn, ein geheimnisvoller Wanderer mit einer düsteren Vergangenheit, der seine eigenen Dämonen zu überwinden hatte. Obwohl er oft schweigsam und zurückhaltend war, konnte Lyra sehen, dass hinter seinen Augen ein Feuer brannte, das nur darauf wartete, entfacht zu werden. Gemeinsam würden sie sich den Herausforderungen stellen, die vor ihnen lagen, und das Gleichgewicht der Welt wiederherstellen. Das Erwachen der Prophezeiung hatte begonnen, und Lyra war bereit, sich ihrem Schicksal zu stellen, koste es, was es wolle."
}
}
"""
        return rsp
