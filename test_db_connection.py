import mysql.connector

print("Starting MySQL Connection Test...")  # Added print

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Afreedy@123",
    database="my_database"
)

if conn.is_connected():
    print("✅ Connected to MySQL")
else:
    print("❌ Connection failed")

conn.close()
print("Connection closed.")  # Added print
