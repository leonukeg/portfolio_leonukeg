import reflex as rx
import portfolioleonukeg.constants as constants
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color
from portfolioleonukeg.components.project_card import project_card


def projects() -> rx.Component:
    projects = [
        ("alien_invasion.jpg", "Project Alpha", "'Alien Invasion' project Python Crash Course book.", "Python PyGame", constants.ALIEN_INVASION),
        ("slyshaka.png","Project Beta", "slyshaka.com, tshirt store.", "Wordpress Elementor woocommerce",constants.SLYSHAKA),
        ("projects.jpg", "Projects Gamma","Big data, soccer", "anaconda... ","#"),
        ]
    
    return rx.grid(
        *[project_card(*p) for p in projects],
        columns="3",
        margin= "auto",
        max_width="1000px",
        
    )