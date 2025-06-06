import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.views.navbar  import navbar
from portfolioleonukeg.views.about import about
from portfolioleonukeg.views.projects import projects
from portfolioleonukeg.views.footer import footer

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.text("esta es una prueba desde linux"),
        about(),
        projects(),
        footer(),
        
    )
    
app = rx.App(
    stylesheets= styles.STYLESHEET,
    style= styles.BASE_STYLE
)

app.add_page(
    index,
    title = "Portfolio Leonukeg",
    description = "Este es mi portafolio"
)

