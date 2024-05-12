import fire
import os
from metagpt.logs import logger
from metagpt.team import Team
from Roles.Autor import Autor
from Roles.Editor import Editor
from Roles.Human_User import Human_User
from ui.main_ui import start_ui, start_second_ui, start_wait_ui, html_generated  # import start_ui aus ui um UI zu starten
from runport import start_server
from workspace.layouterstellen import update_html_from_json
from workspace.writeLatex import generate_pdf
import threading

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

        #idea: str = ui_prompt,
        idea: str = """
{
            "genre": "Asian Roman",
            "gattung": "Liebe Geschichte",
            "tonalitaet" : "romantisch",
            "anzahlvonkapitel":4
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
            #LayoutDesigner(),
        ]
    )

    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)
    generate_pdf()
    generate_pdf()
    #update_html_from_json()
    #start_server()


if __name__ == "__main__":
    with open(os.path.join("workspace") + "/" + "conversation.txt", 'w') as file:
        file.write("")

    fire.Fire(main)

