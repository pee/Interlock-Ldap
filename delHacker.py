#!/usr/bin/python
#
#
from irocldap import IRocLDAP
import argparse
import yaml


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--uid', dest='uid', required=True)
	parser.add_argument('-v', dest='verbose', action='store_true')
	args = parser.parse_args()

	config = file('config.yaml', 'r')
	config = yaml.load(config)
	toolConfig = config['tool']

	host     = toolConfig['host']
	bindDN   = toolConfig['bindDN']
	password = toolConfig['password']

	uid      = args.uid

	iRocLdap = IRocLDAP(host, bindDN, password)

	status = iRocLdap.delHacker( uid )



if __name__ == '__main__':
		main()



