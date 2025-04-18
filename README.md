#Cross-Chain ETH to Cosmos Token Bridge

This project implements a basic cross-chain token swap system between Ethereum and Cosmos.

It consists of:
- A Solidity smart contract (`LockBridge.sol`) deployed to a local Ethereum test network (Ganache)
- A Python listener (`main.py`) that monitors Ethereum events and simulates Cosmos-side minting

## How it works

1. A user locks ETH in the Ethereum smart contract and specifies a Cosmos address.
2. The smart contract emits a `TokensLocked` event with the sender, amount, and Cosmos address.
3. A Python script listens for these events using Web3.py.
4. When an event is detected, the script simulates minting the same amount to the Cosmos address.


