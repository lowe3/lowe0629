import psycopg2

conn = psycopg2.connect(
database = "d4jgiqvfjf2nde",
user = "rdvsrzpesjtzad",
password = "eddaf28d42616aba0fd4de92aeb8df4d1e33c6e1ae6a202da17fd1d6cd39fbaf",
host = "ec2-34-200-101-236.compute-1.amazonaws.com",
port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE Customer(
ID          VARCHAR(50) PRIMARY KEY   NOT NULL,
HEIGHT      INT                       NOT NULL,
WEIGHT      INT                       NOT NULL,
AGE         INT                       NOT NULL,
GENDER      VARCHAR(10)               NOT NULL,
BMR         INT                       NOT NULL);''')
print ("Table created successfully")

conn.commit()
conn.close()