print('welcome to python pizza delivery')
size = input('what size pizza do you want? S, M, or L ')
pepperoni = input('do you want pepperoni? Y or N ')
extra_cheese = input('do you want extra cheese? Y or N ')

# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
final_price = 0

if size == 's' :
    final_price = 15
    if pepperoni == 'y':
        final_price += 2
    if extra_cheese == 'y':
        final_price +=1
elif size == 'm' :
    final_price = 20
    if pepperoni == 'y':
        final_price += 3
    if extra_cheese == 'y':
        final_price +=1
else:
    final_price = 25
    if pepperoni == 'y':
        final_price += 3
    if extra_cheese == 'y':
        final_price +=1

print(final_price)






