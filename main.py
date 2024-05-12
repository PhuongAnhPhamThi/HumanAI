import os
import threading

import fire
from metagpt.logs import logger
from metagpt.team import Team

from Roles.Autor import Autor
from Roles.Editor import Editor
from Roles.Human_User import Human_User
from ui.main_ui import start_ui, start_wait_ui  # import start_ui aus ui um UI zu starten
from workspace.Utils.json_handle import remove_values_json
from workspace.writeLatex import generate_pdf


# help function for wait UI
def controlled_start_wait_ui(stop_event):
    start_wait_ui(stop_event)


# new thread for wait UI
stop_event = threading.Event()
wait_thread = threading.Thread(target=controlled_start_wait_ui, args=(stop_event,))
"""Thread and Wait UI can be started with:

wait_thread.start()

ans should be stopped with:

stop_event.set()
html_generated()
thread.join()
"""

ui_prompt = start_ui()

async def main(

        idea: str = ui_prompt,
        idea1: str = """
{
            "genre": "Asian Roman",
            "gattung": "Liebe Geschichte",
            "tonalitaet" : "romantisch",
            "anzahlvonkapitel":2
        }
        """,
        investment: float = 0.1,
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
