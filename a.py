import inheritane


def main():
    conference_table = inheritane.Furniture('Conference Table', 'Steel', 100, 35, 30, 110, 5)

    print 'Category: ' + conference_table.get_category()
    print 'Material: ' + conference_table.get_material()
    print 'Length: ' + str(conference_table.get_length())
    print 'Width: ' + str(conference_table.get_width())
    print 'Height:' + str(conference_table.get_height())
    print 'Price: ' + str(conference_table.get_price())
    print 'Quantity: ' + str(conference_table.get_quantity())

    print conference_table

main()
