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
import sys

from Configuration import Configuration
from Command import Command
from Logger import Logger
from Database import Database

class VersupBot:
	def __init__(self):
		self._printBanner()
		Logger.info("Initializing bot...")
		config = self._loadConfiguration()
		self.updater = Updater(config.getBotToken())
		self.dp = self.updater.dispatcher

	def _printBanner(self):
		with open('./.banner', "r") as file:
			print(file.read())

	def _loadConfiguration(self):
		Logger.info("Parsing configuration file...")
		config = Configuration()
		if config.load() == True:
			Logger.error("Critical error during the loading of the configuration file. Exiting...")
			sys.exit(1)
		return (config)

	def register(self):
		Logger.info("Registering commands...")
		self.dp.add_handler(CommandHandler("start", Command.start, pass_job_queue=True, pass_chat_data=True))
		self.dp.add_handler(CommandHandler("status", Command.status, pass_chat_data=True))
		self.dp.add_handler(CommandHandler("ping", Command.ping))
		self.dp.add_handler(CommandHandler("follow", Command.follow, pass_args=True, pass_chat_data=True))
		self.dp.add_handler(CommandHandler("unfollow", Command.unfollow, pass_args=True, pass_chat_data=True))
		self.dp.add_handler(CommandHandler("version", Command.version, pass_args=True, pass_chat_data=True))

	def run(self):
		Logger.info("Starting polling...")
		self.dp.add_error_handler(Logger.telegramError)
		self.updater.start_polling()
		Logger.info("VersupBot is waiting for incoming commands")
		self.updater.idle()
