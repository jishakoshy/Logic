#  Question:
# string = "airtel:01, vodafone: 02, idea: 03, airtel:04, idea: 05, airtel:06"
# Output:
# 'airtel': ['01', '04', '06'], 'vodafone': ['02'], 'idea': ['03', '05']

string = "airtel:01, vodafone: 02, idea: 03, airtel:04, idea: 05, airtel:06"
list1 =[]
dict1 =  {(key,value) for key,value in enumerate(string) if list1.append(value)}
print(dict1)

