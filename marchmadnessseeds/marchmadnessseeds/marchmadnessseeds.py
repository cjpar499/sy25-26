seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

name_map = dict(zip(seeds, winners))

upset_count = 0

for seed in seeds:
   if seed >= 10:
       print("Cinderella alert: " + name_map[seed] + " pulls the the upset")
       upset_count += 1

print("Total upsets: " + str(upset_count))