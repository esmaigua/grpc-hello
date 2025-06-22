import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hola, {request.name} desde gRPC")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
