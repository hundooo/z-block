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
$ flask run
```
We now have an up an running flask server to interact with our blockchain.

## Usage


```
$ curl -X GET -H "Content-Type: application/json" -d '{
  "sender": "d4ee26eee15148ee92c6cd394edd974e",
  "recipient": "recipient-address",
  "amount": 5
 }' http://localhost:5000/transaction/new
```

```
$ curl -X POST -H "Content-Type: application/json" -d '{
  "nodes": ["http://127.0.0.1:5001"]
 }' http://localhost:5000/nodes/register
```
