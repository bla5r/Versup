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

from Database import Database

class Chat:
	@staticmethod
	def getStatus(db):
		apps = db.fetch()
		tmp = ""
		for i in range(0, len(apps)):
			if i != 0:
				tmp += ", "
			tmp += "<i>%s</i> (<b>%s</b>)" % (apps[i][1], apps[i][2])
		if tmp == "":
			return("I'm not following any app.")
		return("I'm following: %s." % tmp)

	@staticmethod
	def isInit(chat_data):
		try:
			chat_data["init"]
			return(True)
		except:
			return(False)
