# """File name: nested_for_loop_mult_table.pyDescription: This snippet demonstrates: using nested for loops to generate a multiplication table"""
# #
# ROW_RANGE = 10
# COLUMN_RANGE = 10
#
# for row in range(1, ROW_RANGE+1):
#     for col in range(1, COLUMN_RANGE + 1):
#         # print(row*col)                      # what is the problem with that?
#         # #print(row*col, end='')             # what is the problem with that?
#         # #print(row*col, '\t', end='')       # what is the problem with that?
#         print("%10i" % (row * col), end='')
#     print()             # start another row

# flour_wt = 23.1234
# baking_powder_wt = 1.456
# print("%-28s%7.1f Oz" % ("Flour:", flour_wt))
# print("%-28s%7.1f Oz" % ("Baking Powder:", baking_powder_wt))
weightGrams = 980
weightOz = round(weightGrams // 28.3)
weightLb = weightOz * 16

print(weightOz)
print(weightLb)