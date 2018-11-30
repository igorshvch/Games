# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
print('Hellow!')

import random

class Human():
    alph = [chr(i) for i in range(97, 123, 1)]
    chars = {
            'illness' : ('disease resistance', 'disease prone'),
            'intellect' : ('genius', 'untalanted', 'dumb'),
            'orientation' : ('heterosexual', 'bisexual', 'homosexual'),
            'liveness' : ('dead', 'alive'),
            'marital_status' : ('married', 'unmarried', 'divorced'),
            'employment' : ('jobless', 'employed')
            }
    
    def __init__(self, age, sex, name=None, chars=None):
        self.age = age
        self.sex = sex
        self.name = name if name else self.__create_name()
        self.chars = chars if chars else self.__create_chars()
        self.personal_history = None
    
    def __create_name(self):
        name_letters = random.choices(Human.alph, k=random.randint(3,8))
        return ''.join(name_letters).capitalize()
    
    def __create_chars(self):
        chars = {key:random.choice(Human.chars[key]) for key in Human.chars}
        return chars
    
    def __repr__(self):
        return (
                'Name: {: >8s}, age: {: >3d}, sex: {: >6s}, chars: {: >44s}'\
                .format(self.name, self.age, self.sex, self.chars)
                )
        

class City():
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def __len__(self):
        return len(self.population)
    
    def __repr__(self):
        random_citizen = str(self.population[random.randint(0, len(self)-1)])
        return (
                'City population: {: >7d}'.format(len(self))
                +'\nrandom citizen:\n'
                +'{: <37s}'.format(random_citizen)
                )
                
    def populate(self, citizen_num=10000):
        for i in range(citizen_num):
            self.population.append(
                    Human(random.randint(0,130),
                          random.choice(('male', 'female')))
                    )
        