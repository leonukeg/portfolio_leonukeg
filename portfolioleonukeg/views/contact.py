import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def contact_form() -> rx.Component:
    input_style = {
        "color":Color.PETROL.value,
        #"padding": "0.5em",
        "background": Color.GRAY.value,
        "_placeholder":{
            "color":Color.ORANGE.value

        },
        "_focus": {
            "color":Color.PETROL.value,
            "border": f"2px solid Color.ORANGE.value",
            "background": Color.WITHE.value  # Fondo blanco al enfocar (opcional)
        },
    }

    return rx.box(
    
        rx.hstack(
                rx.form(
                    rx.vstack(
                        rx.text("Contact", color=Color.PETROL.value, font_size=Size.MEDIUM.value),
                        rx.hstack(
                            rx.input(placeholder="Your Name",name="name",**input_style),

                            rx.input(placeholder="your.email@example.com", name="email", type="email"),
                        ),
                    
                        rx.text_area(placeholder="Your Message",name="message"),
                        rx.button("Send Message",type="submit",bg=Color.ORANGE.value),

                    
                        padding_x=Size.DEFAULT.value,
                        padding_y=Size.DEFAULT.value,
                    ),
                    action="https://formsubmit.co/chemaruan@gmail.com",
                    method="post",
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