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

import sqlite3

class Database:
	def __init__(self):
		self.conn = None
		self.cur = None
		self.connected = False

	def load(self):
		return(self._connect())

	def __del__(self):
		self._disconnect()

	def _connect(self):
		try:
			self.conn = sqlite3.connect(".app.db", check_same_thread=False)
			self.cur = self.conn.cursor()
			self.cur.execute("CREATE TABLE IF NOT EXISTS apps (id INTEGER PRIMARY KEY AUTOINCREMENT, app_id CHAR(256) NOT NULL, version CHAR(32) NOT NULL)")
			self.connected = True
			return(False)
		except:
			Logger.error("Unable to connect database")
			return(True)

	def _disconnect(self):
		self.connected = False
		self.conn.close()

	def add(self, app_id, version):
		if self.connected:
			self.cur.execute("INSERT INTO apps (app_id, version) VALUES ('%s', '%s')" % (app_id, version))
			self.conn.commit()
		else:
			Logger.warning("Unable to insert item in database")

	def remove(self, app_id):
		if self.connected:
			self.cur.execute("DELETE FROM apps WHERE app_id = '%s'" % (app_id))
			self.conn.commit()
		else:
			Logger.warning("Unable to remove item in database")

	def update(self, app_id, version):
		if self.connected:
			self.cur.execute("UPDATE apps SET version = '%s' WHERE app_id = '%s'" % (version, app_id))
			self.conn.commit()
		else:
			Logger.warning("Unable to update item in database")

	def exists(self, app_id):
		if self.connected:
			self.cur.execute("SELECT * FROM apps WHERE app_id = '%s'" % (app_id))
			rows = self.cur.fetchall()
			return(True if len(rows) != 0 else False)
		else:
			Logger.warning("Unable to access item in database")
			return(False)

	def fetch(self):
		if self.connected:
			result = []
			self.cur.execute("SELECT * FROM apps")
			rows = self.cur.fetchall()
			for row in rows:
				result.append(row)
			return(result)
		else:
			Logger.warning("Unable to fetch items in database")
			return(None)
