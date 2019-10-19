#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import requests

def messgae_accumulator(dict_input):
    print(dict_input)
    # call your api here:
    # return type dict
    # example:
    '''
    {
        'token': 'fad1e3w5ypbx5q9t69q59jn8mo',
        'team_id': 'wtpx8yiowtbs5nes6adqcdco1e',
        'team_domain': 'plotbotteam',
        'channel_id': '8ufhaw5mzbb47qc4so1tjnxn3w',
        'channel_name': 'utsav_trialas',
        'timestamp': 1571471726012,
        'user_id': 'wg36a3m8j3r7x8zjsxmpgxyqww',
        'user_name': 'utsav',
        'post_id': 'eqfk375uojy3j89mtk87m456jy',
        'text': 'plotbot 1212',
        'trigger_word': 'plotbot',
        'file_ids': ''
    }
    '''
    pass

# Input type string to send it to the token of bot
def message_sender(string_output):
    headers = {'Content-Type': 'application/json'}
    data = {"text": string_output}
    url = 'http://ec2-18-217-150-234.us-east-2.compute.amazonaws.com:8065/hooks/pge13ck3o3b4383jxkdbke74cr'
    response = requests.post(url, headers=headers, data=str(json.dumps(data)))
    # print(response)

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info(json.loads(post_data.decode('utf-8')))
        messgae_accumulator(json.loads(post_data.decode('utf-8')))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
