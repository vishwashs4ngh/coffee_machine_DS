# # class Cars:
# #     Company = "Tokyo Drift"

# #     def __init__(self, brand, color, mileage):
# #         self.brand = brand
# #         self.color = color
# #         self.mileage = mileage

# #     def category(self):
# #         if self.mileage >= 25:
# #             return "Fuel Efficient"
# #         elif self.mileage >= 15:
# #             return "Moderate Mileage"
# #         else:
# #             return "Low Mileage"

# #     def __repr__(self):
# #         return f"Cars(brand='{self.brand}', mileage='{self.mileage}', color='{self.color}')"


# # c1 = Cars("Toyota", "White", 28)
# # c2 = Cars("BMW", "Black", 12)

# # print(c1.category())
# # print(c2.category())
# # print(c1.Company)
# # print(c2)



# # from abc import ABC, abstractmethod
# # # Abstract Class
# # class Car(ABC):
# #     def __init__(self, color, mileage):
# #         # Encapsulation
# #         self.__color = color
# #         self.__mileage = mileage
# #     # Getter methods
# #     def get_color(self):
# #         return self.__color
# #     def get_mileage(self):
# #         return self.__mileage
# #     # Abstract method (Polymorphism)
# #     @abstractmethod
# #     def get_info(self):
# #         pass
# # # Inheritance
# # class Tesla(Car):
# #     # Polymorphism - own implementation
# #     def get_info(self):
# #         return f"Tesla Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"
# # class BMW(Car):
# #     # Polymorphism - own implementation
# #     def get_info(self):
# #         return f"BMW Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"
# # class Audi(Car):
# #     # Polymorphism - own implementation
# #     def get_info(self):
# #         return f"Audi Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"
# # # Objects
# # car1 = Tesla("Red", 500)
# # car2 = BMW("Black", 400)
# # car3 = Audi("White", 450)

# # # Polymorphism - same method name, different implementations
# # cars = [car1, car2, car3]
# # for car in cars:
# #     print(car.get_info())



# from abc import ABC, abstractmethod

# # Abstract Class
# class Car(ABC):
#     def __init__(self, color, mileage):
#         # Encapsulation
#         self.__color = color
#         self.__mileage = mileage

#     # Getter methods
#     def get_color(self):
#         return self.__color

#     def get_mileage(self):
#         return self.__mileage

#     # Abstract method
#     @abstractmethod
#     def get_info(self):
#         pass


# # Inheritance
# class Tesla(Car):
#     def get_info(self):
#         return f"Tesla Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"


# class BMW(Car):
#     def get_info(self):
#         return f"BMW Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"


# class Audi(Car):
#     def get_info(self):
#         return f"Audi Car of Color: {self.get_color()}, Mileage: {self.get_mileage()} km"


# # Objects
# car1 = Tesla("Red", 500)
# car2 = BMW("Black", 400)
# car3 = Audi("White", 450)

# # Store objects in list
# cars = [car1, car2, car3]


# for i, car in enumerate(cars):
#     print(f"Car {i+1}: {car.get_info()}")

# l = [20,30,40,50,60]
# l2 = [1,2,3,4,5]

# l3 = [l ]+ [l2]
# print(l3[1][2])
# print(l3)
# import numpy as np
# l = [20,30,40,50,60,70,80,90,100]
# l2 = [1,2,3,4,5,6,7,8,9,10]

# l3 = [l ]+ [l2]
# print(l3[1][2])
# print(l3)
# import numpy as np
# s=[[1,2,3],[3,4,5],[5,6,7]]
# # v1=np.array([10,20,30,40,50,60,70,80,90,100])
# s1=np.array(s)
# print(s1)
# print(s1[2])
# print(s1[-1])
# print(s1[1][1])
# print(s1[1][-1])
# print(s1[-1][-2])
# print(s1[1][0])
# s1[0][0]=120
# s2=(s1+s1)
# print(s2)
# print([[s1][s1]])


# print(v1[v1>50])
# print(v1+50)
# print(v1*2)
# print(v1[1:5])
# print(v1[::-1])
# print(v1[0:5:-1])


import numpy as np

s = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

# Convert list into NumPy array
s1 = np.array(s)

print(s1)

print(s1[2])        # Third row
print(s1[-1])       # Last row
print(s1[1][1])     # Element at row 1, column 1
print(s1[1][-1])    # Last element of second row
print(s1[-1][-2])   # Second last element of last row
print(s1[1][0])     # First element of second row

# Modify first element
s1[0][0] = 120

# Add array with itself
s2 = s1 + s1

print(s2)

# Correct way to print arrays together
ss= [s1, s1]
print(ss)
print(ss[0][0][0])  



