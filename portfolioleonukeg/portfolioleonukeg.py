import reflex as rx
import portfolioleonukeg.styles.styles as styles
from portfolioleonukeg.views.navbar  import navbar
from portfolioleonukeg.views.about import about
from portfolioleonukeg.views.projects import projects
from portfolioleonukeg.views.footer import footer
from portfolioleonukeg.views.skills import skills
from portfolioleonukeg.views.firma import firma
from portfolioleonukeg.views.contact import contact_form

def index() -> rx.Component:
    rx.script("document.documentElement.lang='es"),
    return rx.box(
        navbar(),
        about(),
        projects(),
        skills(),
        contact_form(),
        firma(),
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

