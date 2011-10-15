#!/usr/bin/python
#
#
# ./addHacker.py --host ldap://localhost --bindDN "cn=root,cn=visp" --password interlock --button 7C000012FF852001
#
#
from irocldap import IRocLDAP
import argparse


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--host', dest='host', required=True)
	parser.add_argument('--bindDN', dest='bindDN', required=True)
	parser.add_argument('--password', dest='password', required=True)

	parser.add_argument('--uid', dest='uid', required=True)
	parser.add_argument('--name', dest='name', required=True)
	parser.add_argument('--address', dest='address', required=True)
	parser.add_argument('--alias', dest='alias', required=True)
	parser.add_argument('--econtact', dest='econtact', required=True)
	parser.add_argument('--status', dest='status', required=True)
	parser.add_argument('--level', dest='level', required=True)

	parser.add_argument('-v', dest='verbose', action='store_true')

	args = parser.parse_args()

	host     = args.host
	bindDN   = args.bindDN
	password = args.password

	uid      = args.uid
	name     = args.name
	address  = args.address
	alias    = args.alias
	econtact = args.econtact
	status   = args.status
	level    = args.level

	iRocLdap = IRocLDAP(host, bindDN, password)

	status = iRocLdap.addHacker( uid, name, address, alias, econtact, status, level )



if __name__ == '__main__':
		main()



