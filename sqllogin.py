import pyodbc
import time

print("*" * 50)

print ("SQL CONNECTİON TEST")

print("*" * 50)

try:
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=.\POSSQL;'
                        'Database=infinia;'
                        'Trusted_Connection=yes;')

    #cursor = conn.cursor()
    #cursor.execute('SELECT * FROM infinia.dbo.employeefiles')a

    time.sleep(2)
    print("Bağlantı sağlandı")

except:
    time.sleep(2)
    print("SQL Bağlantı Hatası")



