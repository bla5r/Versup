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

from gpapi.googleplay import GooglePlayAPI, RequestError, LoginError
from Logger import Logger
from Configuration import Configuration

import os

class GPWrapper:
	def __init__(self, emailAddress, password):
		self.server = GooglePlayAPI()
		self.emailAddress = emailAddress
		self.password = password
		self.connected = False

	def load(self):
		return(self._connection())

	def _connection(self):
		try:
			self.server.login(self.emailAddress, self.password, None, None)
			self.connected = True
			return(False)
		except LoginError:
			Logger.error("Unable to connect Google Play: Bad credentials")
			return(True)

	def getVersion(self, id):
		if self.connected:
			try:
				details = self.server.details(id)
				return(str(details["versionCode"]))
			except RequestError:
				Logger.warning("Unable to get the %s version" % (id))
		return(None)

	def download(self, id, version):
		if self.connected:
			directory = "apk/%s" % (id)
			if not os.path.exists(directory):
				os.makedirs(directory)
			try:
				Logger.info("Downloading %s version %s..." % (id, version))
				apk = self.server.download(id, int(version))
				with open("%s/%s-%s.apk" % (directory, id, version), "wb") as file:
					file.write(apk["data"])
					Logger.info("Download finished")
			except RequestError:
				Logger.warning("Unable to download %s version %s" % (id, version))
