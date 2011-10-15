#!/usr/bin/python
#
#
#
import sys
import time
import yaml
from socket import *
import SocketServer
from locklogger import LockLogger
from udplistener import UDPListener


if __name__ == '__main__':

	debug = sys.argv.count('-v')
	logger = LockLogger('/tmp/lockServer.log')
	logger.log("Server started")

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	print config
	ldapConfig = config['ldap']
	print ldapConfig
	listenConfig = config['listener']
	print listenConfig


	udpListener = UDPListener( listenConfig, ldapConfig, logger )

	udpListener.start()





