shopping_list = []

print("After completion of your item list please ENTER 'Done or DONE' to end.")


while True:
    item = input('Select an item: ')
    if item == "DONE":
        break
    elif item == "Done":
        break
    else:
        shopping_list.append(item)
    
    

print("Your items are: ")        
for items in shopping_list:
    print(items)




