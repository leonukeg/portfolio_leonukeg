import reflex as rx   
from enum import Enum 
from .fonts import Font
from .colors import Color

class Size(Enum):
    SMALL = "0.5em"
    M_SMALL = "0.75em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    LARGE = "8em"
    M_LARGE = "10em"
    X_LARGE = "16em"
    XX_LARGE = "25em"
    
    SCREEN_SIZE = "60vw"
    



STYLESHEET = [
    "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color" : Color.BLACK.value,
    "background": Color.BASE.value
    
    
}

BOX_SHADOW = f"{Size.SMALL.value} {Size.SMALL.value} {Size.SMALL.value} {Color.GRAY.value}"

INPUT_STYLE = {
        "color":Color.PETROL.value,
        "padding": "0.5em",
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
