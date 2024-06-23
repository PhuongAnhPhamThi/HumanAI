from metagpt.provider.human_provider import HumanProvider
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from ui.main_ui import start_second_ui, select_title, get_wait_for_title, get_final_title,select_chapter,\
    start_chapter_ui,MyThread,get_wait_for_chapter, get_final_chapters
from metagpt.provider.human_provider import HumanProvider
from waitingEventHandle import stop_waitUI
from waitingEventHandle import wait_thread, chapter_thread
import time
from Utils.json_handle import extract_json_from_string





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
        select_title(extract_json_from_string(msg))
        while get_wait_for_title():  # we need this, to wait for the User to select one title
            time.sleep(1)  # without sleep CPU goes crazy
        rsp = get_final_title()
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
        #rsp = msg
        #chapter_thread = MyThread(2)
        stop_waitUI()
        while wait_thread.is_alive():
            print("waiting for t1 in Korrektur")
            time.sleep(1)
        chapter_thread.start()
        time.sleep(10)
        select_chapter(msg)
        while get_wait_for_chapter():
            print("waiting for chapter editing")
            time.sleep(1)

        rsp = get_final_chapters()

        return rsp
class HumanProvider_Hdm_Illustration(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("It's your turn, please type in your response. You may also refer to the context below")

        while chapter_thread.is_alive():
            print("waiting for t1 in Illustration")
            time.sleep(1)
        rsp = start_second_ui(msg)
        if rsp in ["exit", "quit"]:
            exit()
        return rsp
