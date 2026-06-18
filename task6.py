people = {"Alex":25, "Emma":15,"Lucas":8,"Sophia":42}
def check_age (value):
    if value>=20:
        return "adult"
    elif 19>= value>=13:
        return "teen"
    else:
        return "Child"
    
desc_people = {key: check_age(value)for (key,value)in people.items()}
print(desc_people)

