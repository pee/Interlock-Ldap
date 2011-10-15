#!/usr/bin/python
#
#
# ./addHacker.py <bunch of crap>
#
#
from irocldap import IRocLDAP
import argparse
import yaml


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--uid', dest='uid', required=True)
	parser.add_argument('--name', dest='name', required=True)
	parser.add_argument('--address', dest='address', required=True)
	parser.add_argument('--alias', dest='alias', required=True)
	parser.add_argument('--econtact', dest='econtact', required=True)
	parser.add_argument('--status', dest='status', required=True)
	parser.add_argument('--level', dest='level', required=True)

	parser.add_argument('-v', dest='verbose', action='store_true')

	args = parser.parse_args()

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	toolConfig = config['tool']

	host     = toolConfig['host']
	bindDN   = toolConfig['bindDN']
	password = toolConfig['password']


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



