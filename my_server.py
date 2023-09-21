# webapp.py

import json
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

class WebRequestHandler(BaseHTTPRequestHandler):

# Set of API calls
# curl -s -X POST 'http://0.0.0.0:8080/floor/5/call'
# curl -s -X POST 'http://0.0.0.0:8080/elevator/goto/5'
# curl -s -X GET 'http://0.0.0.0:8080/floor/requested'
# curl -s -X GET 'http://0.0.0.0:8080/floor/next'

    def write_output(self, msg):
        self.wfile.write(msg.encode('utf-8'))

    def reply_error(self):
        print ('ERROR')
        self.reply(404, 'Invalid API call\n')

    def reply(self, rc, msg):
        print (f'Replying with rc:{rc}, msg:{msg}')
        self.send_response(rc)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.write_output(msg)

    def process_apis(self, method, path):
        try:
            print('Method: %s\n' % method)

            print('processing: %s\n' % path)
            items = path.strip("/").lower().split('/')
            print(items)

            if (method == 'GET'):
                if (items[0] == 'floor' and items[1] == 'next'):
                    print ('processing get next floor')
                    self.reply(200, '3')
                elif (items[0] == 'floor' and items[1] == 'requested'):
                    print ('processing get requested floors')
                    self.reply(200, '[3,5,7]')
                else:
                    self.reply_error()
            elif (method == 'POST'):
                if (len(items) != 3):
                    self.reply_error()

                if (items[0] == 'floor' and items[2] == 'call'):
                    print (f'Sending elevator to floor {items[1]}')
                    self.reply(200, '')
                elif (items[0] == 'elevator' and items[1] == 'goto'):
                    print (f'Going to floor {items[2]}')
                    self.reply(200, '')
                else:
                    self.reply_error()
            else:
                self.reply_error()
        except:
            self.reply_error()

    def do_GET(self):
        self.process_apis('GET', self.path)

    def do_POST(self):
        self.process_apis('POST', self.path)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), WebRequestHandler)
    print ('Started...')
    server.serve_forever()