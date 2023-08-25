import socket

# Cria um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta em que o servidor vai escutar
host = 'localhost'  # ou use o seu IP público
port = 55555

# Faz o bind do socket com o endereço IP e a porta
server_socket.bind((host, port))

# Escuta por conexões
server_socket.listen(1)

print(f'Servidor escutando em {host}:{port}')

# Aceita uma conexão
client_socket, client_address = server_socket.accept()
print(f'Conexão recebida de {client_address[0]}:{client_address[1]}')

try:
    while True:
        # Recebe dados do cliente
        data = client_socket.recv(1024)
        if not data:
            break

        print(f'Dados recebidos do cliente: {data.decode()}')

        # Envia uma resposta de volta ao cliente
        response = f'Recebido: {data.decode()}'
        client_socket.send(response.encode())

except ConnectionResetError:
    print("Conexão foi redefinida pelo cliente.")

finally:
    # Fecha a conexão ao sair do loop
    client_socket.close()
    server_socket.close()
