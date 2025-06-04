import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def about() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="freddy_leon.png", alt="imagen caricatura freddy leon", width= Size.X_LARGE.value, height = Size.X_LARGE.value, padding=Size.MEDIUM.value),

            rx.vstack(
                rx.text("Freddy Leon Romero", color=Color.PETROL.value, font_size=Size.MEDIUM.value),
                rx.text("Python Developer", color=Color.BLACK.value),
                rx.text("> ... by day, debugger by night. I build simple things that work, without overengineering.  " 
                        "A fan of minimalism, thick black borders, and print('hello world')s that never fail.", color=Color.BLACK.value),
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