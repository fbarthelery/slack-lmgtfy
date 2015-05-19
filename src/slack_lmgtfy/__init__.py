#!/bin/env python
#
#  Slack-lgmtfy is a Slack hook to integrate http://www.lmgtfy.com in Slack
#
#  Copyright (C) 2015 by Frederic-Charles Barthelery.
#
#  This file is part of Slack-lmgtfy.
#
#  Slack-lmgtfy is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Slack-lmgtfy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Slack-lmgtfy.  If not, see <http://www.gnu.org/licenses/>.
#
#  Please send bug reports with examples or suggestions to
#  contact@geekorum.com.
#
#

"""
Main module of Slack-lmgtfy application.
It allows to create the web application and configure it.
"""

from flask import Flask


def create_app(instance_path=None):
    """
    Create the Slack-lmgtfy application.

    @param instance_path the instance path of the web application. See Flask doc for more info
    @return the Slack-lmgtfy flask application
    """
    if instance_path:
        app = Flask("slack_lmgtfy", instance_path=instance_path, instance_relative_config=True)
    else:
        app = Flask("slack_lmgtfy", instance_relative_config=True)

    app.config.from_object("slack_lmgtfy.default_config")
    app.config.from_pyfile("config.ini")

    from slack_lmgtfy.views import bp
    app.register_blueprint(bp)
    return app


def create_test_app():
    """
    Create the Slack-lmgtfy application.

    @param instance_path the instance path of the web application. See Flask doc for more info
    @return the Slack-lmgtfy flask application
    """
    app = Flask("slack_lmgtfy")
    app.config["TESTING"] = True
    app.config.from_object("slack_lmgtfy.default_config")

    from slack_lmgtfy.views import bp
    app.register_blueprint(bp)
    return app
