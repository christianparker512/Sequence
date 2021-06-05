shopping_list = ["milk",
                 "pasta",
                 "grapes",
                 "yogurt",
                 "granola",
                 "watermelon",
                 "peaches",
                 "strawberries",
                 "coffee"
                  ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list +=["brownies"]
print(shopping_list)