import fire
import os
from metagpt.logs import logger
from metagpt.team import Team
from Roles.Autor import Autor
from Roles.Editor import Editor
from Roles.Human_User import Human_User
from workspace.Utils.json_handle import remove_values_json
from writeLatex import generate_pdf
from ui.main_ui import start_ui
from ui.waitingEventHandle import wait_thread

ui_prompt = start_ui()
print(ui_prompt)
wait_thread.start()


async def main(

        idea: str = ui_prompt,
        idea1: str = """
{
            "genre": "Kinderbuch",
            "thema": "Mädchen, die die Welt erkundet",
            "tonalitaet" : "lüstig ",
            "anzahlvonkapitel":9
        }
        """,
        investment: float = 2,
        n_round: int = 15,
):
    logger.info(idea)

    team = Team()
    team.hire(
        [
            Editor(),
            Autor(),
            Human_User(is_human=True),
        ]
    )

    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)
    generate_pdf()
    generate_pdf()


if __name__ == "__main__":
    with open(os.path.join("workspace") + "/" + "conversation.txt", 'w') as file:
        file.write("")
    remove_values_json()
    fire.Fire(main)
