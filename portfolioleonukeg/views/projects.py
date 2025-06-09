import reflex as rx
import portfolioleonukeg.constants as constants
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color
from portfolioleonukeg.components.project_card import project_card


def projects() -> rx.Component:
    projects = [
        ("alien_invasion.jpg", "Projects Alpha", "'Alien Invasion' project Python Crash Course book.", "Python PyGame", "https://github.com/leonukeg/alien_invasion"),
        ("projects.jpg","Project Beta", "Flask REST API", "Flask, SQLite","/"),
        ("projects.jpg", "Projects Gamma", "Django task manager", "Django, PostgreSQL","/"),
        ]
    
    return rx.grid(
        *[project_card(*p) for p in projects],
        columns="3",
        margin= "auto",
        #padding=Size.VERY_BIG.value,
        max_width="1000px",
        
    )