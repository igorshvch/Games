import math
import random

MESSAGES = {
    'init':''
}

def init_rand(seeed):
    random.seed(a=seeed)

class Population():
    def __init__(self):
        self.all_gens = {
            'analysis', 'strength', 'art', 'vitality'
        }

POP = Population()

class Person():
    def __init__(self):
        self.gens=None
        self.status='ALIVE'
        self.age=0
        self.fertil = True if self.age > 14 and self.age < 45 else False

    def __call__(self, gens=None, age=None):
        if not gens:
            self.gens = {attr:random.choice(range(-5,6,2)) for attr in POP.all_gens}
        if not age:
            self.age = random.randint(20, 100)
        self.fertil = True if self.age > 14 and self.age < 45 else False

class Mutations():
    def __init__(self):
        pass
    
    def rand_mut(self, person):
        gen_mut = random.choice(POP.all_gens)
        if person.age < 30:
            person.gens[gen_mut] += random.randint(-2, 2)
        elif person.age < 60:
            person.gens[gen_mut] += random.randint(-5, 5)
        elif person.age < 90:
            person.gens[gen_mut] += random.randint(-10, 10)
    
    def crosover(self, parent1, parent2):
        new_born = Person()
        new_gens = {}
        for gen in parent1.gens:
            new_gens[gen] = parent1.gens[gen] + parent2.gens[gen]
        new_born.gens = new_gens
        return new_born


        
class Environment():
    def __init__(self):
        pass