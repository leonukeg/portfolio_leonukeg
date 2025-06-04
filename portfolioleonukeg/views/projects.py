import reflex as rx
from portfolioleonukeg.styles.styles import Size
from portfolioleonukeg.styles.colors import Color
from portfolioleonukeg.components.project_card import project_card

def projects() -> rx.Component:
    projects = [
        ("projects.jpg", "Projects Alpha", "Django task manager", "Django, PostgreSQL"),
        ("projects.jpg","Project Beta", "Flask REST API", "Flask, SQLite"),
        ("projects.jpg", "Projects Gamma", "Django task manager", "Django, PostgreSQL")
        ]
    
    return rx.grid(
        *[project_card(*p) for p in projects],
        columns="3",
        margin= "auto",
        #padding=Size.VERY_BIG.value,
        max_width="1000px",
        
    )