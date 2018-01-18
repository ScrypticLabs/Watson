#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-06-11 14:34:24
# @Last Modified by:   Abhi Gupta
# @Last Modified time: 2015-11-20 01:31:43

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/functions/receiveSMS', json.dumps({}), {
       "X-Parse-Application-Id": "viNLvbxfYcOE0PL7VtwjUUptkDx60lnxcs24VR8U",
       "X-Parse-REST-API-Key": "fxNz8ImcDOvmwm88snWe0flHvB1iD3QYWtLQ3wJ2",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result
