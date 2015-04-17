import requests
import json
import csv

with open('patterns/pid_with_patterns_excel.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    pid_list_row_0 = []
    pid_list_row_1 = []
    for row in csvreader:
        pid_list_row_0.append(row[0])
        pid_list_row_1.append(row[1])

pid_program_row1 = []
pid_program_row2 = []

for i in range(len(pid_list_row_0)):
    string_result = pid_list_row_0[i]
    l2s_result = str(string_result)
    test = l2s_result[32:-10]
    pid_program_row1.append(test)

for i in range(len(pid_list_row_1)):
    string_result = pid_list_row_1[i]
    l2s_result = str(string_result)
    test = l2s_result[32:-10]
    pid_program_row2.append(test)

remove_duplicates_row1 = list(set(pid_program_row1))
remove_duplicates_row2 = list(set(pid_program_row2))

in_first = set(remove_duplicates_row1)
in_second = set(remove_duplicates_row2)

in_second_but_not_in_first = in_second - in_first

combined_list = remove_duplicates_row1 + list(in_second_but_not_in_first)

print(len(combined_list), combined_list)

# variables
pid_genre = []
pid_format = []
pid_title = []
pid_subtitle = []
pid_medsyn = []
pid_first_broadcast_date = []
pid_result = []

# headers
headers = {
    'User-Agent': 'VU student'
}

for i in range(len(combined_list)):
    r = requests.get('http://www.bbc.co.uk/programmes/' + combined_list[i] + '.json', headers=headers)
    json_data = r.json()
    pid_displaytitle = str(json_data["programme"]["display_title"]["title"])
    pid_subtitle = str(json_data["programme"]["display_title"]["subtitle"])
    pid_first_broadcast_date = str(json_data["programme"]["first_broadcast_date"])
    pid_mediumsyn_bbc = str(json_data["programme"]["medium_synopsis"])
    pid_medsyn.append(pid_mediumsyn_bbc)
    length_cat = len(json_data["programme"]["categories"])
    for j in range(length_cat):
       if 'genre' in json_data["programme"]["categories"][j]["type"]:
           pid_genre_bbc = str(json_data["programme"]["categories"][j]["title"])
           pid_genre.append(pid_genre_bbc)
       if 'format' in json_data["programme"]["categories"][j]["type"]:
           pid_format_bbc = str(json_data["programme"]["categories"][j]["title"])
           pid_format.append(pid_format_bbc)
    pid_result.append([combined_list[i],pid_displaytitle,pid_subtitle,pid_first_broadcast_date,pid_genre_bbc,pid_format_bbc,pid_mediumsyn_bbc])
    #pid_result.append([combined_list[i]])
    #print(pid_title, pid_genre)

print(pid_result)


with open('csv_per_cat/pids.csv', 'wb', ) as fp:
    a = csv.writer(fp, delimiter=',')
    data = pid_result
    a.writerows(data)