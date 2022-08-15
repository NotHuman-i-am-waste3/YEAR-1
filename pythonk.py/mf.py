n = int(input())
# Empty dictionary
customers = {}
for i in range(n):
    inp = input().split()
    # First item is id
    cust_id = inp[0]
    # convert the rest of the items to a set
    cust_set = set(inp[1:])
    customers[cust_id] = cust_set
print(customers)
    
max_items = set()
max_index = None

# Now we compare

for id2 in customers:
        if id1 != id2:
            # Intersection consists of the common items
            common_items = customers[id1].intersection(customers[id2])
            if len(common_items) > len(max_items):
                max_items = common_items
                max_index = (str(id1),str(id2))
print(" ".join(sorted(max_index)))
print(" ".join(sorted(max_items)))
print(len(max_items))