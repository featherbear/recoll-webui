#!/usr/bin/env python3
import os
import argparse
import webui

# handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='127.0.0.1',help='address to bind to [127.0.0.1]')
parser.add_argument('-p', '--port', default='8080', type=int, help='port to listen on [8080]')
parser.add_argument('-c', '--config', default=None, type=str, help='configuration directory')
args = parser.parse_args()

if args.config:
    os.environ["RECOLL_CONFDIR"] = args.config

# change to webui's directory and import
if os.path.dirname(__file__) != "":
    os.chdir(os.path.dirname(__file__))

# set up webui and run in own http server
webui.bottle.debug(True)
webui.bottle.run(server='waitress', host=args.addr, port=args.port)

# vim: foldmethod=marker:filetype=python:textwidth=80:ts=4:et
