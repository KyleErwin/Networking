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