text_dict = {"Codingal": 2 , "is" :2 , "the":2 ,"best":2,"for":2,"coding":1}
print("The original dictionary :"+str(text_dict))
K = 2
res = 0
res = 0
for key in text_dict:
  if text_dict[key] == K:
    res = res + 1
print("Frequency of K is: "+str(res))