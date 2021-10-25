# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app

from . import Resource
from .. import schemas

from v1.controllers import devices_controller

class Devices(Resource):

    def get(self):
        current_app.logger.debug(self)
        result = devices_controller.get(self)
        return result, 200, None
