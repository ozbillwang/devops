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
import requests, logging, json, sys, os
from http_calls import EdgeGridHttpCaller
from random import randint
from akamai.edgegrid import EdgeGridAuth,EdgeRc
from config import EdgeGridConfig
import urllib
import argparse
import logging
section_name="default"
debug = False
verbose = False
session = requests.Session()

# If all parameters are set already, use them.  Otherwise
# use the config
config = EdgeGridConfig({"verbose":False},section_name)

if hasattr(config, "debug") and config.debug:
	debug = True

if hasattr(config, "verbose") and config.verbose:
	verbose = True


# Set the config options
session.auth = EdgeGridAuth(
            client_token=config.client_token,
            client_secret=config.client_secret,
            access_token=config.access_token
)

if hasattr(config, 'headers'):
	session.headers.update(config.headers)

baseurl = '%s://%s/' % ('https', config.host)
httpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl)


# Request locations that support the diagnostic-tools
print
print ("Requesting locations that support the diagnostic-tools API.\n")

location_result = httpCaller.getResult('/diagnostic-tools/v2/ghost-locations/available')

# Select a random location to host our request
location_count = len(location_result['locations'])

print("There are {} locations that can run dig in the Akamai Network".format(location_count))
rand_location = randint(0, location_count-1)
#location = location_result['locations'][rand_location]['id']
location = "sanjose-ca-unitedstates"
print ("We will make our call from " + location + "\n")

# Request the dig request the {OPEN} Developer Site IP information
dig_parameters = { "hostName":"developer.akamai.com"}
dig_result = httpCaller.getResult("/diagnostic-tools/v2/ghost-locations/%s/dig-info" % location,dig_parameters)

# Display the results from dig
print (dig_result['digInfo']['result'])
