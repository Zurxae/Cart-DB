import mysql.connector

def getUserInfo(config, email):
    passed = False
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        getUserInfoQuery = "SELECT fname, lname FROM users WHERE email = '{email}';"
        getAddressInfoQuery = "SELECT address, zipcode, state, city FROM address_info WHERE email = '{email}';"

        cursor.execute(getUserInfoQuery.format(email=email))
        user = cursor.fetchone()

        print(user)
        
        cursor.execute(getAddressInfoQuery.format(email=email))
        userMore = cursor.fetchone()

        print(userMore)

        user += userMore

        print(user)

        passed = True
    except mysql.connector.Error as e:
        print('Error reading data from MySQL table', e)
    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print('MySQL connection is closed')
        if passed:
            return user
        else:
            return None