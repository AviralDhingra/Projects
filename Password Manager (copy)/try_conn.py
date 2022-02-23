import psycopg2

connection = psycopg2.connect(user="postgres", password="A@2008viral",
                              host="127.0.0.1",
                              port="5432",
                              database="passm")

cursor = connection.cursor()

query = '''INSERT INTO accounts(service,email, password) VALUES(
    'hello','johndoe@mail.com',
    crypt('johnspassword', gen_salt('bf'))
);'''

cursor.execute(query)
connection.commit()
