from metagpt.provider.human_provider import HumanProvider
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from ui.main_ui import start_second_ui
from metagpt.provider.human_provider import HumanProvider


class HumanProvider_Hdm_Illustration(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("It's your turn, please type in your response. You may also refer to the context below")
        rsp = start_second_ui(msg)
        if rsp in ["exit", "quit"]:
            exit()
        return rsp

class HumanProvider_Hdm_Titel(HumanProvider):
    """Child class inheriting from HumanProvider with modified ask function"""

    def ask(self, msg: str, timeout=USE_CONFIG_TIMEOUT) -> str:
        logger.info("Please choose one titel")
        rsp = input(msg)
        if rsp in ["exit", "quit"]:
            exit()
        return rsp
