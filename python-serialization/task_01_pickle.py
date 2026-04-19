#!/usr/bin/env python3
"""Shebang"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}".format(self.name, self.age, self.is_student))
    
    def serialize(self, filename):
        try:
            with open(filename, 'wb', encoding = 'utf-8') as f:
                pickle.dump(self, f)
        
        except Exception:
            return None
    
    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb', encoding = 'utf-8') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        