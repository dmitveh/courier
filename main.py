import math
import os
from re import L
import time

OrderList = [{"x": 10, "y": 10}]


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return 'Точка доставки с коодинатами {0}, {1}'.format(self.x, self.y)


class Order:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Заказ с координатами {0}, {1}'.format(self.x, self.y)


class Boy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed  # 1 значение в сек

    def walk(self, other_p):

        dist = int(math.sqrt((self.x - other_p['x']) ** 2 + (self.y - other_p['y']) ** 2))
        print(f'Курьер c координатами: x, {self.x}, y {self.y}, идёт за заказом: x, ', {other_p["x"]}, 'y, ', {other_p["y"]})
        for i in range(dist):
            print(f'Прогресс {i + 1}')
            time.sleep(self.speed)

    def find_nearest_order(self, OrderList):
        nearest_order = {}
        for other_p in OrderList:
            dist = int(math.sqrt((self.x - other_p["x"]) ** 2 + (self.y - other_p["y"]) ** 2))
            nearest_order[other_p['x'], other_p['y']] = dist
        point = sorted(nearest_order.items(), key=lambda x: x[-1])[0]
        print(f'Ближайщий заказ с дистанцией {point[1]} и координатами {point[0]}')


##for i in range(0, 10):
  ##  OrderList.append({'x': Order(i, i).x, "y": Order(i, i).y})

b1 = Boy(4, 4, 1)
b1.find_nearest_order(OrderList)
b1.walk(OrderList[0])