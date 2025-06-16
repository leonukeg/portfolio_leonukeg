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
                    badge("Python",Color.PETROL.value, Color.WITHE.value),
                    badge("Reflex",Color.PETROL.value, Color.WITHE.value),
                    badge("Pygame",Color.PETROL.value, Color.WITHE.value),
                    badge("Wordpress",Color.PETROL.value, Color.WITHE.value),
                    badge("Windows",Color.PETROL.value, Color.WITHE.value),
                    badge("Linux",Color.PETROL.value, Color.WITHE.value),
                    badge("Git",Color.PETROL.value, Color.WITHE.value),

                ),

                rx.hstack(
                    badge("Photoshop",Color.ORANGE.value, Color.BLACK.value),
                    badge("Illustrator",Color.ORANGE.value, Color.BLACK.value),
                    badge("Adobe XD",Color.ORANGE.value, Color.BLACK.value),
                    badge("Excel",Color.ORANGE.value, Color.BLACK.value),
                    badge("Word",Color.ORANGE.value, Color.BLACK.value),

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
        padding=Size.BIG.value,
    )