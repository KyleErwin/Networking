from Database import *
from http.server import BaseHTTPRequestHandler, HTTPServer

def viewAppointmentsPage():
    page = """
    <html lang="en">
    <head>
        <title>Appointment Manager</title>
        <link href="style.css" rel="stylesheet">
        <script src="jquery/jquery.min.js"></script>
        <script src="script.js"></script>
    </head>
    <body>
        <h1 id="heading">Appointment Manager</h1>

        <div id="linksBox">
            <a href="/addAppointment" style="cursor: pointer;">Add Appointment</a><br><br>
            <a href="/deleteAppointment" style="cursor: pointer;">Delete Appointment</a><br><br>
            <a href="/updateAppointment" style="cursor: pointer;">Update Appointment</a><br><br>
            <a href="/" style="cursor: pointer;">View Appointment</a><br><br>
        </div>

        <h1 id="contentHeading">View Appointments</h1>
        <div id="contentBox">
            <table>
              <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Time</th>
                <th>Description</th>
                <th>With</th>
              </tr>
    """

    appointments = selectAllAppointments()
    for appointment in appointments:
        page += "<tr>"
        page += "<td>" + str(appointment[0]) + "</td>"
        page += "<td>" + str(appointment[1]) + "</td>"
        page += "<td>" + str(appointment[2]) + "</td>"
        page += "<td>" + str(appointment[3]) + "</td>"
        page += "<td>" + str(appointment[4]) + "</td>"
        page += "</tr>"

    page += """
    </table>
        </div>
    </body>
    </html>
    """

    return page

viewAppointments = viewAppointmentsPage()

addAppointment = """
<html lang="en">

<head>
    <title>Appointment Manager</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>

<body>
    <h1 id="heading">Appointment Manager</h1>
    <div id="linksBox">
        <a href="/addAppointment" style="cursor: pointer;">Add Appointment</a>
        <br>
        <br>
        <a href="/deleteAppointment" style="cursor: pointer;">Delete Appointment</a>
        <br>
        <br>
        <a href="/updateAppointment" style="cursor: pointer;">Update Appointment</a>
        <br>
        <br>
        <a href="/" style="cursor: pointer;">View Appointment</a>
        <br>
        <br>
    </div>
    <h1 id="contentHeading">Add Appointment</h1>
    <div id="contentBox"> 
        <form action="addAppointmentAction" method="get">
            <input type="text" placeholder="dd/mm/yyyy" name="Date">
            <input type="text" placeholder="hh:mm" name="Time">
            <input type="text" placeholder="With whom" name="With">
            <input type="text" placeholder="Description" name="Description">
            <input type="hidden" value="addAppointmentAction" name="Action">
            <input type="submit" value="Submit">
        </form>
    </div>
</body>

</html>

"""

deleteApppointment= """
<html lang="en">

<head>
    <title>Appointment Manager</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>

<body>
    <h1 id="heading">Appointment Manager</h1>
    <div id="linksBox">
        <a href="/addAppointment" style="cursor: pointer;">Add Appointment</a>
        <br>
        <br>
        <a href="/deleteAppointment" style="cursor: pointer;">Delete Appointment</a>
        <br>
        <br>
        <a href="/updateAppointment" style="cursor: pointer;">Update Appointment</a>
        <br>
        <br>
        <a href="/" style="cursor: pointer;">View Appointment</a>
        <br>
        <br>
    </div>
    <h1 id="contentHeading">Delete Appointment</h1>
    <div id="contentBox">
        <form action="data" method="get">
            <input type="number" placeholder="Appointment ID" name="ID">
            <input type="hidden" value="deleteAppointmentAction" name="Action">
            <input type="submit" value="Delete">
        </form>
    </div>
</body>
</html>

"""

updateAppointment = """
<html lang="en">
<head>
    <title>Appointment Manager</title>
    <link href="style.css" rel="stylesheet">
    <script src="jquery/jquery.min.js"></script>
    <script src="script.js"></script>
</head>

<body>
    <h1 id="heading">Appointment Manager</h1>
    <div id="linksBox">
        <a href="/addAppointment" style="cursor: pointer;">Add Appointment</a>
        <br>
        <br>
        <a href="/deleteAppointment" style="cursor: pointer;">Delete Appointment</a>
        <br>
        <br>
        <a href="/updateAppointment" style="cursor: pointer;">Update Appointment</a>
        <br>
        <br>
        <a href="/" style="cursor: pointer;">View Appointment</a>
        <br>
        <br>
    </div>
    <h1 id="contentHeading">Update Appointment</h1>
    <div id="contentBox">
        <form action="data" method="get">
            <input type="number" placeholder="Appointment ID" name="ID">
            <input type="text" placeholder="dd/mm/yyyy" name="Date">
            <input type="text" placeholder="hh:mm" name="Time">
            <input type="text" placeholder="With whom" name="With">
            <input type="text" placeholder="Description" name="Description">
            <input type="hidden" value="updateAppointmentAction" name="Action">
            <input type="submit" value="Update">
        </form>
    </div>
</body>
</html>
"""

portNumber = 8818


def convertToAddArray(getResponse):
    getResponse += ""
    appointment = ["", "", "", ""]
    appointment[0] = find_between(getResponse, "Date=", "&Time=") #date
    appointment[1] = find_between(getResponse, "Time=", "&With=") #time
    appointment[2] = find_between(getResponse, "With=", "&Description=") #with
    appointment[3] = find_between(getResponse, "Description=", "&Action=") #description
    return appointment


def convertToUpdateArray(getResponse):
    getResponse += ""
    appointment = ["", "", "", "", ""]
    appointment[0] = find_between(getResponse, "ID=", "&Date=")  # ID
    appointment[1] = find_between(getResponse, "Date=", "&Time=") #date
    appointment[2] = find_between(getResponse, "Time=", "&With=") #time
    appointment[3] = find_between(getResponse, "With=", "&Description=") #with
    appointment[4] = find_between(getResponse, "Description=", "&Action=") #description
    print(appointment)
    return appointment


def convertToDeleteArray(getResponse):
    getResponse += ""
    appointment = [""]
    appointment[0] = find_between(getResponse, "ID=", "&Action=")  # ID
    return appointment;


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


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

        print(self.path);
        if self.path == "/":  # base path
            viewAppointments = viewAppointmentsPage()
            self.wfile.write(bytes(viewAppointments , "utf8"))

        elif (self.path == "/addAppointment"):
            self.wfile.write(bytes(addAppointment, "utf8"))

        elif(self.path.endswith("addAppointmentAction")):
            appointment = convertToAddArray(self.path)
            insert(appointment)
            viewAppointments = viewAppointmentsPage()
            self.wfile.write(bytes(viewAppointments, "utf8"))

        elif (self.path == "/updateAppointment"):
            self.wfile.write(bytes(updateAppointment , "utf8"))

        elif (self.path.endswith("updateAppointmentAction")):
            appointment = convertToUpdateArray(self.path)
            update(appointment)
            viewAppointments = viewAppointmentsPage()
            self.wfile.write(bytes(viewAppointments, "utf8"))

        elif (self.path == "/deleteAppointment"):
            self.wfile.write(bytes(deleteApppointment, "utf8"))

        elif (self.path.endswith("deleteAppointmentAction")):
            appointment = convertToDeleteArray(self.path)
            delete(appointment)
            viewAppointments = viewAppointmentsPage()
            self.wfile.write(bytes(viewAppointments, "utf8"))
        return

def run():
    print('Server Started')
    createTable()
    # Server settings
    server_address = ('127.0.0.1', portNumber)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server Runnnig')
    httpd.serve_forever()

run()