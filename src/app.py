from flask import Flask
from pangea.routes import sectors
app = Flask(__name__)

app.register_blueprint(sectors.sectors)

if __name__ == "__main__":
    app.run(debug=True)

