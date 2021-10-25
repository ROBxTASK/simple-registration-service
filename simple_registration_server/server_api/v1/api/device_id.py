# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app, g

from . import Resource
from .. import schemas

from v1.controllers import device_controller

class DeviceId(Resource):

    def get(self, id):
        current_app.logger.debug(id)
        result = device_controller.get(self, g, deviceId=id)
        return result, 200, None

