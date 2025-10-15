import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Query 1
cur.execute('''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC
LIMIT 2;
''')
for row in cur.fetchall():
    print(row)

# Query 2
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X
LIMIT 1;
''')
for row in cur.fetchall():
    print(row)

# Cerrar la conexión
conn.close()
