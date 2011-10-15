#!/usr/bin/python
#
#
# ./listButtons.py --host ldap://localhost --bindDN "cn=root,cn=visp" --password interlock 
#
#
from irocldap import IRocLDAP
import argparse


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--host', dest='host', required=True)
	parser.add_argument('--bindDN', dest='bindDN', required=True)
	parser.add_argument('--password', dest='password', required=True)
	args = parser.parse_args()

	host     = args.host
	bindDN   = args.bindDN
	password = args.password

	iRocLdap = IRocLDAP(host, bindDN, password)

	results = iRocLdap.getButtons( )

	if type(results) == tuple and len(results) == 2 :
		(code, arr) = results
	elif type(results) == list:
		arr = results

	for item in arr:
		(dn, attrs) = item
		uid = attrs['uid'][0]
		status = attrs['iLockRocButtonActive'][0]
		if 'iLockRocUserDN' in attrs:
			hackerDN = attrs['iLockRocUserDN'][0]
		else:
			hackerDN = "Undef"

		print "UID: %s Active: %s HackerDN: %s" % ( uid, status, hackerDN )
		





if __name__ == '__main__':
		main()



