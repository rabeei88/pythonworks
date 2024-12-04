orders=["tea","coffee","tea","coffee","porotta","plaindosa","roast"]
orders_summary={}
for ord in orders:

    if ord in orders_summary:

        orders_summary[ord]+=1
    else:
      orders_summary[ord]=1
print(orders_summary)