scores = {"Alice":85, "bob":62, "charlie":90, "Diana":55}
dict_scores = {key:value for (key,value)in scores.items() if value>=70}
print(dict_scores)