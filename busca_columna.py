import sqlite3
import csv

# First, let's check the actual column names in the CSV file
filename = 'tracks.csv'

print("Reading CSV file to check column names...")
with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Column names found:", reader.fieldnames)
    
    # Read first row to see the structure
    first_row = next(reader, None)
    if first_row:
        print("First row sample:", first_row)