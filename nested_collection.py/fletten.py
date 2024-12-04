arr=[

    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

flat_list=[num for ls in arr for num in ls]
print(flat_list)


#greater than 25
flat_gt_25=[num for ls in arr for num in ls if num>25]
print(flat_gt_25)