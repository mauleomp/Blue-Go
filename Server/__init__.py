from flask import Flask

app = Flask(__name__)
app.secret_key = "AFr_256897/@"

app.debug = True

from Server import routes