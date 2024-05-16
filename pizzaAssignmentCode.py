import select
total_cost = 0
receipt = open('receipt.txt', 'a')
 
def select_pizza(total_cost, receipt):
    pizza_size = input('What size pizza would you like? Small for \xA35.50, medium for \xA37.90 or large for \xA312.00: ').lower()
    cost = 0.0
    available_toppings = ['pepperoni', 'mushroom', 'extra cheese', 'sausage', 'onion', 'black olives', 'green pepper', 'fresh garlic', 'tomato', 'fresh basil']
    toppings = []
    total_cost = 0
    receipt = open('receipt.txt', 'a')
 
    while cost == 0.0:
        if pizza_size == 'small':
            cost += 5.5
        elif pizza_size == 'medium':
            cost += 7.9
        elif pizza_size == 'large':
            cost += 12
        else:
            pizza_size = input('Please enter small, medium or large: ')
    print('\n')
    for i in available_toppings:
        print(i)
            
    more_toppings = input('\nWould you like any of these toppings? It costs \xA30.75 per topping. Please enter "no" or one of the toppings: ').lower()
    while more_toppings != 'no':
        if more_toppings in available_toppings:
            cost += 0.75
            toppings.append(more_toppings)
            more_toppings = input('Would you like any more toppings? Please enter "no" or one of the toppings: ').lower()
        else:
            more_toppings = input('Please enter a valid topping from the list or "no": ').lower()
    total_cost += cost
    cost = format(cost, '.2f')
        
    if toppings == []:
        print('Your pizza costs \xA3' + str(cost) + '. It is a ' + pizza_size + ' pizza with no toppings')
        receipt.write('\n - One ' + pizza_size + ' pizza with no toppings. The pizza costs \xA3' + str(cost) + '\n')
    else: 
        print('Your pizza costs \xA3' + str(cost) + '. It is a ' + pizza_size + ' pizza with ' + str(toppings))
        receipt.write('\n - One ' + pizza_size + ' pizza with: ' + str(toppings) + '. The pizza costs \xA3' + str(cost) + '\n')

   
 
def more_pizzas(total_cost, receipt):
    select_pizza(total_cost, receipt)
    more_pizza = input('Would you like to add an additional pizza to your order? Yes or no: ').lower()


    while more_pizza != 'no':
        if more_pizza == 'yes':
            select_pizza(total_cost, receipt)
            more_pizza = input('Would you like to add an additional pizza to your order? Yes or no: ').lower()
        else:
            more_pizza = input('Would you like to add another pizza to your order? Please type "yes" or "no" ').lower()
    delivery = input('Would you like delivery for \xA33.75? Yes or no: ').lower()

    acceptable_answers = ['yes', 'no']

    while delivery not in acceptable_answers:
        delivery = input('Would you like delivery for \xA33.75? Please enter yes or no: ').lower()
        
    if delivery == 'yes':
        total_cost += 3.75
        receipt.write('\nDelivery: \xA33.75. \n')
    elif delivery == 'no':
        total_cost += 0.0

        
    total_cost = format(total_cost, '.2f')
    receipt.write('\nYour order total is: \xA3' + str(total_cost))
    receipt = open('receipt.txt', 'r')
    print(receipt.read())

 
more_pizzas(total_cost, receipt)
