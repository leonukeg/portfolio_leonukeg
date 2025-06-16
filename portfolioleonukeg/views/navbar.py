import reflex as rx
import portfolioleonukeg.constants as constants
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="leonukeg vector_naranja.png", alt="logotipo leonukeg", width= Size.BIG.value, height = Size.BIG.value),
            rx.text("LeonUkeg's Portfolio", ),
            rx.spacer(),
            rx.link(rx.image(src="git_hub.png", alt="logo github", width= Size.MEDIUM.value, height = Size.MEDIUM.value), href=constants.GIT_HUB_URL, is_external= True),
            rx.link(rx.image(src="x.png", alt="logo x", width= Size.MEDIUM.value, height = Size.MEDIUM.value),href=constants.X_URL, is_external= True),
            spacing='3',
            align_items="center",
            justify_content="space-between",
            width ="100%"
        ),
        background_color = Color.BASE.value,
        position = "sticky",
        border_bottom = f"0.01em solid {Color.ORANGE.value}",
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index="999",
        top = "0",
        width ="100%"
    )