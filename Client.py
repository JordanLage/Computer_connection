import socket

# Cria um objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta do servidor
host = 'localhost'  # Use o IP do servidor ou 'localhost' para testes locais
port = 55555

# Conecta ao servidor
client_socket.connect((host, port))

try:
    while True:
        # Solicita ao usuário para digitar uma mensagem
        message = input('Digite uma mensagem para enviar ao servidor (ou "sair" para encerrar): ')
        if message == 'sair':
            break

        # Envia a mensagem para o servidor
        client_socket.send(message.encode())

        # Recebe a resposta do servidor
        response = client_socket.recv(1024)
        print('Resposta do servidor:', response.decode())

except KeyboardInterrupt:
    print("Conexão interrompida pelo usuário.")

finally:
    # Fecha a conexão ao sair do loop
    client_socket.close()
