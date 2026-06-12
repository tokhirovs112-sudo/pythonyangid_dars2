class Restaurant:
    def __init__(self, name, work_time, menu):
        self.name = name
        self.work_time = work_time
        self.menu = menu 
    
    def add_food(self, food): 
        self.menu.append(food)
    
    def get_work_time(self):
        return self.work_time

restaurant = Restaurant("Saroy", "09:00 - 23:00", ["Osh", "Somsa"])
restaurant.add_food("Laghman")
print(restaurant.get_work_time())
print(restaurant.menu)