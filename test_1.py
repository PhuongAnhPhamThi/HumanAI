from workspace.Utils.json_handle import extract_json_from_string
from workspace.Utils.text_handle import write_to_txt_file

str1 = """

json
{
  "Kapitel 1": {
    "Kapitel Titel": "Das Verschwinden",
    "Kapitel Inhalt Teil 1": "Sophie Miller saß in der hintersten Ecke des überfüllten Hörsaals und beobachtete die anderen Studenten. Ihr Blick wanderte über die Gesichter, die in die Vorlesung von Professor David Black vertieft waren. Sie konnte sich nicht konzentrieren. Etwas stimmte nicht. Seit Tagen hatte sie das Gefühl, dass etwas Unheimliches in der Luft lag. Die Universität Ravenwood war schon immer ein Ort voller Geheimnisse und Geschichten gewesen, aber in letzter Zeit schien sich die Dunkelheit zu verdichten.

Nach der Vorlesung packte Sophie ihre Sachen zusammen und machte sich auf den Weg zur Bibliothek. Auf dem Weg dorthin stieß sie mit Alex Turner zusammen, einem Journalismusstudenten, der für seine scharfsinnigen Fragen und seine unermüdliche Suche nach der Wahrheit bekannt war.

\"Hey, pass doch auf!\" rief Alex, als er seine Notizbücher aufhob, die auf den Boden gefallen waren.

\"Tut mir leid, ich war in Gedanken,\" entschuldigte sich Sophie und half ihm, die Bücher aufzusammeln. \"Ich bin Sophie, übrigens.\"

\"Alex,\" antwortete er und musterte sie neugierig. \"Du bist doch die Psychologiestudentin, die immer in der letzten Reihe sitzt, oder?\"

Sophie nickte. \"Ja, das bin ich. Hast du auch das Gefühl, dass hier etwas nicht stimmt?\"

Alex hob eine Augenbraue. \"Wie meinst du das?\"

\"Ich weiß nicht genau,\" sagte Sophie zögernd. \"Aber ich habe das Gefühl, dass etwas Unheimliches vor sich geht. Hast du von den Verschwinden gehört?\"

Alex' Gesichtsausdruck wurde ernst. \"Ja, ich habe davon gehört. Ein paar Studenten sind spurlos verschwunden. Die Polizei hat bisher keine Hinweise gefunden.\"

\"Genau das meine ich,\" sagte Sophie. \"Ich habe das Gefühl, dass wir etwas übersehen. Vielleicht sollten wir uns zusammentun und herausfinden, was hier wirklich vor sich geht.\"

Alex zögerte einen Moment, dann nickte er. \"In Ordnung. Aber wir müssen vorsichtig sein. Wenn jemand herausfindet, dass wir herumschnüffeln, könnten wir in Schwierigkeiten geraten.\"

Die beiden machten sich auf den Weg zur Bibliothek, um mehr Informationen zu sammeln. Dort trafen sie auf Emily White, eine Literaturstudentin, die für ihre Begeisterung und Loyalität bekannt war. Sie saß an einem Tisch und blätterte in einem alten Buch.

\"Emily, hast du einen Moment?\" fragte Sophie und setzte sich neben sie.

\"Natürlich, was gibt's?\" antwortete Emily und legte das Buch beiseite.

\"Wir versuchen herauszufinden, was mit den verschwundenen Studenten passiert ist,\" erklärte Alex. \"Hast du irgendetwas Ungewöhnliches bemerkt?\"

Emily dachte einen Moment nach. \"Nun, ich habe gehört, dass einige der verschwundenen Studenten kurz vor ihrem Verschwinden seltsame Nachrichten erhalten haben. Aber niemand weiß, von wem sie stammen.\"

\"Das ist ein guter Hinweis,\" sagte Sophie. \"Wir sollten versuchen, mehr über diese Nachrichten herauszufinden.\"

Die drei verbrachten den Rest des Tages damit, in alten Zeitungen und Archiven zu stöbern. Sie fanden Berichte über ähnliche Vorfälle, die vor vielen Jahren an der Universität stattgefunden hatten. Es schien, als ob die Geschichte sich wiederholte.

Als die Bibliothek schloss, beschlossen sie, ihre Ermittlungen am nächsten Tag fortzusetzen. Auf dem Weg nach draußen begegneten sie Professor David Black, der sie mit einem durchdringenden Blick musterte.

\"Guten Abend, Professor,\" sagte Sophie höflich.

\"Guten Abend, Miss Miller, Mr. Turner, Miss White,\" antwortete der Professor. \"Was führt Sie zu dieser späten Stunde in die Bibliothek?\"

\"Wir recherchieren für ein Projekt,\" antwortete Alex schnell.

Der Professor nickte langsam. \"Seien Sie vorsichtig, was Sie suchen. Manchmal ist es besser, bestimmte Dinge nicht zu wissen.\"

Mit diesen Worten drehte er sich um und ging. Sophie, Alex und Emily sahen sich an. Sie wussten, dass sie auf der richtigen Spur waren, aber sie ahnten auch, dass die Gefahr näher war, als sie gedacht hatten."
  }
}
```
Warning: model not found. Using cl100k_base encoding.
json string in Util
{
  "Kapitel 1": {
    "Kapitel Titel": "Das Verschwinden",
    "Kapitel Inhalt Teil 1": "Sophie Miller saß in der hintersten Ecke des überfüllten Hörsaals und beobachtete die anderen Studenten. Ihr Blick wanderte über die Gesichter, die in die Vorlesung von Professor David Black vertieft waren. Sie konnte sich nicht konzentrieren. Etwas stimmte nicht. Seit Tagen hatte sie das Gefühl, dass etwas Unheimliches in der Luft lag. Die Universität Ravenwood war schon immer ein Ort voller Geheimnisse und Geschichten gewesen, aber in letzter Zeit schien sich die Dunkelheit zu verdichten.

Nach der Vorlesung packte Sophie ihre Sachen zusammen und machte sich auf den Weg zur Bibliothek. Auf dem Weg dorthin stieß sie mit Alex Turner zusammen, einem Journalismusstudenten, der für seine scharfsinnigen Fragen und seine unermüdliche Suche nach der Wahrheit bekannt war.

\"Hey, pass doch auf!\" rief Alex, als er seine Notizbücher aufhob, die auf den Boden gefallen waren.

\"Tut mir leid, ich war in Gedanken,\" entschuldigte sich Sophie und half ihm, die Bücher aufzusammeln. \"Ich bin Sophie, übrigens.\"

\"Alex,\" antwortete er und musterte sie neugierig. \"Du bist doch die Psychologiestudentin, die immer in der letzten Reihe sitzt, oder?\"

Sophie nickte. \"Ja, das bin ich. Hast du auch das Gefühl, dass hier etwas nicht stimmt?\"

Alex hob eine Augenbraue. \"Wie meinst du das?\"

\"Ich weiß nicht genau,\" sagte Sophie zögernd. \"Aber ich habe das Gefühl, dass etwas Unheimliches vor sich geht. Hast du von den Verschwinden gehört?\"

Alex' Gesichtsausdruck wurde ernst. \"Ja, ich habe davon gehört. Ein paar Studenten sind spurlos verschwunden. Die Polizei hat bisher keine Hinweise gefunden.\"

\"Genau das meine ich,\" sagte Sophie. \"Ich habe das Gefühl, dass wir etwas übersehen. Vielleicht sollten wir uns zusammentun und herausfinden, was hier wirklich vor sich geht.\"

Alex zögerte einen Moment, dann nickte er. \"In Ordnung. Aber wir müssen vorsichtig sein. Wenn jemand herausfindet, dass wir herumschnüffeln, könnten wir in Schwierigkeiten geraten.\"

Die beiden machten sich auf den Weg zur Bibliothek, um mehr Informationen zu sammeln. Dort trafen sie auf Emily White, eine Literaturstudentin, die für ihre Begeisterung und Loyalität bekannt war. Sie saß an einem Tisch und blätterte in einem alten Buch.

\"Emily, hast du einen Moment?\" fragte Sophie und setzte sich neben sie.

\"Natürlich, was gibt's?\" antwortete Emily und legte das Buch beiseite.

\"Wir versuchen herauszufinden, was mit den verschwundenen Studenten passiert ist,\" erklärte Alex. \"Hast du irgendetwas Ungewöhnliches bemerkt?\"

Emily dachte einen Moment nach. \"Nun, ich habe gehört, dass einige der verschwundenen Studenten kurz vor ihrem Verschwinden seltsame Nachrichten erhalten haben. Aber niemand weiß, von wem sie stammen.\"

\"Das ist ein guter Hinweis,\" sagte Sophie. \"Wir sollten versuchen, mehr über diese Nachrichten herauszufinden.\"

Die drei verbrachten den Rest des Tages damit, in alten Zeitungen und Archiven zu stöbern. Sie fanden Berichte über ähnliche Vorfälle, die vor vielen Jahren an der Universität stattgefunden hatten. Es schien, als ob die Geschichte sich wiederholte.

Als die Bibliothek schloss, beschlossen sie, ihre Ermittlungen am nächsten Tag fortzusetzen. Auf dem Weg nach draußen begegneten sie Professor David Black, der sie mit einem durchdringenden Blick musterte.

\"Guten Abend, Professor,\" sagte Sophie höflich.

\"Guten Abend, Miss Miller, Mr. Turner, Miss White,\" antwortete der Professor. \"Was führt Sie zu dieser späten Stunde in die Bibliothek?\"

\"Wir recherchieren für ein Projekt,\" antwortete Alex schnell.

Der Professor nickte langsam. \"Seien Sie vorsichtig, was Sie suchen. Manchmal ist es besser, bestimmte Dinge nicht zu wissen.\"

Mit diesen Worten drehte er sich um und ging. Sophie, Alex und Emily sahen sich an. Sie wussten, dass sie auf der richtigen Spur waren, aber sie ahnten auch, dass die Gefahr näher war, als sie gedacht hatten."
  }
}
"""
str2 = """
{
  "Kapitel 1": {
    "Kapitel Titel": "Das Verschwinden",
    "Kapitel Inhalt Teil 1": "Sophie Miller saß in der hintersten Ecke des überfüllten Hörsaals und beobachtete die anderen Studenten. Ihr Blick wanderte über die Gesichter, die in die Vorlesung von Professor David Black vertieft waren. Sie konnte sich nicht konzentrieren. Etwas stimmte nicht. Seit Tagen hatte sie das Gefühl, dass etwas Unheimliches in der Luft lag. Die Universität Ravenwood war schon immer ein Ort voller Geheimnisse und Geschichten gewesen, aber in letzter Zeit schien sich die Dunkelheit zu verdichten.\n\nNach der Vorlesung packte Sophie ihre Sachen zusammen und machte sich auf den Weg zur Bibliothek. Auf dem Weg dorthin stieß sie mit Alex Turner zusammen, einem Journalismusstudenten, der für seine scharfsinnigen Fragen und seine unermüdliche Suche nach der Wahrheit bekannt war.\n\n\"Hey, pass doch auf!\" rief Alex, als er seine Notizbücher aufhob, die auf den Boden gefallen waren.\n\n\"Tut mir leid, ich war in Gedanken,\" entschuldigte sich Sophie und half ihm, die Bücher aufzusammeln. \"Ich bin Sophie, übrigens.\"\n\n\"Alex,\" antwortete er und musterte sie neugierig. \"Du bist doch die Psychologiestudentin, die immer in der letzten Reihe sitzt, oder?\"\n\nSophie nickte. \"Ja, das bin ich. Hast du auch das Gefühl, dass hier etwas nicht stimmt?\"\n\nAlex hob eine Augenbraue. \"Wie meinst du das?\"\n\n\"Ich weiß nicht genau,\" sagte Sophie zögernd. \"Aber ich habe das Gefühl, dass etwas Unheimliches vor sich geht. Hast du von den Verschwinden gehört?\"\n\nAlex' Gesichtsausdruck wurde ernst. \"Ja, ich habe davon gehört. Ein paar Studenten sind spurlos verschwunden. Die Polizei hat bisher keine Hinweise gefunden.\"\n\n\"Genau das meine ich,\" sagte Sophie. \"Ich habe das Gefühl, dass wir etwas übersehen. Vielleicht sollten wir uns zusammentun und herausfinden, was hier wirklich vor sich geht.\"\n\nAlex zögerte einen Moment, dann nickte er. \"In Ordnung. Aber wir müssen vorsichtig sein. Wenn jemand herausfindet, das"s wir herumschnüffeln, könnten wir in Schwierigkeiten geraten.\"\n\nDie beiden machten sich auf den Weg zur Bibliothek, um mehr Informationen zu sammeln. Dort trafen sie auf Emily White, eine Literaturstudentin, die für ihre Begeisterung und Loyalität be"kannt war. Sie saß an einem Tisch und blätterte in einem alten Buch.\n\n\"Emily, hast du einen Moment?\" fragte Sophie und setzte sich neben sie.\n\n\"Natürlich, was gibt's?\" antwortete Emily und legte das Buch beiseite.\n\n\"Wir versuchen herauszufinden, was mit den verschwundenen Studenten passiert ist,\" erklärte Alex. \"Hast du irgendetwas Ungewöhnliches bemerkt?\"\n\nEmily dachte einen Moment nach. \"Nun, ich habe gehört, dass einige der verschwundenen Studenten kurz vor ihrem Verschwinden seltsame Nachrichten erhalten haben. Aber niemand weiß, von wem sie stammen.\"\n\n\"Das ist ein guter Hinweis,\" sagte Sophie. \"Wir sollten versuchen, mehr über diese Nachrichten herauszufinden.\"\n\nDie drei verbrachten den Rest des Tages damit, in alten Zeitungen und Archiven zu stöbern. Sie fanden Berichte über ähnliche Vorfälle, die vor vielen Jahren an der Universität stattgefunden hatten. Es schien, als ob die Geschichte sich wiederholte.\n\nAls die Bibliothek schloss, beschlossen sie, ihre Ermittlungen am nächsten Tag fortzusetzen. Auf dem Weg nach draußen begegneten sie Professor David Black, der sie mit einem durchdringenden Blick musterte.\n\n\"Guten Abend, Professor,\" sagte Sophie höflich.\n\n\"Guten Abend, Miss Miller, Mr. Turner, Miss White,\" antwortete der Professor. \"Was führt Sie zu dieser späten Stunde in die Bibliothek?\"\n\n\"Wir recherchieren für ein Projekt,\" antwortete Alex schnell.\n\nDer Professor nickte langsam. \"Seien Sie vorsichtig, was Sie suchen. Manchmal ist es besser, bestimmte Dinge nicht zu wissen.\"\n\nMit diesen Worten drehte er sich um und ging. Sophie, Alex und Emily sahen sich\tan.&& || Sie wussten, dass sie auf der richtigen Spur waren, aber sie ahnten auch, dass die Gefahr näher war, als sie gedacht hatten."
  }
}
"""
# extract_json_from_string(str2)
test = """
    
{
  "Kapitel 8": {
    "Kapitel Titel": "Das geheimnisvolle Unterwasserreich",
    "Kapitel Inhalt Teil 3": "Clara, Leo und Yuki standen am Ufer und schauten auf das glitzernde Meer zurück. Die schimmernde Muschel in Claras Hand funkelte im Sonnenlicht. 'Ich kann es kaum glauben, dass wir das alles erlebt haben,' sagte Clara und strich über die Muschel. 'Es war wirklich ein unglaubliches Abenteuer.'\n\nLeo nickte und schüttelte erneut das Wasser aus seinem Fell. 'Und ich dachte, der Dschungel wäre aufregend! Aber das hier war etwas ganz Besonderes.'\n\nYuki, der Roboter, dessen Sensoren immer noch leicht blinkten, fügte hinzu: 'Die Daten, die ich gesammelt habe, sind von unschätzbarem Wert. Aber die Erinnerungen sind noch wertvoller.'\n\nClara lächelte und sah zu Marina, die ihnen vom Wasser aus zuwinkte. 'Danke, Marina. Ohne dich hätten wir das nie geschafft.'\n\nMarina lächelte zurück. 'Es war mir eine Freude, euch zu helfen. Ihr seid immer willkommen in unserem Reich. Passt gut auf euch auf und vergesst nicht, dass wahre Schätze nicht immer aus Gold und Edelsteinen bestehen.'\n\nClara nickte. 'Das werde ich nie vergessen. Freundschaft und Abenteuer sind die größten Schätze.'\n\nMit einem letzten Winken tauchte Marina zurück in die Tiefen des Ozeans. Clara, Leo und Yuki drehten sich um und gingen zum magischen Globus, der am Strand auf sie wartete.\n\n'Bereit für das nächste Abenteuer?' fragte Clara und legte ihre Hand auf den Globus.\n\nLeo grinste. 'Immer bereit!'\n\nYuki nickte. 'Lasst uns sehen, wohin er uns als nächstes führt.'\n\nMit einem leuchtenden Strahlen aktivierte sich der Globus, und in einem Augenblick wurden sie in ein neues Abenteuer teleportiert. Clara hielt die schimmernde Muschel fest in ihrer Hand und wusste, dass sie diese Reise nie vergessen würde. Neue Abenteuer warteten auf sie, und sie war bereit, die Welt weiter zu erkunden."
  }
}"""





escaped_str = test.replace('\"', "'").replace('\\', '').replace('\t', '').replace('"', "'")
# extract_json_from_string(test)
#escaped_str = test.replace('\\', '').replace('\t', '\\t')
#print(test.index("Kapitel Inhalt Teil"))
#print(test[test.index("Kapitel Inhalt Teil")+25])

json=extract_json_from_string(test)
def get_all_keys(d, keys_set=None):
    if keys_set is None:
        keys_set = set()
    for k, v in d.items():
        keys_set.add(k)
        if isinstance(v, dict):
            get_all_keys(v, keys_set)
    return keys_set

print(get_all_keys(json))
print(escaped_str)