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

from ..Configuration import Configuration
from ..Database import Database
from ..GPWrapper import GPWrapper
from ..Chat import Chat
from ..User import User
from ..ScheduledTask import ScheduledTask
from ..Logger import Logger

class StartCommand:
	def _removeJobs(self, jobs):
		for job in jobs:
			job.schedule_removal()

	def _sendStatus(self, bot, chat_id, db):
		User.reply(bot, chat_id, "What's up mate?")
		User.reply(bot, chat_id, Chat.getStatus(db))

	def _scheduleTask(self, job_queue, chat_id, config, db, gp):
		Logger.info("Checking new available version for each app every %d minute(s)" % (config.getRefreshRate()))
		job_queue.run_repeating(ScheduledTask.run, interval=(config.getRefreshRate() * 60), first=0, context=(chat_id, db, gp))

	def _loadConfiguration(self, chat_data):
		try:
			chat_data["config"]
		except KeyError:
			chat_data["config"] = Configuration()
			chat_data["config"].load()
			# Exit if return True

	def _loadDatabase(self, chat_data):
		try:
			chat_data["db"]
		except KeyError:
			chat_data["db"] = Database()
			chat_data["db"].load()
			# Exit if return True

	def _loadGpWrapper(self, chat_data):
		try:
			chat_data["gp"]
		except KeyError:
			chat_data["gp"] = GPWrapper(chat_data["config"].getEmailAddress(), chat_data["config"].getPassword())
			chat_data["gp"].load()
			# Exit if return True

	def _loadComplete(self, chat_data):
		chat_data["init"] = True

	def run(self, bot, update, job_queue, chat_data):
		self._removeJobs(job_queue.jobs())
		self._loadConfiguration(chat_data)
		self._loadDatabase(chat_data)
		self._loadGpWrapper(chat_data)
		self._loadComplete(chat_data)
		self._sendStatus(bot, update.message.chat_id, chat_data["db"])
		Logger.info("Service starting by @%s..." % (update.message.chat.username))
		self._scheduleTask(job_queue, update.message.chat_id, chat_data["config"], chat_data["db"], chat_data["gp"])