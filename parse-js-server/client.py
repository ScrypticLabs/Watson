#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi Gupta
# @Date:   2015-06-09 20:13:01
# @Last Modified by:   Abhi
# @Last Modified time: 2018-01-17 20:59:14

import json,httplib

class Messages:
	def __init__(self):
		"""Connects to the server"""
		self.connection = httplib.HTTPSConnection('api.parse.com', 443)
		self.connection.connect()

	def SMS(self, number, message, WatsonNumber):
		"""Sends a SMS to the specified phone number"""
		# parameters go in the json.dumps
		self.connection.request('POST', '/1/functions/inviteWithTwilio', json.dumps({"plan": "paid", "number": str(number), "message": str(message), "WatsonNumber":str(WatsonNumber)}), {
		       "X-Parse-Application-Id": "viNLvbxfYcOE0PL7VtwjUUptkDx60lnxcs24VR8U",
		       "X-Parse-REST-API-Key": "fxNz8ImcDOvmwm88snWe0flHvB1iD3QYWtLQ3wJ2",
		       "Content-Type": "application/json"
		     })
		result = json.loads(self.connection.getresponse().read())
		print(result)	

	def sendMessage(self, number, message, WatsonNumber, spam = False):
		if spam:
			while True:
				self.SMS(number, message, WatsonNumber)
		else:
			self.SMS(number, message, WatsonNumber)

messages = Messages()

# Single Service - 5067990324
# Two Parties - 2892747953

messages.sendMessage(2262463034, "Good morning!", 5067990324, True)
