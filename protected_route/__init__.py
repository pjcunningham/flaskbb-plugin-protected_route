# -*- coding: utf-8 -*-
"""
    protected_route
    ~~~~~~~~~~~~~~~

    A protected_route Plugin for FlaskBB.

    :copyright: (c) 2023 by Paul Cunningham.
    :license: MIT License, see LICENSE for more details.
"""
import os

from flask import current_app, request
from flask_login import current_user

from pluggy import HookimplMarker

from flaskbb.forum.models import Forum
from flaskbb.utils.forms import SettingValueType
from flaskbb.utils.helpers import render_template


from .views import protected_route_bp

__version__ = "0.1.0"


hookimpl = HookimplMarker("flaskbb")


# connect the hooks
@hookimpl
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app):
    app.register_blueprint(protected_route_bp, url_prefix="/protected_route")


@hookimpl
def flaskbb_tpl_before_navigation():
    return render_template("protected_route_navlink.html")


allowed_endpoints = (
    'static',
    '_themes.static',
    'auth.login',
)


@hookimpl
def flaskbb_request_processors(app):
    """Apply the login restriction."""

    @app.before_request
    def before_request():
        """Check authentication before request is handled."""

        if (request.endpoint not in allowed_endpoints and not current_user.is_authenticated):
            return current_app.login_manager.unauthorized()
