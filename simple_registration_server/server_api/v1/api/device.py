# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app, g

from . import Resource
from .. import schemas

from v1.controllers import device_controller

class Device(Resource):

    def get(self, body=None):
        current_app.logger.debug(body)
        result = device_controller.get(self, g)
        return result, 200, None

    def post(self, body=None):
        current_app.logger.debug(body)
        result = device_controller.insert(self)
        return result, 200, None

    def put(self, body=None):
        current_app.logger.debug(body)
        result = device_controller.update(self)
        return result, 200, None