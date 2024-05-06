import sqlite3

con = sqlite3.connect('lab8.db')
cursor = con.cursor()

cursor.execute(
    '''Create table if not exists _group(
id integer primary key autoincrement,
name text,
balance integer)''')

cursor.execute(
    '''Create table if not exists user(
    id integer primary key autoincrement,
    name text,
    email text,
    member_since text,
    avatar text)''')

cursor.execute(
    '''Create table if not exists group_user(
    id integer primary key autoincrement,
    id_group integer references _group(id),
    id_user integer references user(id),
    balance integer)''')

cursor.execute(
    '''Create table if not exists bill(
    id integer primary key autoincrement,
    id_group integer references _group(id),
    title integer,
    amount integer,
    date text,
    created_by integer)''')

cursor.execute(
    '''Create table if not exists bill_user_owes(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    owes integer)''')

cursor.execute(
    '''Create table if not exists bill_user_paid(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    paid integer)''')

cursor.execute(
    '''Create table if not exists note(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    massage text,
    created text)''')

print('1 - заполнение; 2 - вывод')
one = int(input())
if int(one) == 1:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    numbers = int(input())
    if int(numbers) == 1:
        print('group')
        print('имя ')
        name = input()
        print('balance')
        balance = input()
        cursor.execute('''insert into group(name,balance,) values(?,?);''',
                       (name, balance))
    elif int(numbers) == 2:
        print('bill')
        print('title')
        title = input()
        print('amount')
        amount = input()
        print('date')
        date = input()
        print('created_by')
        created_by = input()
        cursor.execute('''insert into bill(title,amount,date,created_by) values(?,?,?,?);''',
                       (title, amount,date,created_by))
    elif int(numbers) == 3:
        print('group_user')
        print('balance')
        balance = input()
        cursor.execute('''insert into group_user(balance) values(?);''',
                       (balance,))
    elif int(numbers) == 4:
        print('bill_user_owes')
        print('owes')
        owes = input()
        cursor.execute('''insert into bill_user_owes(owes) values(?);''',
                       (owes,))
    elif int(numbers) == 5:
        print('bill_user_paid')
        print('paid')
        paid = input()
        cursor.execute('''insert into bill_user_paid(paid) values(?);''',
                       (paid,))
    elif int(numbers) == 6:
        print('note')
        print('massage')
        massage = input()
        print('created')
        created = input()
        cursor.execute('''insert into note(massage,created) values(?,?);''',
                       (massage,created))
    elif int(numbers) == 7:
        print('user')
        print('имя ')
        name = input()
        print('почта ')
        email = input()
        print('номер телефона ')
        member_since = input()
        print('аватар ')
        avatar = input()
        cursor.execute('''insert into user(name,email,member_since,avatar) values(?,?,?,?);''',
                   (name, email, member_since, avatar))
    con.commit()
elif int(one) == 2:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    number = int(input())
    if int(number) == 1:
        cursor.execute('''select * from group''')
        nomber1 = cursor.fetchall()
        print(nomber1)
    elif int(number) == 2:
        cursor.execute('''select * from bill''')
        nomber2 = cursor.fetchall()
        print(nomber2)
    elif int(number) == 3:
        cursor.execute('''select * from group_user''')
        nomber3 = cursor.fetchall()
        print(nomber3)
    elif int(number) == 4:
        cursor.execute('''select * from bill_user_owes''')
        nomber4 = cursor.fetchall()
        print(nomber4)
    elif int(number) == 5:
        cursor.execute('''select * from bill_user_paid''')
        nomber5 = cursor.fetchall()
        print(nomber5)
    elif int(number) == 6:
        cursor.execute('''select * from note''')
        nomber6 = cursor.fetchall()
        print(nomber6)
    elif int(number) == 7:
        cursor.execute('''select * from user''')
        nomber7 = cursor.fetchall()
        print(nomber7)
    else:
        print('не то ')
else:
    print('не та команда')

con.commit()
con.close()
