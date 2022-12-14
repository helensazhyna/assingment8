import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source', help='File choosing')
parser.add_argument('-medals', help='Medals. Usage: -m country/country_code year', nargs=2)
parser.add_argument('-output', help='Output in file. Usage: -o filename.txt')
parser.add_argument('-total', help='Total statistics. Usage: -t year')

arguments = parser.parse_args()
#print(arguments)

path = arguments.source
output_path = arguments.output

def medal(country, year):
    result = ''
    count = 0
    medals = [0, 0, 0] #gold - silver - bronze
    with open(path, 'r') as input_file:
        line = input_file.readline()
        while line and count != 10:
            line = line.split('\t')

            if line[14] != 'NA\n' and (country == line[6] or country == line[7]) and year == line[9]:
                count += 1
                if line[14] == 'Gold\n':
                    medals[0] += 1
                elif line[14] == 'Silver\n':
                    medals[1] += 1
                else:
                    medals[2] += 1

                result_line = line[1] + '  -  ' + line[13] + '  -  ' + line[14]
                result += result_line

            line = input_file.readline()

    result += 'Gold: ' + str(medals[0]) + ', Silver: ' + str(medals[1]) + ', Bronze: ' + str(medals[2])
    if count == 0:
        return 'Not found medals or input data is invalid'
    elif count < 10:
        return 'Not enough medals'
    return result

def total(year):
    result = {}
    with open(path, 'r') as input_file:
        line = input_file.readline()
        while line:
            line = input_file.readline().split('\t')
            if line[14] != 'NA\n' and line[9] == year:
                if result[line[6]] is None:
                    result[line[6]] = [0, 0, 0] #g - s - b
                    if line[14] == 'Gold\n':
                        result[line[6]][0] +=1
                    elif line[14] == 'Silver\n':
                        result[line[6]][1] +=1
                    elif line[14] == 'Bronze\n':
                        result[line[6]][2] +=1
                else:
                    if line[14] == 'Gold\n':
                        result[line[6]][0] +=1
                    elif line[14] == 'Silver\n':
                        result[line[6]][1] +=1
                    elif line[14] == 'Bronze\n':
                        result[line[6]][2] +=1

    return result

#country 6 - gold - silver - bronze    year9

# 1 - name
# 6 - country
# 7 - country code
# 9 - year
# 13 - game
# 14 - medal

if arguments.medals:
    medal_result = medal(arguments.medals[0], arguments.medals[1])
    print(medal_result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(medal_result)

if arguments.total:
    total_result = total(arguments.total)
    print(total_result)
