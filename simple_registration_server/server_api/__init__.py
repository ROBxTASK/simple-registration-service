# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v1
import os
import time
from logging.config import dictConfig

log_level = os.getenv("DEVICE_REGISTER_LOG_LEVEL", "INFO")

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': log_level,
        'handlers': ['wsgi']
    }
})


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    app.config["MONGO_URI"] = os.environ["DEVICE_REGISTER_MONGO_URI"]
    app.logger.info(app.config)
    app.logger.info('build time: {}'.format(time.ctime(os.path.getmtime("."))))
    app.logger.info('app age: {:.0f}s'.format(time.time() - os.path.getmtime(".")))
    return app

if __name__ == '__main__':
    create_app().run(host="0.0.0.0", debug=(log_level == 'DEBUG'))