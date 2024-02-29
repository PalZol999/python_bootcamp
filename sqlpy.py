import sqlite3
conn= sqlite3.connect("user")


#c.execute("CREATE TABLE users (user_name TEXT, user_pw TEXT) ")
#query = '''INSERT INTO users VALUES ("Adam", "Password123"), ("Bela", "PW123"), ("Carle", "pamacs123")'''
#c.execute(query)

u=input("please enter your username...")
p=input("please enter your paswrod...")
query=f"SELECT * FROM users WHERE user_name='{u}' AND user_pw='{p}'"

c= conn.cursor()
c.execute(query)

result=c.fetchone()
if (result) : 
    print ("Welcome back")
else:
    print ("Access denied")
conn.commit()
conn.close()