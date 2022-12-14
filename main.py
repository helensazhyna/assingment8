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
    medals = [0, 0, 0] #g - s - b
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
        while True:
            line = input_file.readline().split('\t')
            if len(line) == 1:
                break
            if line[14] != 'NA\n' and line[9] == year:
                if line[6] not in result.keys():
                    result[line[6]] = [0, 0, 0] #g - s - b
                if line[14] == 'Gold\n':
                    result[line[6]][0] +=1
                elif line[14] == 'Silver\n':
                    result[line[6]][1] +=1
                elif line[14] == 'Bronze\n':
                    result[line[6]][2] +=1
    return result

if arguments.medals:
    medal_result = medal(arguments.medals[0], arguments.medals[1])
    print(medal_result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(medal_result)

if arguments.total:
    total_result = total(arguments.total)
    result = ''
    for key in total_result:
        result += '\n' + str(key) + ': Gold - ' + str(total_result[key][0]) + ', Silver - ' + str(total_result[key][1]) + ', Bronze - ' + str(total_result[key][2])
        print(result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(result)
