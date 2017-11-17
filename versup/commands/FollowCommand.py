#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Versup.
#
# Copyright(c) 2017 bla5r
# https://github.com/bla5r
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from ..User import User
from ..Chat import Chat
from ..Logger import Logger
from ..Database import Database
from ..GPWrapper import GPWrapper

class FollowCommand:
	def _getDetails(self, bot, update, args, gp):
		try:
			id = args[0]
		except IndexError:
			User.reply(bot, update.message.chat_id, "Hey mate, give me the app ID.")
			return(None, None)
		version = gp.getVersion(id)
		if version == None:
			User.reply(bot, update.message.chat_id, "Sorry, I'm unable to find the current version.")
			return(None, None)
		if int(version) == 0:
			User.reply(bot, update.message.chat_id, "Your GP account isn't allowed to access this app.")
			return(None, None)
		return(id, version)

	def _follow(self, bot, update, args, db, gp):
		id, version = self._getDetails(bot, update, args, gp)
		if version == None:
			return(None)
		if db.exists(id):
			User.reply(bot, update.message.chat_id, "I already follow this app.")
			return (None)
		Logger.info("Following %s (%s)..." % (id, version))
		db.add(id, version)
		gp.download(id, version)
		User.reply(bot, update.message.chat_id, ("OK, I'll often take a look at this app version. The current version is <b>%s</b>." % version))

	def _notRunning(self, bot, chat_id):
		User.notLogged(bot, chat_id)

	def run(self, bot, update, args, chat_data):
		if Chat.isInit(chat_data):
			self._follow(bot, update, args, chat_data["db"], chat_data["gp"])
		else:
			self._notRunning(bot, update.message.chat_id)