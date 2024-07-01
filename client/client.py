import time
import socket
import json
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

player_obj = {
    'username': 'test',
    'password': 'test'
}

databytes = bytes(json.dumps(player_obj), encoding='utf-8')

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0)
    
    addr = ("127.0.0.1", 12000)

    while True:
        # message = b'test' TODO: What does b'test' mean?
        

        start = time.time()
        client_socket.sendto(databytes, addr)

        try:
            data = client_socket.recvfrom(1024)
            data = data[0].decode('utf-8')

            end = time.time()
            elapsed = end - start
            logger.info("Received message back from server %s", data)
            logger.info("Elapsed time: %s", elapsed)

        except socket.timeout:
            logger.error("Socket timed out")
        finally:
            # for now close as we test this out
            client_socket.close()
            break;



if __name__ == '__main__':
    logging.info("Starting client")
    main()