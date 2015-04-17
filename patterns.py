import csv
import requests
import json

with open('data/test_pids.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    pid_list = []
    for row in csvreader:
        pid_list.extend(row)	

result_pattern_list = []

for i in range(len(pid_list) - 1):
    for j in range(i+1, len(pid_list)):
        api_url = 'http://eculture2.cs.vu.nl:1234/get_patterns_between_programmes?pid='+pid_list[i]+'&pid='+pid_list[j]+'&indent=true'
        r = requests.get(api_url)
        r_2_string = str(r.content, 'utf-8')
        print("compare ", pid_list[i]," with ", pid_list[j], "result: ", r_2_string)		
        if r_2_string != '[]':
            result_pattern_list.append(r_2_string)		
		
print(result_pattern_list)

with open('results/patterns.json', 'w') as outfile:     
     json.dump(result_pattern_list, outfile, sort_keys = False, indent = 4,ensure_ascii=False)

	 
	 
	 
	 
	 
	 
#### OLD ###########	 
# for pid in range(0,200):        
    # if pid == 0:                
        # pid += 1        
    # if pid != 0:
        # other_pid = pid_list[pid]		
    # api_url = 'http://eculture2.cs.vu.nl:1234/get_patterns_between_programmes?pid='+first_pid+'&pid='+other_pid+'&indent=true'
    # r = requests.get(api_url)
    # r_2_string = str(r.content, 'utf-8')
    # print("compare: ", first_pid, "with: ", other_pid, "check results: ", r_2_string)
    # if r_2_string != '[]':    
        # result_pattern_list.append(r_2_string)    
        