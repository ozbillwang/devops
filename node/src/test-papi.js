#! /usr/bin/env node

/**
Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at 

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

========================================================================

Example of using the Akamai OPEN CCU V3 (Fast Purge) API

Note: in order for this to work you need to provision credentials
specifically for CCU - you cannot extend existing credentials to add
CCU as it's managed under "CCU" in the API credential system.

Configure->Organization->Manage APIs
Select "CCU APIs"
Create client collections/clients
Add authorization

Put the credentials in ~/.edgerc as demonstrated by api-kickstart/sample_edgerc
*/

path = require('path'),
    os = require('os'),
    prettyJSON = require('prettyjson'),
    logger = require('./logger'),
    argv = require('minimist')(process.argv.slice(2));

// Akamai EdgeGrid signing library
var EdgeGrid = require('edgegrid');

// Optional command-line arguments
var debug = argv.debug ? true : false;
var verbose = argv.verbose ? true : false;
var headers = argv.headers ? argv.headers : {};

// The result data returned by the purge POST request
var purgePostResult;

// The path to the .edgerc file to use for authentication
var edgercPath = path.join(os.homedir(), "/.edgerc");

// The section of the .edgerc file to use for authentication
var sectionName = "au";

// Create a new instance of the EdgeGrid signing library
var eg = new EdgeGrid({
    path: edgercPath,
    section: sectionName,
    debug: true
});

/**
 * Adds item to be invalidated.
 */
function invalidate() {
    eg.auth({
        path: "/papi/v0/properties/prp_368018/versions/17/hostnames/?contractId=ctr_3-1A42HS1&groupId=grp_53736",
        method: "GET",
        headers: { 'Content-Type': 'application/json' },
    });

    eg.send(function(data, response) {
	console.log("Response: ", response);
        data = JSON.parse(data);
        console.log("Data: ", data);
    });
}

invalidate();
