def user_pizza(collection):
    user_input = input("Add a pizza: ")
    if user_input in collection:
        return collection
    else:
        collection = (*collection, user_input)
        return collection


def pizza_print(collection):
    print(f"------LISTE DE PIZZAS ({len(collection)})--------")
    if not collection:
        print("Aucune Pizza")
        return
    new_collection = user_pizza(collection)
    for i in new_collection:
        print(i)
    print()
    print("First pizza : " + collection[0])
    print("Last pizza : " + collection[-1])


pizzas = ["Regina", "Végé", "MeatBall", "Cheese"]
vide = ()
pizza_print(pizzas)
