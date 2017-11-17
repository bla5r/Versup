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

from commands.StartCommand import StartCommand
from commands.StatusCommand import StatusCommand
from commands.PingCommand import PingCommand
from commands.VersionCommand import VersionCommand
from commands.FollowCommand import FollowCommand
from commands.UnfollowCommand import UnfollowCommand

class Command:
	@staticmethod
	def start(bot, update, job_queue, chat_data):
		cmd = StartCommand()
		cmd.run(bot, update, job_queue, chat_data)

	@staticmethod
	def ping(bot, update):
		cmd = PingCommand()
		cmd.run(bot, update)

	@staticmethod
	def unfollow(bot, update, args, chat_data):
		cmd = UnfollowCommand()
		cmd.run(bot, update, args, chat_data)

	@staticmethod
	def follow(bot, update, args, chat_data):
		cmd = FollowCommand()
		cmd.run(bot, update, args, chat_data)

	@staticmethod
	def version(bot, update, args, chat_data):
		cmd = VersionCommand()
		cmd.run(bot, update, args, chat_data)

	@staticmethod
	def status(bot, update, chat_data):
		cmd = StatusCommand()
		cmd.run(bot, update, chat_data)