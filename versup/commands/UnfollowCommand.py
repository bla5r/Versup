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

class UnfollowCommand:
	def _unfollow(self, bot, update, args, db):
		try:
			id = args[0]
			if db.exists(id):
				Logger.info("Unfollowing %s..." % (id))
				db.remove(id)
				User.reply(bot, update.message.chat_id, "OK, I don't follow <i>%s</i> anymore." % (id))
			else:
				User.reply(bot, update.message.chat_id, "Sorry, I don't follow this app.")
		except IndexError:
			User.reply(bot, update.message.chat_id, "Hey mate, give me the app ID.")

	def _notRunning(self, bot, chat_id):
		User.notLogged(bot, chat_id)

	def run(self, bot, update, args, chat_data):
		if Chat.isInit(chat_data):
			self._unfollow(bot, update, args, chat_data["db"])
		else:
			self._notRunning(bot, update.message.chat_id)