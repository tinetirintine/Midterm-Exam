filename = open('sales_log.txt')
sales_records = []

def saleRecord() :
    item_name = input('Item Name: ')

    try:
        quantity = int(input('Quantity Sold: '))
        price = float(input('Price Per Unit: '))

        total = quantity * price

        sales_records.append({
            'item': item_name,
            'quantity': quantity,
            'price': price,
            'total': total
        })
        print('Sale record saved successfully.')

    except ValueError:
        print('Invalid input. Please enter a valid number.')


def viewallrecords():
    if len(sales_records) == 0:
        print('No records found.')
        return

    total_units = 0
    grand_total = 0

    for i, record in enumerate(sales_records, 1):
        print(f'\nRecord #{i}')
        print(f'Item Name: {record["item"]}')
        print(f'Quantity Sold: {record["quantity"]}')
        print(f'Price Per Unit: ₱{record["price"]:.2f}')
        print(f'Total Sale: ₱{record["total"]:.2f}')

        total_units += record['quantity']
        grand_total += record['total']

    print('       SUMMARY STATISTICS         ')
    print(f'Total Units Sold: {total_units}')
    print(f'Grand Total Revenue: ₱{grand_total:.2f}')


def deleteRecords():
        print('All records cleared. No records remaining.')


def exit():
    print('Thank you for using the Sales Record Management System.')


while True:
    print('========================================')
    print('     SALES RECORD MANAGEMENT SYSTEM     ')
    print('========================================')
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')
    print('========================================')
    select = input('Select an Option (1-4):')

    if select == '1':
        saleRecord()

    elif select == '2':
        viewallrecords()

    elif select == '3':
        deleteRecords()

    elif select == '4':
        exit()
        break

    else:
        print('Invalid option. Please select 1-4.')
