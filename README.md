# simple-blockchain

```
$ curl -X GET -H "Content-Type: application/json" -d '{
> "sender": "d4ee26eee15148ee92c6cd394edd974e",
>  "recipient": "recipient-address",
>  "amount": 5
> }' http://localhost:5000/transaction/new
```

```
$ curl -X POST -H "Content-Type: application/json -d '{
  "nodes": ["http://127.0.0.1:5001"]
  }' http://localhost:5000/nodes/register
```
