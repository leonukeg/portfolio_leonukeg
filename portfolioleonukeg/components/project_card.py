import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def project_card(image, title: str, desc: str, tech:str, url: str) -> rx.components:
    return rx.box(
        rx.vstack(
            
            rx.image(src=image, padding=Size.MEDIUM.value, width= Size.X_LARGE.value, height = Size.X_LARGE.value, box_shadow = styles.BOX_SHADOW),
            rx.text(title, weight="bold", style={"color": Color.BLACK.value, "fontSize": Size.MEDIUM.value}),
            rx.text(desc, style={"color": Color.BLACK.value,}, align="center"), 
            rx.text(tech, style={"color": Color.PETROL.value,}, align="center", weight="bold"),
            rx.link("Repo",href=url,is_external=True, style={"color": Color.ORANGE.value}),
            align_items="center",
            
        ),
        
        background_color = Color.WITHE.value,
        border_radius=Size.SMALL.value,
        margin=Size.SMALL.value,
        padding=Size.DEFAULT.value,
        _hover= {"box_shadow":styles.BOX_SHADOW},
        
    )
    