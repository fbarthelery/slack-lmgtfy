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
Default configuration for Slack-lmgtfy application.
"""

# classical flask configuration option
TRAP_HTTP_EXCEPTIONS = True
TRAP_BAD_REQUEST_ERRORS = True
# app secret key : change it
SECRET_KEY = "myrandomsecretkey"

SERVER_NAME = "localhost:5000"

# Slack incoming webhook url
SLACK_WEBHOOK_URL = "http://localhost:4000"


