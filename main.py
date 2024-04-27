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


async def main(
        #idea: str = """Gedichte für Kinder""",
        idea: str =
        """{
            "genre": "Haiku",
            "gattung": "Gedicht"
        }"""
        ,
        investment: float = 0.2,
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
    with open(file_path, 'w') as file:
        file.write("")
    fire.Fire(main)
