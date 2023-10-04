# -*- coding: utf-8 -*-
"""
    protected_route.views
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains the views for the
    protected_route Plugin.

    :copyright: (c) 2023 by Paul Cunningham.
    :license: MIT License, see LICENSE for more details.
"""
from flask import Blueprint, flash
from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry


protected_route_bp = Blueprint("protected_route_bp", __name__, template_folder="templates")


@protected_route_bp.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="protected_route").first()
    if plugin and not plugin.is_installed:
        flash(_("Plugin is not installed."), "warning")

    return render_template("index.html", plugin=plugin)
