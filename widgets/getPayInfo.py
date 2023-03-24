import mysql.connector

def getPayInfo(config, email):
    passed = False

    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        getPayInfoQuery = "SELECT card_number, cvc FROM payment_info where email = '{email}';"
        cursor.execute(getPayInfoQuery.format(email=email))
        getPayList = cursor.fetchone()
        if(cursor.rowcount > 0):
            print("Payment Info Doesn't Exist.")
            passed = True

    except mysql.connector.Error as e:
        print('Error reading data from MySQL table', e)
    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print('MySQL connection is closed')
        if passed:
            return (getPayList, passed)
        else:
            return (None, passed)
