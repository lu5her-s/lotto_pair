# define the columns of the table
columns = ['ID', 'Name', 'Age']

# define the data of the table
data = [[1, 'John', 20],
        [2, 'Alice', 25],
        [3, 'Bob', 30]]

# determine the maximum width of each column
column_widths = [max(len(str(x)) for x in col) for col in zip(*data, columns)]

# create the format string for each row
row_format = '+'.join(['-' * (width + 2) for width in column_widths])

# print the top border
print(row_format)

# print the header row
print('| ' + ' | '.join(['{:^{width}}'.format(col, width=width) for col, width in zip(columns, column_widths)]) + ' |')

# print a line separator
print(row_format)

# print the data rows
for row in data:
    print('| ' + ' | '.join(['{:^{width}}'.format(cell, width=width) for cell, width in zip(row, column_widths)]) + ' |')

# print the bottom border
print(row_format)

