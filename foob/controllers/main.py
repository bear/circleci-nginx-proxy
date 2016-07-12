# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

from flask import Blueprint, current_app, request, redirect, render_template, jsonify


main = Blueprint('main', __name__)


@main.route('/', methods=['GET',])
def indexPage():
    templateContext = {}
    return render_template('index.jinja', **templateContext)
