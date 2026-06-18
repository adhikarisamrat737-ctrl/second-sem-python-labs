#List comprehension that takes a list of a numbers and creates a list that creates a dictionary where each number is a key and its square number is a value 
list_numbers = [1,2,3,4,5]
dict_form = {key: key**2 for key in list_numbers }
print(dict_form)

prices = {"apple":"1.00","banana":"2.00","kiwi":"5.00"}
dict_prices={key: value*2 for (key,value) in prices.items()}
print(dict_prices)

