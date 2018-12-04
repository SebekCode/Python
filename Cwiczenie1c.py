#!/usr/bin/env python3


class Flower:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def describe_flower(self):
        print("Your flower is {} and its name is {}".format(self.color, self.name))


color = input("What color is your flower? ")
name = input("What is your flower's name? ")

flower = Flower(color, name)
flower.describe_flower()

