from .model import God
from lib.background import backgrounds_en, backgrounds_pt

gods_list : list[God] = [
    God(
        name="Apholo",
        background_pt= backgrounds_pt["apholo"],
        background_en= backgrounds_en["apholo"],
        image="./images/apholo.png"
    ),
    God(
        name="Aphrodite",
        background_pt= backgrounds_pt["aphrodite"],
        background_en= backgrounds_en["aphrodite"],
        image= "./images/aphrodite.png"
    ),
        God(
        name="Ares",
        background_pt= backgrounds_pt["ares"],
        background_en= backgrounds_en["ares"],
        image="./images/ares.png"
    ),
    God(
        name="Artemis",
        background_pt= backgrounds_pt["artemis"],
        background_en= backgrounds_en["artemis"],
        image= "./images/artemis.png"
    ),
    God(
        name="Athena",
        background_pt= backgrounds_pt["athena"],
        background_en= backgrounds_en["athena"],
        image="./images/athena.png"
    ),
    God(
        name="Dionysus",
        background_pt= backgrounds_pt["dionysus"],
        background_en= backgrounds_en["dionysus"],
        image= "./images/dionysus.png"
    ),
        God(
        name="Hades",
        background_pt= backgrounds_pt["hades"],
        background_en= backgrounds_en["hades"],
        image="./images/hades.png"
    ),
    God(
        name="Hera",
        background_pt= backgrounds_pt["hera"],
        background_en= backgrounds_en["hera"],
        image= "./images/hera.png"
    ),
        God(
        name="Hermes",
        background_pt= backgrounds_pt["hermes"],
        background_en= backgrounds_en["hermes"],
        image="./images/hermes.png"
    ),
    God(
        name="Posseidon",
        background_pt= backgrounds_pt["posseidon"],
        background_en= backgrounds_en["posseidon"],
        image= "./images/posseidon.png"
    ),
    God(
        name="Zeus",
        background_pt= backgrounds_pt["zeus"],
        background_en= backgrounds_en["zeus"],
        image="./images/zeus.png"
    )   
]

gods_dict : dict[str, God] = {god.name : god for god in gods_list}