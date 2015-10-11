# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class HelloWorldManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (HelloWorldManager, self).__init__(consensusManager, wallet)
			
	def sendName (self, name):
		cid = self._produce_transaction ('helloworld.hello', [name])
		return cid
	
	def getNames (self):
		return self.consensusManager.jsonConsensusCall ('helloworld.get_names', [])['result']
