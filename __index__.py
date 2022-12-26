import os
from flask import Flask
from mongoengine import connect, errors
from exceptions import ApiError
import dotenv
from routes import routes
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)
dotenv.load_dotenv()
db = connect(host=os.environ.get('MONGODB_HOST'))

for route in routes:
    app.register_blueprint(route)


@app.errorhandler(ApiError.ApiError)
def api_error(error):
    return error.message, error.status


@app.errorhandler(404)
def api_error(error):
    return 'Url is not found', 404


@app.errorhandler(errors.ValidationError)
def validation_error(error):
    return 'Id is not valid', 500


@app.errorhandler(Exception)
def global_error(error):
    return 'Unexpected error', 500


if __name__ == "__main__":
    app.run(debug=True)
