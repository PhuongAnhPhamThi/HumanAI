import fire
import asyncio
from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team
from Roles.Autor import Autor
from Roles.Editor import Editor
from Roles.Illustrator import Illustrator
from Roles.Editor import file_path
from ui.main_ui import start_ui, start_second_ui    # import start_ui aus ui um UI zu starten

ui_prompt = start_ui()
print(ui_prompt )
print(type(ui_prompt ))
async def main(
        #idea: str = """Gedichte für Kinder""",
        idea: str = ui_prompt
        ,
        investment: float = 0.001,
        n_round: int = 15,
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            Editor(),
            Autor(),
            Illustrator(is_human=True)


        ]
    )

    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)


if __name__ == "__main__":
    # UI starten und Input Prompt ui_prompt bekommen
    #ui_prompt = start_ui()

    with open(file_path, 'w') as file:
        file.write("")
    fire.Fire(main)

