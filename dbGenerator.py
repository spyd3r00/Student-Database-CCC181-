import sqlite3

conn = sqlite3.connect('students.db')

c = conn.cursor()

# c.execute("""CREATE TABLE students(
# 			id INTEGER PRIMARY KEY AUTOINCREMENT,
# 			fullname text,
# 			course text,
# 			idnumber text UNIQUE,
# 			year integer,
# 			gender text
# 			)""")

# c.execute("""CREATE TABLE colleges(
# 			course text,
# 			colleges text
# 			)""")

#c.execute("INSERT INTO colleges VALUES ('BSCS','CCS')")
c.execute("INSERT INTO colleges VALUES ('BSMATH','CSM')")
c.execute("INSERT INTO colleges VALUES ('DTTE','CED')")
c.execute("INSERT INTO colleges VALUES ('BSCE','COET')")
c.execute("INSERT INTO colleges VALUES ('BSPSYCH','CASS')")
c.execute("INSERT INTO colleges VALUES ('BSBA','CBAA')")
c.execute("INSERT INTO colleges VALUES ('NURSING','CON')")
conn.commit()
conn.close()