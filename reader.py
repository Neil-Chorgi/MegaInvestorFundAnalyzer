import csv
def in_list(obj,list):
    for i in list:
        print(i)
        if obj in i[0]:
            return list.index(i)
    #return -1

file = open("funds.csv")
csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
rows = []
item_count_list =[['MSFT',0],['AAPL',0]]
#print(item_count_list[0][0])

for row in csvreader:
    rows.append(row)
    for item in row:
        #print(item)
        for i in range(len(item_count_list)):
            if item in item_count_list[i]:
                #for i in item_count_list:
                item_count_list[i][1] = item_count_list[i][1] + 1
                #print(item_count_list[i][1])
                #print(type(item_count_list[i][1]))
                break
        
            elif item not in item_count_list:
                item_count_list.append([])
                x = len(item_count_list)-1
                item_count_list[x].append(item)
                item_count_list[x].append(1)
            
            
          
print(item_count_list)
        #else:
        #    print("no")
#print(rows)

file.close()