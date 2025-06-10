import reflex as rx
import portfolioleonukeg.constants as constants
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color


def footer() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.vstack(
                rx.text("Portfolio Freddy Leon Romero ", style={"color": Color.BLACK.value, "fontSize": Size.M_SMALL.value}),
                rx.link("creado con cariño por @leonukeg", href=constants.GIT_HUB_URL, is_external=True, _hover={"color":Color.ORANGE.value}, style={"color": Color.BLACK.value,"fontSize": Size.M_SMALL.value}),
                align_items="center",
                spacing="0",
            
            ),
            rx.spacer(),
            rx.vstack(
                rx.image(src="logo_fl.png", alt="logotipo leonukeg", width= "3.5em", height = "2.5em"),
            ), 
            width="100%"
        ),
        margin_top= Size.DEFAULT.value,
        background_color = Color.PETROL.value,
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
    )