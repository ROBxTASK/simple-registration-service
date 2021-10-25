# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Version(Resource):

    def get(self):

        return {"serviceId": "simple-registration-service", "version" : "1.0.0"}, 200, None