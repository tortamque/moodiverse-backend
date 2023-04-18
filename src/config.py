from flask import Flask

app = Flask(__name__)

rate_limits = {
    "default": "6 per minute"
}
