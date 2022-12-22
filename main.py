import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source', help='File choosing')
parser.add_argument('-medals', help='Medals. Usage: -m country/country_code year', nargs=2)
parser.add_argument('-output', help='Output in file. Usage: -o filename.txt')
parser.add_argument('-total', help='Total statistics. Usage: -t year')
parser.add_argument('-overall', help='Overall max medals. Usage: -m country', nargs='*')
parser.add_argument('-interactive')  # help='Statistics of the country. Usage: -m country')
arguments = parser.parse_args()
# print(arguments)

path = arguments.source

output_path = arguments.output


def medal(country, year):
    result = ''
    count = 0
    medals = [0, 0, 0]  # g - s - b
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
                    result[line[6]] = [0, 0, 0]  # g - s - b
                if line[14] == 'Gold\n':
                    result[line[6]][0] += 1
                elif line[14] == 'Silver\n':
                    result[line[6]][1] += 1
                elif line[14] == 'Bronze\n':
                    result[line[6]][2] += 1
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
        result += '\n' + str(key) + ': Gold - ' + str(total_result[key][0]) + ', Silver - ' + str(
            total_result[key][1]) + ', Bronze - ' + str(total_result[key][2])
        print(result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(result)


# task 3
def overall(country):
    res = {}
    with open(path, "r") as input_file:
        line = input_file.readline()
        while line:
            next_line = line.split("\t")
            if country == next_line[6] or country == next_line[7]:
                if next_line[-1] != "NA\n" and next_line[9] not in res:
                    res[next_line[9]] = 1
                elif next_line[-1] != "NA\n":
                    res[next_line[9]] += 1
            line = input_file.readline()

    return res.items()


def count_medals(medals):
    gold = 0
    silver = 0
    bronze = 0
    for medal in medals:
        if "Gold\n" in medal:
            gold += 1
        if "Silver\n" in medal:
            silver += 1
        if "Bronze\n" in medal:
            bronze += 1
    print(f"amount of gold medals {gold}\namount of silver medals {silver}\namount of bronze medals {bronze} ")
    return gold + silver + bronze


def check(country):
    min_year = 2220
    with open(path, "r") as input_file:
        line = input_file.readline()
        while line != "":
            new_line = line.split("\t")
            if country == new_line[6] or country == new_line[7]:
                year = int(new_line[9])
                if year < min_year:
                    min_year = year
                    city = new_line[11]
            line = input_file.readline()
        return min_year, city


# task 4
def interactive(country):
    with open(path, "r") as input_file:
        line = input_file.readline()
        while line != "":
            next_line = line.split("\t")
            if country == next_line[6] or country == next_line[7]:
                minimal_year, place = check(country)
                year_max, maximum = max(overall(country))
                year_min, minimum = min(overall(country))
                print(f"First attendance in {minimal_year} in {place}.")
                print(f"The most successful olympiad in {year_max} had {maximum} medals.")
                print(f"The worst olympiad in {year_min} had {minimum} medals.")
                exit()
                line = input_file.readline()


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
        result += '\n' + str(key) + ': Gold - ' + str(total_result[key][0]) + ', Silver - ' + str(
            total_result[key][1]) + ', Bronze - ' + str(total_result[key][2])
        print(result)
    if output_path:
        with open(output_path, 'w') as output_file:
            output_file.write(result)

if arguments.overall:
    for country in arguments.overall:
        best_year, win_medals = max(overall(country))
        print(f"For {country} in {best_year} the biggest amount of medals is {win_medals}")

if arguments.interactive:
    country = input("Enter the country for statistics: ")
    print(interactive(country))
