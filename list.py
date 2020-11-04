

test_list = [10,25,36,7,58,69,15,25,69]

print ("The original list is : " +  str(test_list))


res = []

for i in test_list:

    if i not in res:

        res.append(i)

  
print ("The list after removing duplicates : " + str(res))
