import SimpleHTTPServer
import SocketServer
import webbrowser

webbrowser.open_new_tab('http://localhost:8000/CARSIM.html')

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()