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

from Logger import Logger

import json

class Configuration:
	def __init__(self):
		self.filename = "config.json"
		self.json = None
		self.emailAddress = None
		self.password = None
		self.botToken = None
		self.refreshRate = None

	def _create(self):
		try:
			file = open(self.filename, "r")
			content = file.read()
			file.close()
			self.json = json.loads(content)
			return(False)
		except IOError:
			Logger.error("%s: No such file" % (self.filename))
			return(True)
		except ValueError:
			Logger.error("%s: Invalid JSON format" % (self.filename))
			return(True)

	def _parse(self):
		try:
			self.emailAddress = self.json["emailAddress"]
			self.password = self.json["password"]
			self.botToken = self.json["botToken"]
			self.refreshRate = self.json["refreshRate"]
			return(False)
		except KeyError, e:
			Logger.error("%s: Unable to find the element %s" % (self.filename, e))
			return(True)

	def load(self):
		if self._create():
			return(True)
		if self._parse():
			return(True)
		return(False)

	def getEmailAddress(self):
		return(self.emailAddress)

	def getPassword(self):
		return(self.password)

	def getBotToken(self):
		return(self.botToken)

	def getRefreshRate(self):
		return(self.refreshRate)
