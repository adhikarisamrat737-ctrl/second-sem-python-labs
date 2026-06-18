cities_in_f = {"NewYork":"32","Boston":"75","LosAngeles":"100","Chicago":"50"}
cities_in_c = {key:(value-32)*(5/9) for (key,value)in cities_in_f.items()}
print(cities_in_c)
