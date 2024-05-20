from metagpt.actions import Action
from metagpt.configs.llm_config import LLMConfig
from Roles.HumanProvider_Hdm import HumanProvider_Hdm_Titel

mock_llm_config = LLMConfig(
    llm_type="mock",
    api_key="mock_api_key",
    base_url="mock_base_url",
    app_id="mock_app_id",
    api_secret="mock_api_secret",
    domain="mock_domain",
)


class titelEmpfehlen(Action):
    name: str = "titelEmpfehlen"

    async def run(self, titeln: str):
        human_provider = HumanProvider_Hdm_Titel(mock_llm_config)
        rsp = await human_provider.aask(msg=titeln)
        return rsp
