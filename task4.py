scores = {"Alice":85, "bob":62, "charlie":90, "Diana":55}
upper_scores = {key.upper(): value for (key,value) in scores .items()}
print(upper_scores)
