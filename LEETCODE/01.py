id_list =   [0,  1, 2,  3,  4, 5, 6,  7,  8,  9]
buy_list =  [2,  7, 4,  9,  7, 3, 4,  1,  7,  6]
sell_list = [6, 14, 8, 16, 10, 6, 5, 11, 15, 11]
budget = 30

profit_list = []
weight_list = []


for index, item in enumerate(buy_list):

   profit_item =  sell_list[index] - item
   weight_item = sell_list[index] / item

   profit_list.append(profit_item)
   weight_list.append(weight_item)

seek_list = list(zip(id_list,weight_list,buy_list,sell_list,profit_list))
seek_list = [x for x in seek_list if (x[1] > 0)]
seek_list = sorted(seek_list, key=lambda x: x[2])
seek_list = sorted(seek_list, key=lambda x: (x[1], x[4]), reverse=True)

total_profit = 0
selected = []

for element in seek_list:
   

    if element[4] <= 0:
        continue
   
    if element[2] <= budget:
        budget -= element[2]
        if budget <= 0:
            budget += element[2]
            continue

        total_profit += element[4]
        selected.append(element)

print(selected)
print(total_profit)
print(seek_list)