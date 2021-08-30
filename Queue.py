queue =[]

def get_queue_items():
    data_input = input("Feed value for Queue: ")
    return data_input

def queue_size():
    size = input("Set size of the queue:")
    return int(size)

def add_queue_items(data):
    queue.append(data)
    print("\n Queue contents: ",queue)

def rem_queue_items():
    confirm = input("Do you really want to remove item from a queue ? (Press Y/N) ")
    if (confirm== 'Y'):
         queue.pop(0)
         print("\n Queue contents after removal: ",queue)
    else :
        print("\n Nothing deleted. Queue contents are: ",queue)


i = queue_size()

for x in range(i):
    item = get_queue_items()
    add_queue_items(item)

rem_queue_items()



