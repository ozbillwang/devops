#! /usr/bin/env python
# Very basic script demonstrating diagnostic tools functionality
#
""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at 

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import requests, logging, json, sys
from akamai.edgegrid import EdgeGridAuth
session = requests.Session()
section_name = "alerts"
import os

if sys.version_info[0] >= 3:
     # python3
     from urllib import parse
else:
     # python2.7
     import urlparse as parse


env_prefix = '_'.join(['AKAMAI',section_name.upper()])
env = {}
for token in ('CLIENT_TOKEN','CLIENT_SECRET','ACCESS_TOKEN','HOST'):
	env_string = '_'.join([env_prefix, token])
	if env_string not in os.environ:
		print "Need to set environment variables: %s" % env_string
		continue
	env[token] = os.environ[env_string]

if len(env) < 4:
	exit(0)

# Set the config options
session.auth = EdgeGridAuth(
            client_token=env['CLIENT_TOKEN'],
            client_secret=env['CLIENT_SECRET'],
            access_token=env['ACCESS_TOKEN']
)

baseurl = '%s://%s/' % ('https', env['HOST'])

alert_result = session.get(parse.urljoin(baseurl,'/alerts/v2/alert-definitions'))
print alert_result.json()

