import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        name = "Mundo"
        response = stub.SayHello(hello_pb2.HelloRequest(name=name))
        print("Respuesta del servidor:", response.message)

if __name__ == '__main__':
    run()
