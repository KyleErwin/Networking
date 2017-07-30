import mimetypes
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

Las_Angeles = """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">Las Angeles</h1>
    <!-- <h1 id="date">Error</h1> -->
    <h1 id="staticJohannesburgTime">Error</h1>
    <h1 id="staticJohannesburgLocation">Johannesburg</h1>
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""

London = """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">London</h1>
    <!-- <h1 id="date">Error</h1> -->
    <h1 id="staticJohannesburgTime">Error</h1>
    <h1 id="staticJohannesburgLocation">Johannesburg</h1>
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""

Cape_Town= """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">Cape Town</h1>
    <!-- <h1 id="date">Error</h1> -->
    
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""

Johannesburg = """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" type="text/css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">Johannesburg</h1>
    <!-- <h1 id="date">Error</h1> -->
    
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""
Hong_Kong = """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">Hong Kong</h1>
    <!-- <h1 id="date">Error</h1> -->
    <h1 id="staticJohannesburgTime">Error</h1>
    <h1 id="staticJohannesburgLocation">Johannesburg</h1>
    
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""

Sydney = """
<html lang="en">
<head>
    <title>World Clock</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <h1 id="time">Error</h1>
    <h1 id="location">Sydney</h1>
    <!-- <h1 id="date">Error</h1> -->
    <h1 id="staticJohannesburgTime">Error</h1>
    <h1 id="staticJohannesburgLocation">Johannesburg</h1>
    
    <div id="linksBox">
        <a href="/Las_Angeles" style="cursor: pointer;">Las Angeles</a><br><br>
        <a href="/London" style="cursor: pointer;">London</a><br><br>
        <a href="/Cape_Town" style="cursor: pointer;">Cape Town</a><br><br>
        <a href="/" style="cursor: pointer;">Johannesburg</a><br><br>
        <a href="/Hong_Kong" style="cursor: pointer;">Hong Kong</a><br><br>
        <a href="/Sydney" style="cursor: pointer;">Sydney</a><br><br>
    </div>
</body>
</html>
"""

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        if self.path.endswith(".css"):
            mimetype = 'text/css'
            f = open("style.css")
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(bytes(f.read(), "utf8"))
            return
            f.close()

        if self.path.endswith(".min.js"):
            mimetype = 'application/javascript'
            f = open("jquery/jquery.min.js")
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(bytes(f.read(), "utf8"))
            f.close()
            return

        if self.path.endswith(".js"):
            mimetype = 'application/javascript'
            f = open("script.js")
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(bytes(f.read(), "utf8"))
            f.close()
            return

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write content

        if self.path == "/":  # base path
            self.wfile.write(bytes(Johannesburg , "utf8"))

        elif (self.path == "/Las_Angeles"):
            self.wfile.write(bytes(Las_Angeles, "utf8"))

        elif (self.path == "/London"):
            self.wfile.write(bytes(London, "utf8"))

        elif (self.path == "/Cape_Town"):
            self.wfile.write(bytes(Cape_Town, "utf8"))

        elif (self.path == "/Johannesburg "):
            self.wfile.write(bytes(Johannesburg , "utf8"))

        elif (self.path == "/Hong_Kong"):
            self.wfile.write(bytes(Hong_Kong, "utf8"))

        elif (self.path == "/Sydney"):
            self.wfile.write(bytes(Sydney, "utf8"))
        return


def run():
    print('Server Started')
    # Server settings
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server Runnnig')
    httpd.serve_forever()

run()