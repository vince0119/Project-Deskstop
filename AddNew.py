import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='asp')

CardReDB = 'SELECT * FROM cardregistered LIMIT 0, 5'
ParksDB = 'SELECT * FROM parking_area LIMIT 0, 5'
CarLogDB = 'SELECT * FROM car_log LIMIT 0, 5'
UserDB = 'SELECT * FROM users LIMIT 0, 5'
CarTypeDB = 'SELECT * FROM cardtype LIMIT 0, 5'
StaffDB = 'SELECT * FROM staffs LIMIT 0, 5'

def insert_data(self):
    try:
        mycursor = db.cursor()

        UserName = self.txtStaffUserName.text()
        Password = self.txtStaffPassword.text()

        query = "INSERT INTO (UserName, Password) VALUES (%s, %s)"

        value = (UserName, Password)

        mycursor.execute(query, value)

        db.commit()
        self.btnStaffOK.setText("Data Inserted")
    except mysql.Error as e:
        print('Fail')

    
        