# Using gRPC

**gRPC (gRPC Remote Procedure Calls)** is an open source remote procedure call (RPC) system initially developed at Google. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. It generates cross-platform client and server bindings for many languages.

## Task
Create a simple Calculator with add(x, y) function as gRPC server and provide a test client to invoke the Calculator service