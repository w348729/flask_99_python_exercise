from flask import Flask
from flask_cors import CORS
from flask_model import db
from flask_config import Config
from flask_api.listing import listing
from flask_api.users import users

app = Flask(__name__)


app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(users)
app.register_blueprint(listing)

CORS(app, supports_credentials=True)


@app.route("/", methods=['GET'])
def hello():
    return '99.co test flask_api'


