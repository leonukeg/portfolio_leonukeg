import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def contact_form() -> rx.Component:
    return rx.box(
    
        rx.hstack(
                rx.form(
                    rx.vstack(
                        rx.text("Contact", color=Color.PETROL.value, font_size=Size.MEDIUM.value),
                        rx.hstack(
                            rx.input(placeholder="Your Name",name="name",),

                            rx.input(placeholder="your.email@example.com", name="email", type="email"),
                        ),
                    
                        rx.text_area(placeholder="Your Message",name="message"),

                    
                        padding_x=Size.DEFAULT.value,
                        padding_y=Size.DEFAULT.value,
                    ),
                    #action="https://formsubmit.co/chemaruan@gmail.com", ojo con esto hay que arreglarlo para que funcione
                    #method="POST",
                    reset_on_submit=True,
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