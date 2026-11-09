#WAP to fill in a letter template given below with name and date.

letter='''Dear {name},
       You are selected!
       {date}'''

print(letter.replace('{name}', 'John').replace('{date}', '2023-10-10'))