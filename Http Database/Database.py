import sqlite3

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def createTable():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Appointments ( '
                       'ID INTEGER PRIMARY KEY AUTOINCREMENT, '
                       'Date VARCHAR(32),'
                       'Time INT(10),'
                       'With VARCHAR(32),'
                       'Description VARCHAR(32));')
        db.commit()


def insert(values):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        sql = 'INSERT INTO Appointments(Date, Time, With, Description) VALUES (?, ?, ?, ?)'
        cursor.execute(sql, values)
        db.commit()


def update(values, id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        sql = 'UPDATE Appointments SET Date = ?, Time = ?, With = ?, Description = ? WHERE ID = ' + id
        cursor.execute(sql, values)
        db.commit()

def delete(id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        sql = 'DELETE FROM Appointments WHERE ID = ?'
        cursor.execute(sql, id)
        db.commit()

def selectAllAppointments():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Appointments')
        appointments = cursor.fetchall()
        return appointments

def printAppointments(self):
    appointments = selectAllAppointments()

    self.write(style.BOLD + 'ID\tDate\t\t\tTime\t\tWith\t\tDescription' + style.END + "\n")

    for appointment in appointments:
        self.write('{0}.\t{1}\t    {2}\t    {3}\t    {4}'
              .format(appointment[0], appointment[1], appointment[2], appointment[3], appointment[4]) + "\n")

def selectAppointment(id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM Appointments WHERE ID = ?'
        cursor.execute(sql, id)
        appointment = cursor.fetchall()
        return appointment

def printAppointment(self, id):
    appointment = selectAppointment(id)[0]

    self.write(style.BOLD + 'ID:    ' + style.END + '{0}'.format(appointment[0]) + "\n")
    self.write(style.BOLD + 'Date:        ' + style.END + '{0}'.format(appointment[1]) + "\n")
    self.write(style.BOLD + 'Time:        ' + style.END + '{0}'.format(appointment[2]) + "\n")
    self.write(style.BOLD + 'With:        ' + style.END + '{0}'.format(appointment[3]) + "\n")
    self.write(style.BOLD + 'Description:        ' + style.END + '{0}'.format(appointment[4]) + "\n")

def displayMenu(self):
    createTable()
    appointment = ["", "", "", ""]

    while (True):
        self.write("\n\t" + style.BOLD + "APOINTMENT MANAGER" + style.END + "\n"
              "1. View appoinments\n"
              "2. Add appointment\n"
              "3. Delete appointment\n"
              "4. Update appointment\n"
              "5. Exit\n")

        self.write('\nEnter your choice: ')
        choice = format(self.read())

        if choice == '1':
            self.write('\n' + style.BOLD + "View Appointments" + style.END + "\n")
            self.write('-------------------------------------------------------\n')
            printAppointments(self)
            self.write("\n")

        if choice == '2':
            self.write('\n' + style.BOLD + "Add Appointment" + style.END + "\n")
            self.write('-------------------------------------------------------\n')

            self.write('\nDate?: ')
            date = format(self.read())
            self.write('\nTime?: ')
            time = format(self.read())
            self.write('\nWith?: ')
            with_ = format(self.read())
            self.write('\nDescription: ')
            description = format(self.read())

            appointment[0] = date
            appointment[1] = time
            appointment[2] = with_
            appointment[3] = description

            insert(appointment)
            self.write("Appointment added!\n")
            self.write("\n")

        if choice == '3':
            self.write('\n' + style.BOLD + "Delete Appointment" + style.END + "\n")
            self.write('-------------------------------------------------------\n')
            printAppointments(self)
            self.write("\n")
            self.write('Enter the ID of the appointment you wish to delete: ')
            id = format(self.read())
            self.write('Are you sure you want to delete this appointment?')
            printAppointment(self, id)
            self.write("\n")
            self.write('Yes or No: ')
            check = format(self.read())
            if check == 'Yes':
                delete(id)
                self.write("Appointment deleted!\n")
                self.write("\n")

        if choice == '4':
            self.write('\n' + style.BOLD + "Update Appointment" + style.END + "\n")
            self.write('-------------------------------------------------------\n')
            printAppointments(self)
            self.write("\n")
            self.write('Enter the ID of the appointment you wish to delete: ')
            id = format(self.read())
            printAppointment(self, id)
            self.write("\n")
            self.write("Update the field or leave it as is by pressing enter.")
            self.write('\nDate?: ')
            date = format(self.read())
            self.write('\nTime?: ')
            time = format(self.read())
            self.write('\nWith?: ')
            with_ = format(self.read())
            self.write('\nDescription: ')
            description = format(self.read())

            oldInfo = selectAppointment(id)[0]

            appointment[0] = oldInfo[1]
            appointment[1] = oldInfo[2]
            appointment[2] = oldInfo[3]
            appointment[3] = oldInfo[4]

            if date != "":
                appointment[0] = date

            if time != "":
                appointment[1] = time

            if with_ != "":
                appointment[2] = with_ + ""

            if description != "":
                appointment[3] = description

            update(appointment, id)
            self.write("Appointment updated!\n")
            self.write("\n")

        if choice == '5':
            break