import mysql.connector

def checkout(form, config, email):
    passed = False
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)
        getItemPricesQuery = ""
        storeTransactionQuery = ""
        storeIncludeQuery = ""
    except mysql.connector.Error as e:
        db.rollback()
        print('Failed to insert data into MySQL table', e)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print('MySQL connection is closed')
        return passed

