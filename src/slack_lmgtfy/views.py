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
    Views of the Slack-lmgtfy application.
    It contains the differente url route for the application.
"""

from flask import Blueprint, request, current_app
from slack_lmgtfy.slack import IncomingMessage, send_message, SlackError
from urllib.parse import urlencode

bp = Blueprint("main", __name__)   # pylint: disable=invalid-name


@bp.route("/lmgtfy", methods=["GET", "POST"])
def cmd_hook():
    """ Hook for Slack command /lmgtfy that send back a link in the channel. """
    channel = request.values["channel_name"]
    text = request.values["text"]
    if not text:
        return "You need to add some search parameters", 500
    lmgtfy_url = get_lmgtfy_url(text)
    message = IncomingMessage()
    message_text = "Hey! Check this <" + lmgtfy_url + "|interesting link!>"
    message.set_text(message_text)
    message.set_channel(channel)
    webhook_url = current_app.config["SLACK_WEBHOOK_URL"]
    try:
        send_message(message, webhook_url)
        return ""
    except SlackError:
        return "Unable to send link to slack channel", 500


def get_lmgtfy_url(text):
    data = {}
    data["q"] = text
    return "http://lmgtfy.com/" + urlencode(data)

