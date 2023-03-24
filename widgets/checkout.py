import mysql.connector

def checkoutOrder(config, email, final_items, final_count, form):
    passed = False


    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        getItemPricesQuery = "SELECT price FROM items WHERE item_name = '{item}';"
        storeTransactionQuery = "INSERT INTO transactions (email, amount) VALUES ('{email}', '{amount}');"

        #used to get tid of current transaction. Make sure to subtract 1 from result.
        getTidQuery = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'transactions' and table_schema = 'cart';"
        
        storeIncludeQuery = "INSERT INTO includes VALUES ('{item_name}', '{tid}', '{count}');"

        fixCacheBugQuery = "SET @@SESSION.information_schema_stats_expiry = 0;"

        storePayInfoQuery = "INSERT INTO payment_info VALUES ('{email}', '{card_number}', '{cvc}');"

        total_amount = 0

        for i in range(len(final_items)):
            cursor.execute(getItemPricesQuery.format(item=final_items[i]))
            price = cursor.fetchone()
            total_amount += price[0] * final_count[i]
        
        print("recieved prices for all items...")

        cursor.execute(storeTransactionQuery.format(email=email, amount=total_amount))

        print("inserted order into transactions table")


        #To fix cache bug
        cursor.execute(fixCacheBugQuery)

        cursor.execute(getTidQuery)
        tidRecord = cursor.fetchone()
        tid = int(tidRecord[0])
        tid -= 1

        print("Recieved tid as:", str(tidRecord[0]), 'which is the type of:', type(tidRecord[0]))

        for i in range(len(final_items)):
            cursor.execute(storeIncludeQuery.format(item_name=final_items[i], tid=tid, count=final_count[i]))

        getPayInfoQuery = "SELECT card_number, cvc FROM payment_info where email = '{email}';"
        cursor.execute(getPayInfoQuery.format(email=email))
        getPayList = cursor.fetchone()

        if(cursor.rowcount == 0):
            cursor.execute(storePayInfoQuery.format(email=email,card_number=form.card_number.data, cvc=form.cvc.data))

        db.commit()
        
        passed = True

    except mysql.connector.Error as e:
        db.rollback()
        print('Failed to insert data into MySQL table', e)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print('MySQL connection is closed')
        return passed

