from metagpt.actions import Action
from metagpt.configs.llm_config import LLMConfig
from Roles.HumanProvider_Hdm import HumanProvider_Hdm_Illustration

mock_llm_config = LLMConfig(
    llm_type="mock",
    api_key="mock_api_key",
    base_url="mock_base_url",
    app_id="mock_app_id",
    api_secret="mock_api_secret",
    domain="mock_domain",
)


class illustrieren(Action):
    name: str = "illustrieren"

    async def run(self, prompt_fur_bookcover: str):
        human_provider = HumanProvider_Hdm_Illustration(mock_llm_config)
        rsp = await human_provider.aask(msg=prompt_fur_bookcover)
        return rsp
