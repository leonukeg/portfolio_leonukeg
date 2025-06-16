import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def about() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="freddy_leon.png", alt="imagen caricatura freddy leon", width= Size.X_LARGE.value, height = Size.X_LARGE.value, padding=Size.MEDIUM.value),

            rx.vstack(
                rx.text("Freddy Leon Romero", color=Color.PETROL.value, font_size=Size.BIG.value),
                rx.text("Python Developer",  font_size=Size.MEDIUM.value),
                rx.text("> ... Programming calms me."),
                rx.text("I’m not here to sell myself."),
                rx.text(" "),
                rx.text("This portfolio is my space, my style, my way of showing how I think and work."),
                rx.text("Simple, functional, with personality. Straightforward… with the soul of an open terminal."),
                rx.text(" "),
                rx.text("Learning to create from scratch. At my own pace, with my own logic."),
                rx.text("Falls, tests, repetition… until it flows."),
                rx.text("Skateboarding taught me that skill comes, but consistency and discipline win."),
                rx.text("And that there’s no style without attitude."),
                rx.text(" "),
                rx.text("My goal is simple:"),
                rx.text("Master Python until it feels like an extension of my thoughts."),
                rx.text(" "),
                rx.text("If any of this made you stay a little longer…"),
                rx.text("we’re already connecting."),
                rx.text(" "),
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