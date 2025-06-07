import reflex as rx
import portfolioleonukeg.constants as constants
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="leonukeg vector_verde petroleo.png", alt="logotipo leonukeg", width= Size.BIG.value, height = Size.BIG.value),
        ),
    )