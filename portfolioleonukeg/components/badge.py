import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color

def badge(text: str) -> rx.components:
    return rx.box(
        
        
        rx.text(text, weight="bold", style={"color": Color.WITHE.value, "fontSize": Size.DEFAULT.value}),
    
        background_color = Color.PETROL.value,
        border_radius=Size.SMALL.value,
        margin=Size.SMALL.value,
        padding=Size.SMALL.value,
        
        
    )
    