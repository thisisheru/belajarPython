import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()
print("Daftar Siswa")
print(students)
print("Data Telah Ditampilkan")
print(ini dari banch compose
      )