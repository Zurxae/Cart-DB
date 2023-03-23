import mysql.connector

def editUserInfo(form, config, email):
    passed = False
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        fname = form.fname.data
        lname = form.lname.data
        address = form.address.data
        zipcode = form.zipcode.data
        state = form.state.data
        city = form.city.data

        updateUserQuery = "UPDATE users SET fname = '{fname}', lname = '{lname}' WHERE email = '{email}';"
        updateAdressInfoQuery = "UPDATE address_info SET address = '{address}', zipcode = {zipcode}, state = '{state}', city = '{city}' WHERE email = '{email}';"

        cursor.execute(updateUserQuery.format(fname=fname, lname=lname, email=email))
        cursor.execute(updateAdressInfoQuery.format(address=address, zipcode=zipcode, state=state, city=city, email=email))
        db.commit()

        print("Columns for {email} updated".format(email=email))
        passed = True

    except mysql.connector.Error as e:
        print('Error updating row in MySQL table', e)
    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print('MySQL connection is closed !!!!')
        return passed