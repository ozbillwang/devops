# Python Code Examples

This will guide you through the steps necessary to set up credentials and start playing with the sample code.  Note that once you've set up credentials for one language, you don't need to re-create them for another language.  If you set up the credentials for python, php will use the same credentials.

These instructions expect that you are in the examples/python subdirectory of the github repository.

# Authentication and Provisioning
The easiest way to walk through the needed provisioning and authentication to get your credentials is by following the instructions on [Authorizing your Client](https://developer.akamai.com/introduction/Prov_Creds.html) from the Getting started guide on our site.  Once you have done this, you'll be able to run the 'diagnostic tools' example scripts.

## Credential File Creation
You can get your credentials set up for use by the sample code by using the gen_edgerc.py command in the examples/python directory:
```bash
$ ./gen_edgerc.py
``` 

When you run gen_edgerc.py with no command line options, the script will create a 'default' section in your ~/.edgerc file.  For examples other than diagnostic_tools.py you'll need to pass the name of the appropriate section as an
argument, for example this is how you'd set up ccu.py:
```bash
./gen_edgerc.py ccu
```

You can find the correct name for the credentials section on the "section=" line in the example script.  If you run the script again for a specific section (including 'default') it will overwrite the previous credentials with your new ones.

## Diagnostic Tools - diagnostic_tools.py
The first example code to test is the diagnostic_tools.py script.  The credentials from the creation step give you permission to run the "dig" command from the API.

``` bash
./diagnostic_tools.py
```

This simple script runs the 'locations' call to find out where the Akamai servers are located.  The API can run the 'dig' for you from any of these locations.  Once it has done that, it grabs one at random and makes the dig call from there.

By reviewing the code you can see how simple it is to make API calls.

All of the sample code in the directory also supports --verbose to see the output on the screen, and/or --debug to see all of the HTTP traffic.  These flags can help enormously in figuring out what's going wrong or how it's working.

``` bash
./diagnostic_tools.py --verbose
./diagnostic_tools.py --debug
```

## CCU (Purge) - ccu.py
We have a [blog post](https://community.akamai.com/community/developer/blog/2015/08/20/getting-started-with-the-v2-open-ccu-api) with instructions on getting set up with the CCU API.
Prerequisites: ccu credentials and edit the filename to a valid file on your system

