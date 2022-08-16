# simple-blockchain
This project as the name implies was made in order to understand the structure of a blockchain at its simplest, as well as, understand related ideas such as chaining, consensus, and proof of work. Python was used to created the blockchain object, and Flask was utilized to handle API endpoints.

## Setup 
In order to use this blockchain you will need a Python Interpreter and an HTTP client such as cURL.

First, download this repository and navigate to the folder location in git bash and run the following command to activate the virtual environment
```
$ cd .venv/Scripts && . activate && cd ../../
```
We will now set the flask environment variable with the following command
```
$ export set FLASK_APP=blockchain
```
Finally, run the flask app with the following command 
```
$ flask run -h localhost -p 5000
```
We now have an up an running flask server to interact with our blockchain.

## Usage
Before we can begin interacting with our blockchain we need to first understand what a block on the chain looks like
``` 
{
    'index': 1,
    'timestamp': 1506092455,
    'transactions': [
        {
            'sender': "d4ee26eee15148ee92c6cd394edd974e",
            'recipient': "a77f5cdfa2934hv25c7c7da5df1f",
            'amount': 19,
        }
    ],
    'proof': 35293,
    'previous_hash': "e17dc1bc69806ca3311e7a41c2e5ea763ca9756585d2cef6e42fe1478b2ae8e3"
}
```
Each block has a index, timestamp, list of transactions, proof, and its own hash as well as the hash of the previous block.

Now loading up a new instance of git bash we can begin interacting with our blockchain.

### Mining
We can mine a block onto our chain using the following curl command in git bash
```
$ curl http://localhost:5000/mine
```

### Adding Transactions
We can add transactions onto our blockchain by sending a json object of the following form
```
{
  "sender": "d4ee26eee15148ee92c6cd394edd974e",
  "recipient": "a77f5cdfa2934hv25c7c7da5df1f",
  "amount": 20
 }
```
this can be done with the following curl command 
```
$ curl -X GET -H "Content-Type: application/json" -d '{
  "sender": "d4ee26eee15148ee92c6cd394edd974e",
  "recipient": "a77f5cdfa2934hv25c7c7da5df1f",
  "amount": 20
 }' http://localhost:5000/transaction/new
```

### Viewing Chain 
We can view our entire blockchain using the following curl command 
```
$ curl http://localhost:5000/chain
```

Now before we can begin using consensus with our blockchain we must first setup other nodes on the network, and register them to our node.

To setup another node we can follow the same process outlined in Setup in a new git bash terminal, but changing the port number when we run the flask app.

### Registering nodes
In order to register nodes we will send a json object containing the IP address of the other nodes on the network.
```
{
  "nodes": ["http://localhost:5001"]
}
```
We can achieve this with the following curl command 
```
$ curl -X POST -H "Content-Type: application/json" -d '{
  "nodes": ["http://127.0.0.1:5001"]
 }' http://localhost:5000/nodes/register
```

### Consensus
We can update our blockchain with the most up to date version of the blockchain on the network with the following curl command 
```
curl http://localhost:5000/nodes/resolve
```