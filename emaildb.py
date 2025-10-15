import sqlite3
import re

# Create SQLite database and table
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

# Read the mbox.txt file
filename = 'mbox.txt'

# Regular expression to extract email domains from From: lines
email_pattern = re.compile(r'^From .*@([a-zA-Z0-9.-]+)')

try:
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            match = email_pattern.match(line)
            if match:
                org = match.group(1).lower()  # Convert to lowercase for consistency
                
                # Update count in database
                cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
                row = cur.fetchone()
                
                if row is None:
                    cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
                else:
                    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    # Commit all changes at once (for better performance)
    conn.commit()

except FileNotFoundError:
    print(f"Error: File {filename} not found.")
    print("Please download mbox.txt from http://www.py4e.com/code3/mbox.txt")
    conn.close()
    exit()

# Print the results to verify
print("Counts by organization:")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
for row in cur:
    print(row[0], row[1])

cur.close()
conn.close()

print("\nDatabase file 'emaildb.sqlite' has been created and is ready for upload.")