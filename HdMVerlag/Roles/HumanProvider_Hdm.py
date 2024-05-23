from metagpt.provider.human_provider import HumanProvider
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from ui.main_ui import start_second_ui, select_title, get_wait_for_title, get_final_title
from metagpt.provider.human_provider import HumanProvider
from waitingEventHandle import stop_waitUI
from waitingEventHandle import wait_thread
import time
from Utils.json_handle import extract_json_from_string


class HumanProvider_Hdm_Illustration(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("It's your turn, please type in your response. You may also refer to the context below")
        stop_waitUI()
        rsp = start_second_ui(msg)
        if rsp in ["exit", "quit"]:
            exit()
        return rsp


class HumanProvider_Hdm_Titel(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("Please choose one titel")
        select_title(extract_json_from_string(msg))
        while get_wait_for_title():  # we need this, to wait for the User to select one title
            time.sleep(1)  # without sleep CPU goes crazy
        rsp = get_final_title()
        if rsp in ["exit", "quit"]:
            exit()
        return rsp


class HumanProvider_Hdm_Idea(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("Please choose one idea")
        wait_thread.start()
        # select_title(extract_json_from_string(msg))
        # while get_wait_for_title():  # we need this, to wait for the User to select one title
        #    time.sleep(1)  # without sleep CPU goes crazy
        rsp = input(msg)
        if rsp in ["exit", "quit"]:
            exit()
        return rsp


class HumanProvider_Hdm_Korrektur(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("Please correct the text if you want")
        # select_title(extract_json_from_string(msg))
        # while get_wait_for_title():  # we need this, to wait for the User to select one title
        #    time.sleep(1)  # without sleep CPU goes crazy
        rsp1 = """
        {
    "Kapitel 1": {
        "Kapitel Titel": "Neue Anfänge",
        "Kapitel Inhalt": " Sophie war aufgeregt, als sie den ersten Schritt auf den Universitätscampus setzte. Alles war so neu und aufregend. Sie spürte eine Mischung aus Nervosität und Vorfreude, als sie sich umsah und die vielen Gebäude und Gesichter auf sich wirken ließ. Inmitten des Trubels erkannte sie plötzlich eine vertraute Gestalt. Es war Lena, ihre beste Freundin seit Kindertagen. Die beiden umarmten sich stürmisch und begannen sofort, die neuen Möglichkeiten des Studentenlebens zu erkunden. Gemeinsam besuchten sie die Orientierungsveranstaltungen und lernten die verschiedenen Clubs und Aktivitäten auf dem Campus kennen. Es fühlte sich gut an, eine vertraute Person an ihrer Seite zu haben, während sie sich in dieser neuen Umgebung zurechtfinden musste. Doch trotz Lenas Unterstützung fühlte sich Sophie auch ein wenig unsicher. Sie fragte sich, ob sie den Anforderungen des Studiums gewachsen sein würde und ob sie neue Freunde finden könnte. Diese Gedanken begleiteten sie, als sie sich auf den Weg zu ihrer ersten Vorlesung machte. Dort begegnete sie Max zum ersten Mal. Er saß in der ersten Reihe, lächelte sie an und bot ihr einen Platz neben sich an. Sophie spürte sofort eine gewisse Anziehungskraft zwischen ihnen und war neugierig darauf, mehr über ihn zu erfahren. Während der Vorlesung entdeckten sie, dass sie einige Gemeinsamkeiten hatten, und verabredeten sich, um sich nach der Vorlesung auf einen Kaffee zu treffen. Diese Begegnung sollte der Beginn einer besonderen Verbindung sein, die Sophie und Max auf eine Reise voller Herausforderungen und Erfolge im Studentenleben führen würde. Sophie und Max verbrachten den Nachmittag damit, sich näher kennenzulernen. Sie teilten ihre Träume, Ängste und Hoffnungen miteinander und fanden heraus, dass sie viele gemeinsame Interessen hatten. Während ihres Gesprächs entdeckten sie, dass sie beide eine Leidenschaft für das Reisen und die Fotografie teilten. Max erzählte von seinen Abenteuern in fernen Ländern, und Sophie berichtete von ihrer Begeisterung für die faszinierende Architektur und Kultur verschiedener Städte. Es war, als ob sie sich schon lange kennen würden, und doch war da auch eine aufregende Spannung, die sie beide spürten. Als die Sonne langsam unterging, beschlossen sie, gemeinsam zum Abendessen zu gehen. Auf dem Weg zum Restaurant tauschten sie Geschichten aus ihrer Vergangenheit aus und lachten über lustige Erlebnisse. Es fühlte sich an, als ob sie sich in einer Blase befanden, in der nur sie beide existierten. Doch die Realität holte sie ein, als sie das Restaurant betraten und auf Lena trafen, die bereits auf sie wartete. Lena strahlte vor Freude, als sie die beiden sah, und schien zu ahnen, dass sich zwischen Sophie und Max etwas Besonderes entwickelte. Während des Abendessens erzählte Lena von ihren eigenen Abenteuern und Herausforderungen, und die drei Freunde verbrachten einen unvergesslichen Abend miteinander. Als sie sich später voneinander verabschiedeten, wussten Sophie und Max, dass sich ihr Leben für immer verändert hatte, und sie freuten sich auf die gemeinsamen Herausforderungen, die noch vor ihnen lagen. Sophie fühlte sich dankbar für Lenas Unterstützung, als sie sich in der neuen Umgebung zurechtfinden musste. Die anfängliche Unsicherheit wich langsam einem Gefühl der Aufregung und Abenteuerlust. Max war stets an ihrer Seite, ermutigte sie, sich neuen Herausforderungen zu stellen, und half ihr, ihre Leidenschaft für Architektur und Kultur weiter zu entfalten. Gemeinsam erkundeten sie die Campusstadt und entdeckten versteckte Ecken, die sie mit ihrer Kamera festhielten. In diesen Momenten fühlte sich Sophie lebendiger und freier als je zuvor. Professor Müller ermutigte sie, ihre kreativen Interessen zu verfolgen und eröffnete ihr neue Perspektiven. Die Freundschaft zwischen Sophie, Max und Lena wuchs mit jeder gemeinsamen Erfahrung. Als sie sich später voneinander verabschiedeten, wussten sie, dass sich ihr Leben für immer verändert hatte, und sie freuten sich auf die gemeinsamen Herausforderungen, die noch vor ihnen lagen."
    },
    "Kapitel 2": {
        "Kapitel Titel": "Liebe im Uni-Alltag",
        "Kapitel Inhalt": " Sophie und Max verbrachten immer mehr Zeit miteinander, vertieften ihre Beziehung und entdeckten, dass sie sich ineinander verliebt hatten. Die gemeinsamen Höhen und Tiefen des Uni-Alltags schweißten sie noch enger zusammen. Während Sophie sich mit den Anforderungen des Studiums auseinandersetzte, fand sie in Lena eine unterstützende Freundin, die sie ermutigte, weiterzumachen. Max hingegen suchte Rat bei Professor Müller, der ihm wichtige Ratschläge gab, wie er seine Leidenschaft für Architektur und Design mit seinem Studium verbinden konnte. Die Unterstützung von Freunden und Mentoren half beiden, ihre eigenen Wege zu finden und sich in der neuen Umgebung zurechtzufinden. Inmitten des Uni-Alltags erlebten Sophie und Max ein unerwartetes Ereignis, das sie noch näher zusammenbrachte. Sie lernten, dass Liebe und Unterstützung in schwierigen Zeiten besonders wichtig sind und dass sie gemeinsam jede Herausforderung meistern konnten. Als Sophie und Max sich tiefer in ihre Beziehung vertieften, wurden sie mit neuen Herausforderungen konfrontiert, die ihr Band auf die Probe stellten. Der Uni-Alltag brachte nicht nur gemeinsame Höhen, sondern auch Tiefen mit sich, die sie gemeinsam meistern mussten. Während Sophie sich weiterhin mit den Anforderungen des Studiums auseinandersetzte, fand sie in Lena eine unterstützende Freundin, die sie ermutigte, weiterzumachen. Lena selbst musste ihre eigenen Herausforderungen meistern, was ihre Freundschaft mit Sophie auf eine neue Ebene brachte. Max hingegen suchte weiterhin Rat bei Professor Müller, der ihm half, seine Leidenschaft für Architektur und Design mit seinem Studium zu verbinden. Die Gespräche mit Professor Müller eröffneten Max neue Perspektiven und halfen ihm, seine Ziele klarer zu definieren. Die Unterstützung von Freunden und Mentoren erwies sich als entscheidend, als Sophie und Max mit unerwarteten Schwierigkeiten konfrontiert wurden. Inmitten des Uni-Alltags und der damit verbundenen Herausforderungen lernten sie, dass Liebe und Unterstützung in schwierigen Zeiten besonders wichtig sind. Ihr gemeinsames Band wurde durch das Überwinden von Hindernissen gestärkt, und sie erkannten, dass sie gemeinsam jede Herausforderung meistern konnten, solange sie füreinander da waren. Als der Semesterstress zunahm, fanden sich Sophie und Max inmitten von Prüfungsvorbereitungen und Projektarbeiten wieder. Die Anforderungen des Studiums forderten ihren Tribut, und sie mussten lernen, wie sie ihre Zeit effektiv nutzen konnten, um den Herausforderungen gerecht zu werden. In dieser stressigen Zeit fanden sie Trost und Unterstützung in ihrer Beziehung, die ihnen die nötige Kraft gab, um durchzuhalten. Sophie war entschlossen, sich den Prüfungen zu stellen, aber Zweifel nagten dennoch an ihr. Max erkannte ihre Unsicherheit und stand ihr bei, indem er sie ermutigte und an ihre Fähigkeiten glaubte. 'Du bist so talentiert, Sophie. Du schaffst das', sagte er sanft, während er ihre Hand hielt. Diese Worte gaben Sophie die Zuversicht, die sie brauchte, um sich ihren Ängsten zu stellen. Währenddessen fand Lena in ihrer eigenen Prüfungsphase Unterstützung bei Professor Müller, der ihr half, ihre Leidenschaft für Geschichte mit ihren akademischen Verpflichtungen in Einklang zu bringen. 'Sie haben das Potenzial, die Welt der Geschichte zu verändern', ermutigte er sie. Diese Worte beflügelten Lena und gaben ihr die Motivation, die sie brauchte, um sich den Herausforderungen zu stellen. Inmitten des Prüfungsstresses fanden Sophie, Max und Lena Trost und Ermutigung in ihrer Freundschaft und den weisen Ratschlägen ihres Mentors. Sie erkannten, dass sie gemeinsam stark waren und dass ihre Liebe und Unterstützung füreinander unersetzlich waren, besonders in Zeiten der Prüfungen und Unsicherheiten."
    }
}
        """
        print("rsp1")
        print(rsp1)

        return rsp1
