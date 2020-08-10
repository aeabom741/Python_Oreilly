day = ['Monday','Tuseday','Wendnesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
dessert = ['tiramisu','ice cream' ,'pie','pudding']

for day,fruits,drinks,dessert in zip(day,fruits,drinks,dessert):
    print(day,": drink",drinks, " - eat",fruits,"- enjoy", dessert )