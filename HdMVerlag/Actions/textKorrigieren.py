from metagpt.actions import Action
from metagpt.configs.llm_config import LLMConfig
from Roles.HumanProvider_Hdm import HumanProvider_Hdm_Korrektur

mock_llm_config = LLMConfig(
    llm_type="mock",
    api_key="mock_api_key",
    base_url="mock_base_url",
    app_id="mock_app_id",
    api_secret="mock_api_secret",
    domain="mock_domain",
)


class textKorrigieren(Action):
    name: str = "textKorrigieren"

    async def run(self, text_json: str):
        print("in action text korrigieren)")
        human_provider = HumanProvider_Hdm_Korrektur(mock_llm_config)
        rsp = await human_provider.aask(msg=text_json)
        return rsp
