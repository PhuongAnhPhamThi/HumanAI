from metagpt.provider.human_provider import HumanProvider
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from ui.main_ui import start_second_ui, select_title, get_wait_for_title, get_final_title
from metagpt.provider.human_provider import HumanProvider
from waitingEventHandle import stop_waitUI
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
