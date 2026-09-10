from flask import Flask

from backend.routes import main


app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="static"
)


# Register application routes
app.register_blueprint(main)


if __name__ == "__main__":

    app.run(
        debug=True
    )