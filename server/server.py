import blueprints
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask app
app = Flask(__name__)
swagger = Swagger(app)

# Initialize cache
blueprints.common.cache.init_app(app)

# Register blueprints
app.register_blueprint(blueprints.autocomplete.app, url_prefix="/autocomplete")
app.register_blueprint(blueprints.caching.app, url_prefix="/caching")
app.register_blueprint(blueprints.genres.app, url_prefix="/genres")
app.register_blueprint(blueprints.movies.app, url_prefix="/movies")
app.register_blueprint(blueprints.personality.app, url_prefix="/personality")
app.register_blueprint(blueprints.ratings.app, url_prefix="/ratings")
app.register_blueprint(blueprints.users.app, url_prefix="/users")

# Initialize cross origin resource sharing
CORS(app, origins="http://localhost")

# Create a new Prometheus metrics export configuration
PrometheusMetrics(app)
