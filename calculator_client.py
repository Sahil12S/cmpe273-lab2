# Client library for Calculator

# Import required libraries.
from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)


    while True:
        try:
            val1 = float(input("Enter first number:"))
            val2 = float(input("Enter second number:"))
            break
        except ValueError:
            print("You entered invalid number\n")

    response = stub.Sum(calculator_pb2.SumRequest(value1=val1, value2=val2))
    print("Sum of {} and {} is: {}".format(val1, val2, response.value))
    channel.close()


if __name__ == '__main__':
    run()
