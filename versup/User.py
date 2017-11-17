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

class User:
	@staticmethod
	def reply(bot, chat_id, text):
		bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

	@staticmethod
	def notLogged(bot, chat_id):
		User.reply(bot, chat_id, "I'm not running. Please send /start before.")