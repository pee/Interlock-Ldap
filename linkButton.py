#!/usr/bin/python
#
#
#
from irocldap import IRocLDAP
import argparse
import yaml


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--button', dest='buttonID', help='the iButton ID', required=True)
	parser.add_argument('--uid', dest='uid', help='the hacker uid', required=True)
	args = parser.parse_args()

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	toolConfig = config['tool']

	host     = toolConfig['host']
	bindDN   = toolConfig['bindDN']
	password = toolConfig['password']


	buttonID = args.buttonID
	uid      = args.uid

	iRocLdap = IRocLDAP(host, bindDN, password)

	status = iRocLdap.linkButtonToUid( buttonID, uid )



if __name__ == '__main__':
		main()



