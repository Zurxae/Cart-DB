import mysql.connector

def authUser(form, config):
    passed = False
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        email = form.email.data
        pwd = form.password.data

        print('email:', email, 'password:', pwd)

        getUserQuery = "SELECT pwd FROM users WHERE email = %s;"
        cursor.execute(getUserQuery, (email,))

        record = cursor.fetchone()
        print('Total number of rows in table: ', cursor.rowcount)

        if cursor.rowcount == 0:
            print('email does not exist')
        else:
            print('record exists')
            if pwd == record[0]:
                print('Authentication Successful')
                passed = True
            else:
                print('Wrong password')
    except mysql.connector.Error as e:
        print('Error reading data from MySQL table', e)
    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print('MySQL connection is closed')
        if passed:
            return True, email
        else:
            return False, None
    