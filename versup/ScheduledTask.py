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

from telegram.ext import Updater, CommandHandler
import telegram

from User import User
from Database import Database
from GPWrapper import GPWrapper
from Logger import Logger

import time

class ScheduledTask:
	@staticmethod
	def _getData(context):
		return(context[0], context[1], context[2])

	@staticmethod
	def _checkVersion(bot, chat_id, app, db, gp):
		version = gp.getVersion(app[1])
		if version == None:
			Logger.warning("Unable to retrieve the current version of %s" % (app[1]))
		else:
			if version != app[2]:
				Logger.info("New version of %s (%s)" % (app[1], version))
				User.reply(bot, chat_id, "I spot a new release of <i>%s</i>: <b>%s</b> to <b>%s</b>" % (app[1], app[2], version))
				db.update(app[1], version)
				gp.download(app[1], version)
			else:
				Logger.info("%s is still in version %s" % (app[1], app[2]))
		time.sleep(5)

	@staticmethod
	def run(bot, job):
		chat_id, db, gp = ScheduledTask._getData(job.context)
		apps = db.fetch()
		Logger.info("Trying to find new release into %d app(s)..." % (len(apps)))
		for app in apps:
			ScheduledTask._checkVersion(bot, chat_id, app, db, gp)
