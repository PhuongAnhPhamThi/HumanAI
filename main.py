import fire
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team
from Roles.Autor import Autor
from Roles.Editor import Editor
#from Roles.Editor2 import Editor,Editor2
from Roles.Illustrator import Illustrator
from Roles.LayoutDesigner import LayoutDesigner
from Roles.Editor import file_path
from ui.main_ui import start_ui, start_second_ui    # import start_ui aus ui um UI zu starten



ui_prompt = start_ui()

async def main(
        #idea: str = """Gedichte für Kinder""",
        idea: str = ui_prompt,
        investment: float = 0.08,
        n_round: int = 15,
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            Editor(),
            #Editor2(),
            Autor(),
            Illustrator(is_human=True),
            LayoutDesigner(),


        ]
    )

    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)


if __name__ == "__main__":
    with open(file_path + "conversation.txt", 'w') as file:
        file.write("")
    fire.Fire(main)

