#
#
#
#

from socket import *
import thread
from threading import Thread
import ldap
import time
from locklogger import LockLogger
from irocldap import IRocLDAP
from struct import unpack
from binascii import *


class UDPListener(Thread):

	max_packet_size = 8
	
	def __init__(self, listenSettings, ldapInfo, logger ):
		Thread.__init__(self)
		self.listenSettings = listenSettings
		self.host = listenSettings['host']
		self.port = listenSettings['port']
		self.ldapInfo = ldapInfo

		self.logger = logger
		
		self.logger.log("lock server initialized...")		


	def run(self):

		bAddr = ( self.host, self.port )

		self.serversock = socket(AF_INET, SOCK_DGRAM)
		self.serversock.bind(bAddr)

		while 1:

			try:
				self.logger.log("waiting for connection")
				data, cAddr = self.serversock.recvfrom(self.max_packet_size)
				self.logger.log("New connection from: %s" % (cAddr,))
				if ( len(data) != 8 ): 
					self.logger.log("Data size was not 8, bailing");
					continue;
			

				ldap = IRocLDAP( self.ldapInfo['host'], self.ldapInfo['bindDN'], self.ldapInfo['password'] )

				print len(data)
#				data = unpack('hhhh', data)
				print hexlify(data)
				data = data.encode('hex')
				print data
				status = ldap.getButtonState( data )
				print status
				self.serversock.sendto( status , cAddr )

			except	e:
				self.logger.log(e);
		








