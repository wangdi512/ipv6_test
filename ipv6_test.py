#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-27 13:50:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import socket
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/ip':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write('Your IP address is %s' % self.client_address[0])
      return
    else:
      return SimpleHTTPRequestHandler.do_GET(self)

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

def main():
  server = HTTPServerV6(('::', 80), MyHandler)
  server.serve_forever()

if __name__ == '__main__':
  main()