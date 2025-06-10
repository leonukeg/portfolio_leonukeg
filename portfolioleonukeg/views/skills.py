import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color
from portfolioleonukeg.components.badge import badge

def skills() -> rx.Component:
    return rx.box(
        rx.hstack(
                rx.vstack(
                rx.text("Skills", color=Color.PETROL.value, font_size=Size.MEDIUM.value),

                rx.hstack(
                    badge("Python"),
                    badge("Reflex"),
                    badge("Pygame"),
                    badge("Wordpress"),
                    badge("Photoshop"),
                    badge("Illustrator")
                ),
                
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            ),
            border_radius=Size.SMALL.value, 
            align_items="center",
            background_color = Color.WITHE.value,
            box_shadow = styles.BOX_SHADOW,
            max_width="1000px",
            margin="auto",
        ),
        padding=Size.VERY_BIG.value,
    )