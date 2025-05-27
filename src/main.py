import src.sly_functions as f
import src.sly_globals as g
from src.ui.projects import set_training_data_table
from src.ui.sidebar import sidebar
from supervisely import Application
from supervisely.app.widgets import Container, Dialog

# from sly_sdk.webpy.app import WebPyApplication

dialog = Dialog(content=sidebar, title="New Experiment")
dialog.show()


layout = Container(widgets=[dialog], widget_id="main_layout_cont")


app = Application(layout=layout, static_dir="src")

g.api = f._init_api(app)

# update models
set_training_data_table(g.api)
