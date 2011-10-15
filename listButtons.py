#!/usr/bin/python
#
#
# ./listButtons.py
#
#
from irocldap import IRocLDAP
import argparse
import yaml

def main():

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	toolConfig = config['tool']

	host     = toolConfig['host']
	bindDN   = toolConfig['bindDN']
	password = toolConfig['password']


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



