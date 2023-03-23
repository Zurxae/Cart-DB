import mysql.connector

def enrollUser(form, config):
    passed = False
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        email = form.email.data
        pwd = form.password.data
        fname = form.fname.data
        lname = form.lname.data
        address = form.address.data
        zipcode = form.zipcode.data
        state = form.state.data
        city = form.city.data

        checkIfUserExistsQuery = "SELECT * FROM users WHERE email = '{email}';"

        enrollUserQuery = "INSERT INTO users VALUES ('{email}', '{pwd}', '{fname}', '{lname}'); "

        enrollUserAddressInfoQuery = "INSERT INTO address_info VALUES ('{email}', '{address}', {zipcode}, '{state}', '{city}');"

        cursor.execute(checkIfUserExistsQuery.format(email=email))
        print(cursor.rowcount)
        print(email)

        if cursor.rowcount > 0:
            print('Account with this email already exists')
        else:
            cursor.execute(enrollUserQuery.format(email=email, pwd=pwd, fname=fname, lname=lname))

            cursor.execute(enrollUserAddressInfoQuery.format(email=email, address=address, zipcode=zipcode, state=state, city=city))
            db.commit()
            print("Successfully enrolled user.")
            passed = True


    except mysql.connector.Error as e:
        db.rollback()
        print('Failed to insert data into MySQL table', e)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print('MySQL connection is closed')
        if passed:
            return True, email
        else:
            return False, None