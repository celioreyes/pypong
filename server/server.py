"""
    Some inspiration:
    https://www.youtube.com/watch?v=AkvYfwRFS7E

    - Create a routing system to know what action to take when a message is received. (DESIGN PATTERN KNOWLEDGE)
        { Action: "Player:Login_Anon", "Data": { "username": "test", "device_id": "1234"}}
    
    - Possibly have it be a dictionary with the key being the message and the value being the action to take. (JSON?)
    
    - Connect to SQLite database to store player stats and pull player information (username, password hash (?), etc...) (DATABASE KNOWLEDGE)
    
    - Have message be dealt with in a separate thread to not block the main thread. (ASYNC)
    
    - Logging and save to a file (sync to distributed logging solution). (LOGGING)
        - https://docs.python.org/3/library/logging.html
        - https://www.geeksforgeeks.org/logging-in-python/

    - Host the server on a cloud provider (AWS, Azure, Google Cloud, etc...) (CLOUD KNOWLEDGE) (Pure EC2?) (ECS for Scaling?)

    - Compile PyGmae to WebAssembly (WASM) to run in the browser. (WEB KNOWLEDGE)
        - https://www.youtube.com/watch?v=q25i2CCNvis
        - Faking a unique identifier for the device in HTML5
            - https://www.reddit.com/r/godot/comments/nrj62t/i_need_an_identifier_for_the_device_in_html5/
"""

import socket
import logging
import json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

def main():
    while True:
        message, address = server_socket.recvfrom(1024)
        
        parsedM = json.loads(message.decode('utf-8'))

        logger.info("Received message from client username: %s", parsedM["username"])
        # logger.info("Sending message back to client %s %s", username)
        server_socket.sendto(message, address)


# TODO: Better understand this...
if __name__ == '__main__':
    logger.info("Starting server")
    main()