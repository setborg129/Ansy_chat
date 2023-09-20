import json

# from common.variables import MAX_PACKAGE_LENGTH, ENCODING

def get_message(sock):

    encode_response = sock.recv(1000000)
    if isinstance(encode_response, bytes):
        json_responce = encode_response.decode('utf-8')
        responce = json.loads(json_responce)
        if isinstance(responce, dict):
            return responce



def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode('utf-8')
    sock.send(encoded_message)