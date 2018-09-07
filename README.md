# Using gRPC

**gRPC (gRPC Remote Procedure Calls)** is an open source remote procedure call (RPC) system initially developed at Google. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. It generates cross-platform client and server bindings for many languages.

## Task
Create a simple Calculator with add(x, y) function as gRPC server and provide a test client to invoke the Calculator service
## Solution
### Setting up the environment
```sh
$ # Create virtual environment for the lab.
$ python3 -m venv lab2-venv
$ # activate the environment
$ source lab2-venv/bin/activate
$ # Upgrade pip
$ pip3 install --upgrade pip
$ # Install libraries
$ pip3 install grpcio
$ # Install other gRPC tools after successful execution of last step
$ pip3 install grpcio-tools googleapis-common-protos
```

### Writing _Calculator.proto_
  - Use syntax **_proto3_**.
  - Write service definition for **Calculator**.

### Generating _pb2_ files
```sh
$ python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/calculator.proto
```

### Next steps
  - Write **_calculator_server.py_**. This will implement the addition functionality.
  - Write **_calculator_client.py_**. This will provide the parameters to _Sum()_ function

### Running  program
```sh
$ # In one terminal window start the server
$ python3 calculator_server.py
$ # In another terminal window start client
$ python3 calculator_client.py
```

### Cleaning the system
```sh
$ # Create "requirements.txt"
$ pip3 freeze > requirements.txt
$ # Deactivate the virtual Environment
$ deactivate
$ # Delete the environment
$ rm -r lab2-venv
```
