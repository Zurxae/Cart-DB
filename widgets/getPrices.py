import mysql.connector

def getPrices(final_items, final_count, config):
    passed = False

    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor(buffered=True)

        getItemPricesQuery = "SELECT price FROM items WHERE item_name = '{item}';"
        
        total_amount = 0
        item_prices = [] 

        print("~~~ Before For loop ~~~")

        for i in range(len(final_items)):
            cursor.execute(getItemPricesQuery.format(item=final_items[i]))
            price = cursor.fetchone()
            item_prices.append(price[0])
            total_amount += price[0] * final_count[i]

        print("~~~ After For Loop ~~~")

        passed = True

    except mysql.connector.Error as e:
        print('Failed to insert data into MySQL table', e)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print('MySQL connection is closed')
        if(passed):
            return(item_prices, total_amount)
        else:
            print("Failed to get prices")
            return(None, None)


