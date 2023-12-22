#!/usr/bin/python3
""" New view for amenities model """

from flask import abort, jsonify, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


def recup_all_amenities():
    all_amenities = []
    for value in storage.all(Amenity).values():
        all_amenities.append(value.to_dict())
    return all_amenities


