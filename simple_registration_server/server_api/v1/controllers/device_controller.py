# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import current_app, g
from flask_restful import abort

from werkzeug.local import LocalProxy
import json

# Use LocalProxy to read the global db instance with just `db`
from .db_util import get_db
db = LocalProxy(get_db)

def get(device, deviceId="DeviceID"):
    current_app.logger.info("get device")
    current_app.logger.debug(device)
    result = db.devices.find_one({"DeviceID": deviceId}, {'_id': False})
    current_app.logger.debug(result)
    return result

def insert(device):
    deviceId = g.json["DeviceID"]
    current_app.logger.info("insert device")
    if db.devices.find_one({"DeviceID": deviceId}, {'_id': False}) is not None:
        abort(400, message='Devcice already exists')
    x = db.devices.insert_one(g.json)
    current_app.logger.debug(x)
    return "Document with deviceId {0} inserted".format(deviceId)

def update(device):
    deviceId = g.json["DeviceID"]
    current_app.logger.info("update device")
    current_app.logger.debug(deviceId)
    x = db.devices.find_one_and_update(
        { 'DeviceID': deviceId },
        { '$set'    : g.json   }, upsert=True
    )
    current_app.logger.debug(x)
    return "Document with deviceId {0} updated".format(deviceId)
