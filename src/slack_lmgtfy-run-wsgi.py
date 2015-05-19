#!/usr/bin/python
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

from slack_lmgtfy import create_app

application = create_app()

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/slack_lmgtfy'
        return self.app(environ, start_response)

application.wsgi_app = WebFactionMiddleware(application.wsgi_app)

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)


