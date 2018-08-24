# CPSC-442-11/Python  - Assignment 1, Problem 2
# Author:  Wofford, Juana 1014901
#
# Program calculates and displays wholesale price for 40 copies
# of books for the following problem:
#
# The cover price of a book is $25, but bookstores get a 10% discount.
# Shipping costs $2  for the first five copies and 2.75 cents for
# all rest of copies.


# using .format to format string price
book_price = 25
percentage = 0.1
shipping_costs_five = 2
shipping_costs_remainder = 2.75
# total of 40 books to ship
# multiply the shipping cost for five books
shipping_five_books = (5 * book_price) + (shipping_costs_five * 5)

# multiply the shipping costs for (over 5) remaining books
shipping_thirtyfive_books = (35 * book_price) + (shipping_costs_remainder * 35)

# calculate the total wholesale amount, 40 books; price, plus shipping
total_wholesale_amount = (shipping_five_books + shipping_thirtyfive_books)

# calculate the savings amount
savings = total_wholesale_amount * percentage

# calculate the total wholesale with discount amount
total_whlse_wdiscount = total_wholesale_amount - savings

# print the information
print('Book Cover Price: '+'${:,.2f}'.format(book_price))
print('Bookstores get 10% discount')
# print('Savings: '+'${:,.2f}'.format(savings))
print('Shipping Costs for first 5 Books is $2 per Book: '+
      '${:,.2f}'.format(shipping_five_books))
print('Shipping Costs for 35 Books is $2.75 per Book: '+
      '${:,.2f}'.format(shipping_thirtyfive_books))
print('Total Wholesale Cost for 40 copies:   '+
      '${:,.2f}'.format(total_wholesale_amount))
print('Total Wholesale Cost with 10% Discount: '+
      '${:,.2f}'.format(savings) + ' Savings, Brings Total Cost to: ' +
      '${:,.2f}'.format(total_whlse_wdiscount))