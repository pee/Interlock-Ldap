'''
'''
import ldap
import ldap.modlist as modlist
from ldap.cidict import cidict
import ldif
from StringIO import StringIO


class IRocLDAP():

		HACKER_BASE = 'ou=hackers, dc=interlockroc, dc=org, cn=visp'
		BUTTON_BASE = 'ou=iButtons, dc=interlockroc, dc=org, cn=visp'

		def	__init__(self, host, bindDN, password):
			self.host = host
			self.bindDN = bindDN
			self.password = password
#			try:
			conn = ldap.initialize( self.host )
			conn.simple_bind_s( self.bindDN, self.password )
#			except ldap.LDAPError, e:
#				print e
			self.conn = conn


		def	addButton( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == True:
				print "Button with ID " + buttonID + " already exists"
				return

			addDN = "uid=" + buttonID + "," + self.BUTTON_BASE

			attrs = {}
			attrs['objectclass'] = ['top','iLockButton']
			attrs['iLockRocButtonID'] = buttonID
			attrs['iLockRocButtonActive'] = 'FALSE'

			# turn it into ldif
			ldif = modlist.addModlist(attrs)

			# stuff it into the server
			self.conn.add_s(addDN,ldif)

			# print to screen
			self.dumpButton( buttonID )

		def addHacker( self, uid, name, address, alias, econtact, status, level ):

			self.validateUID(uid)
			self.validateName(name)
			self.validateAddress(address)
			self.validateAlias(alias)
			self.validateEContact(econtact)
			self.validateStatus(status)
			self.validateLevel(level)

			if self.hackerExists(uid) == True:
				print "Hacker with uid " + uid + " already exists"
				return
			
			addDN = "uid=" + uid + "," + self.HACKER_BASE

			attrs = {}
			attrs['objectclass'] = [ 'top', 'iLockRocUser']
			attrs['uid'] = uid
			attrs['iLockRocName'] = name
			attrs['iLockRocAddress'] = address
			attrs['iLockRocAlias'] = alias
			attrs['iLockRocEmergencyContact'] = econtact
			attrs['iLockRocMemberStatus'] = status
			attrs['iLockRocMemberLevel'] = level

			# turn it into ldif
			ldif = modlist.addModlist(attrs)

			# add to server
			self.conn.add_s( addDN, ldif )

			# print to screen
			self.dumpHacker( uid )

		def validateUID( self, uid ):
			''' '''
			print "not actually validating UID:" + uid

		def validateName( self, name ):
			''' '''
			print "not actually validating Name:" + name

		def validateAddress( self, address ):
			''' '''
			print "not actually validating Address:" + address

		def validateAlias( self, alias ):
			''' '''
			print "not actually validating Alias:" + alias

		def validateEContact( self, econtact ):
			''' '''
			print "not actually validating EContact:" + econtact

		def validateStatus( self, status ):
			''' '''
			print "not actually validating Status:" + status

		def validateLevel( self, level):
			''' '''
			print "not actually validating Level:" + level
							
		def delButton( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == False:
				print "Button with ID" + buttonID + " does not exist"
				return

			self.dumpButton( buttonID )
			# build the DN to delete
			delDN = "uid=" + buttonID + "," + self.BUTTON_BASE

			# delete it
			self.conn.delete_s(delDN)

		def delHacker( self, uid ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateUID( uid )

			if self.hackerExists( uid ) == False:
				print "Hacker with uid " + uid + " does not exist"
				return

			self.dumpHacker( uid )

			# build the DN to delete
			delDN = "uid=" + uid + "," + self.HACKER_BASE

			# delete it
			self.conn.delete_s(delDN)


		def setButtonStatus( self, buttonID, status ):
			print "setButtonStatus"


		def validateButtonID( self, buttonID ):
			print "########## validateButton(" + buttonID + ")"
			if len(buttonID) != 16:
				raise ValueError("ButtonID was of incorrect length")
			
		def dumpButton( self, buttonID ):

			results = self._getButton( buttonID )

			if len(results) == 0:
				print "WTF Bubblefuck..."
				return
				
			if type(results) == tuple and len(results) == 2 :
				(code, arr) = results
			elif type(results) == list:
				arr = results

			for item in arr:
				(dn, attrs) = item

			print "##########\n"

			out = StringIO()
			ldiffOut = ldif.LDIFWriter(out)
			ldiffOut.unparse( dn, attrs)

			print out.getvalue()
			print "##########\n"

		def dumpHacker( self, uid ):

			results = self.conn.search_s(self.HACKER_BASE, ldap.SCOPE_SUBTREE, "uid="+uid)

			if len(results) == 0:
				print "WTF Bubblefuck..."
				return
				
			if type(results) == tuple and len(results) == 2 :
				(code, arr) = results
			elif type(results) == list:
				arr = results

			for item in arr:
				(dn, attrs) = item

			print "##########\n"

			out = StringIO()
			ldiffOut = ldif.LDIFWriter(out)
			ldiffOut.unparse( dn, attrs)

			print out.getvalue()
			print "##########\n"


		def buttonExists( self, buttonID):

			results = self._getButton( buttonID )

			# no idea if this is correct ;)
			if len(results) == 0:
				return False
			else:
				return True

		def hackerExists( self, uid):

			results = self._getHacker( uid )

			# no idea if this is correct ;)
			if len(results) == 0:
				return False
			else:
				return True

		def _getButton( self, buttonID ):
			return self.conn.search_s( self.BUTTON_BASE, ldap.SCOPE_SUBTREE, "iLockRocButtonID="+buttonID )

		def getButtons( self ):
			return self.conn.search_s( self.BUTTON_BASE, ldap.SCOPE_SUBTREE, "uid=*" )

		def _getHacker( self, uid ):
			return self.conn.search_s( self.HACKER_BASE, ldap.SCOPE_SUBTREE, "uid="+uid )


		def	enableButton( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == False:
				print "Button with ID " + buttonID + " does not exist"
				return

			self._setButtonState( buttonID, "TRUE", "FALSE" )

			# print to screen
			self.dumpButton( buttonID )

		def	disableButton( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == False:
				print "Button with ID " + buttonID + " does not exist"
				return

			self._setButtonState( buttonID, "FALSE", "TRUE" )

			# print to screen
			self.dumpButton( buttonID )

		def _setButtonState( self, buttonID, state, oldState):

			modDN = "uid=" + buttonID + "," + self.BUTTON_BASE

			oldAttr = {}
			oldAttr['iLockRocButtonActive'] = oldState

			attrs = {}
			attrs['iLockRocButtonActive'] = state

			# turn it into ldif
			ldif = modlist.modifyModlist( oldAttr , attrs )

			# stuff it into the server
			self.conn.modify_s( modDN,ldif )


		def getButtonState( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == False:
				print "Button with ID " + buttonID + " does not exist"
				# "False" as in active, not false as in the truth valise
				# maybe we should change this
				return "False"

			results = self._getButton( buttonID )

			state = self._getState( results, buttonID )

			return state


		def _getState( self, results, buttonID ):

			if type(results) == tuple and len(results) == 2 :
				(code, arr) = results
			elif type(results) == list:
				arr = results

			if len(arr) != 1:
				raise ValueError("Too many returns from search for buttonID for ID " + buttonID )

			(dn, attrs) = arr[0]

			return attrs['iLockRocButtonActive'][0]

		def getButtonUserDN( self, buttonID ):

			#
			# Real men would regexp check the button id right about here and explode
			#
			self.validateButtonID(buttonID)

			if self.buttonExists(buttonID) == False:
				print "Button with ID " + buttonID + " does not exist"
				return

			results = self._getButton( buttonID )

			hackerDN = self._getButtonUserDN( results, buttonID )

			return hackerDN


		def _getButtonUserDN( self, results, buttonID ):

			if type(results) == tuple and len(results) == 2 :
				(code, arr) = results
			elif type(results) == list:
				arr = results

			if len(arr) != 1:
				raise ValueError("Too many returns from search for buttonID for ID " + buttonID )

			(dn, attrs) = arr[0]
			if 'iLockRocUserDN' in attrs:
				hackerDN = attrs['iLockRocUserDN'][0]
			else:
				hackerDN = "Undef"

			return hackerDN



		def linkButtonToUid( self, buttonID, uid ):

			self.validateButtonID( buttonID )
			self.validateUID( uid )

			if self.buttonExists( buttonID ) == False:
				print "Button with ID " + buttonID + " does not exist"
				return

			if self.hackerExists(uid) == False:
				print "Hacker with uid " + uid + " does not exist"
				return
			
			hStatus = self._getHacker( uid )
			(dn, attrs) = hStatus[0]
			# iLockRocUserDN

			oldAttr = {}
			oldDN = self.getButtonUserDN( buttonID )
			print "oldDN:" + oldDN
			if oldDN is "Undef":
				print "oldDN is none"
				attrs = {}
				attrs['iLockRocUserDN'] = dn
				ldif = modlist.modifyModlist(oldAttr, attrs)
				modDN = "uid=" + buttonID + "," + self.BUTTON_BASE
				self.conn.modify_s( modDN,ldif )
				self.dumpButton( buttonID )

			else:
				oldAttr['iLockRocUserDN'] = oldDN
				attrs = {}
				attrs['iLockRocUserDN'] = dn

				# turn it into ldif
				ldif = modlist.modifyModlist( oldAttr , attrs )

				# stuff it into the server
				modDN = "uid=" + buttonID + "," + self.BUTTON_BASE
				self.conn.modify_s( modDN,ldif )

				self.dumpButton( buttonID )

'''







'''
