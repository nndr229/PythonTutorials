def addition_and_multplication(a,b,c):
    if a < b and a < c:
        return a*(b+c)
    return "Not feasible"


print(addition_and_multplication(4,2,3))


def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1)*num


print(factorial(3))

print()


list_ = []

for i in range(1,11):
    list_.append(i)

print(list_)


list_2 = [i**2 for i in list_]

print(list_2)


for i in range(len(list_)):
    if list_[i]%2==0:
        print(f"Even number found --- {list_[i]}")




dict_shopping_cart = {"Nithin":["Carrots","Potatoes"],"Deepkumar":["Bread","Milk"]}


print()

for key,value in dict_shopping_cart.items():
    print(f"The customer name is {key} and the customer has these items --- {value}")

