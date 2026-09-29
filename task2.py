import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create table and insert 8 records
cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price REAL,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'Data Science Basics', 'Tech', 1450, 10),
(2, 'Clean Code', 'Tech', 1200, 8),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'Python Crash Course', 'Tech', 950, 15),
(5, 'To Kill a Mockingbird', 'Fiction', 800, 3),
(6, '1984', 'Fiction', 1100, 6),
(7, 'The Great Gatsby', 'Fiction', 1250, 1),
(8, 'Intro to Algorithms', 'Tech', 2200, 4);
""")
conn.commit()

# Query (a) & (b): Price > 1000 sorted descending, title aliased as book_title
print("Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title AS book_title, price 
FROM books 
WHERE price > 1000 
ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

# Query (c): Fiction with stock < 5
print("\nLow-stock Fiction books:")
cur.execute("""
SELECT title AS book_title, genre, price, stock 
FROM books 
WHERE genre = 'Fiction' AND stock < 5;
""")
for row in cur.fetchall():
    print(row)

conn.close()