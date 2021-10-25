# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app, g

from werkzeug.local import LocalProxy

# Use LocalProxy to read the global db instance with just `db`
from .db_util import get_db
db = LocalProxy(get_db)

import logging
log = logging.getLogger(__name__)

def get(devices):
    current_app.logger.info("get devices")
    current_app.logger.debug(devices)
    result = db.devices.find({}, {'_id': False})
    log.debug(result)
    return result
