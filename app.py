from flask import Flask, render_template
import uuid
import hashlib
import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='mz4358bh',
                             password='Compscispring2020',
                             db='mz4358bh_',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

Name = input("Enter a username: ")
Password = input("Enter a password for username: " + Name + ": ")
Salt = uuid.uuid4().hex
Hash = hashlib.sha512(Password.encode('utf-8') + Salt.encode('utf-8')).hexdigest()



try:
    with connection.cursor() as cursor:
        # Select from Students Table the name set as input
        sql = ("INSERT into Salt Values ('" + Name + "', '" + Salt + "', '" + Hash + "')" )

        # execute the SQL command
        cursor.execute(sql)
        output = cursor.fetchall()

finally: connection.commit()
print(sql + "\n")

print("Database updated with new salt and hash")
Name_2 =input("Please enter Username: ")
Password_2 = input("Please enter password for " + Name_2 + ": ").__str__()
try:
    with connection.cursor() as cursor:
        # Select from Students Table the name set as input
        sql = ("SELECT * FROM Salt WHERE Name = '" + Name_2 + "'")

        # execute the SQL command
        cursor.execute(sql)
        for result in cursor:
            print(result)
            saved_salt = result.get('salt').__str__()
            saved_hash = result.get('hash').__str__()
        new_hash = hashlib.sha512(Password_2.encode('utf-8') + saved_salt.encode('utf-8')).hexdigest()
        print(new_hash)
        if saved_hash == new_hash:
            print("passwords match!")
        else:
            print("passwords do not match!")

finally: connection.close()

app = Flask(__name__)

if __name__ == '__main__':
    app.run()