import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color


def firma() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="freddyleonromero_firma.png",width="30em", height="10em", padding=Size.DEFAULT.value,),    
            border_radius=Size.SMALL.value, 
            align_items="center",
            justify_content="center",
            background_color = Color.BLACK.value,
            box_shadow = styles.BOX_SHADOW,
            max_width="1000px",
            margin="auto",
        ),
        padding=Size.BIG.value,
    )