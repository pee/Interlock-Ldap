#!/usr/bin/python
#
#
# ./addButton.py --button 01000012FF85207C
#
#
from irocldap import IRocLDAP
import argparse
import yaml


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--button', dest='buttonID', help='the iButton ID', required=True)
	parser.add_argument('-v', dest='verbose', action='store_true')
	args = parser.parse_args()

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	toolConfig = config['tool']

	host     = toolConfig['host']
	bindDN   = toolConfig['bindDN']
	password = toolConfig['password']
	buttonID = args.buttonID

	iRocLdap = IRocLDAP(host, bindDN, password)

	status = iRocLdap.addButton( buttonID )



if __name__ == '__main__':
		main()



