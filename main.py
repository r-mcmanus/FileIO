import csv
import os

#open an existing file, reading, parsing the comma separated values into a list of lists, and closing the open file.
country_list = []
with open("data/continents.csv") as file:
    reader = csv.reader(file)
    country_list = list(reader)

#print file information to the console
print(country_list)

#determine the size of a file
print(f'The size of continents.csv is {os.path.getsize("data/continents.csv")}.')

#create a new file, write data to a file, modify data in a file, determine location within a file, append data to existing file
with open("data/continents_3.csv") as infile, open('data/continents_3_temp.csv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, lineterminator='\n')
    for line in reader:
        if line == ['Africa', 'Angola']:
            line = writer.writerow(['AFRICA', 'ANGOLA'])
            print(f'Line {reader.line_num} was modified.')
            break
        else:
            writer.writerow(line)
    writer.writerows(reader)
    writer.writerow(['Antarctica', 'Antarctica'])

#inserting data into an existing file
with open("data/continents_3.csv") as infile, open('data/continents_3_temp.csv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, lineterminator='\n')
    for line in reader:
        if reader.line_num == 4:
            next_line = line
            line = writer.writerow(['0000', '0000'])
            writer.writerow(next_line)
            print(f'Line was inserted at row {reader.line_num}.')
            break
        else:
            writer.writerow(line)
    writer.writerows(reader)

#delete a file
os.remove('data/continents_3.csv')
os.rename('data/continents_3_temp.csv', 'data/continents_3.csv')


