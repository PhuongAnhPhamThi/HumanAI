from metagpt.actions import Action
from metagpt.configs.llm_config import LLMConfig
from Roles.HumanProvider_Hdm import HumanProvider_Hdm


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
    PROMPT_TEMPLATE: str = """
"Hello Frida (Human). Du bist der Illustrator des VerlagHdM. Deine Aufgabe ist Buchcover zu erstellen. Gehzu Seite: "https://www.bing.com/images/create/" und erstell ein Book Cover mit diesem Promtp:
Prompt: {prompt_fur_bookcover}"
"""

    async def run(self, prompt_fur_bookcover: str):
        #prompt = self.PROMPT_TEMPLATE.format(prompt_fur_bookcover=prompt_fur_bookcover)
        human_provider = HumanProvider_Hdm(mock_llm_config)
        rsp = await human_provider.aask(msg=prompt_fur_bookcover)
        return rsp
