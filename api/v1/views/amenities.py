#!/usr/bin/python3
""" New view for amenities model """

from flask import abort, jsonify, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity



