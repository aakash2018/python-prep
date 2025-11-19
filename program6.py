# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 13:23:09 2025

@author: Aakash
"""
import math

radius = float(input("enter the radius of circle"))

class perimeterOfCircle:
    def __init__(self,radius):
        self.radius = radius
    def compute(self):
        return 2 * math.pi * self.radius
    
result = perimeterOfCircle(radius)

print(f"the perimeter of circle {result.compute():.2f}")