import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source', help='File choosing')
parser.add_argument('-m', '-medals', help='Medals. Usage: -m country/country_code year', nargs=2)
parser.add_argument('-o', '-output', help='Output in file. Usage: -o filename.txt')
parser.add_argument('-t', '-total', help='Total statistics. Usage: -t year')

arguments = parser.parse_args()

path = arguments.source
output_path = arguments.o



# 1 - name
# 6 - country
# 7 - country code
# 9 - year
# 13 - game
# 14 - medal

def check_medal(arr, country, year):
    if arr[14] != 'NA\n' and (country == arr[6] or country == arr[7]) and year == arr[9]:
        return 1
    else:
        return 0

def medal(country, year):
    result = ''
    count = 0
    lines = 0
    medals = [0, 0, 0] #gold - silver - bronze
    with open(path, 'r') as input_file:
        while count != 10:
            lines += 1
            line = input_file.readline().split('\t')

            if check_medal(line, country, year) == 1:
                if line[14] == 'Gold\n':
                    medals[0] += 1
                elif line[14] == 'Silver\n':
                    medals[1] += 1
                else:
                    medals[2] += 1

                result_line = line[1] + '  -  ' + line[13] + '  -  ' + line[14]
                result += result_line
                count += 1
                if lines == 261707 and count != 10:
                    return 'Not enough medals!'
    result += 'Gold: ' + str(medals[0]) + ', Silver: ' + str(medals[1]) + ', Bronze: ' + str(medals[2])
    return result

if len(arguments.m) == 2:
    medal_result = medal(arguments.m[0], arguments.m[1])
    print(medal_result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(medal_result)
