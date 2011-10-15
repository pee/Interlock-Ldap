#!/usr/bin/python
#
#
#
from irocldap import IRocLDAP
import argparse


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--host', dest='host', required=True)
	parser.add_argument('--bindDN', dest='bindDN', required=True)
	parser.add_argument('--password', dest='password', required=True)
	parser.add_argument('--button', dest='buttonID', help='the iButton ID', required=True)
	parser.add_argument('-v', dest='verbose', action='store_true')
	args = parser.parse_args()

	host     = args.host
	bindDN   = args.bindDN
	password = args.password
	buttonID = args.buttonID

	iRocLdap = IRocLDAP(host, bindDN, password)

	status = iRocLdap.enableButton( buttonID )



if __name__ == '__main__':
		main()



