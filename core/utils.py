import os
import random

from django.core.cache import cache
from django.conf import settings
from .search.tree import BPlusTree

# Utility functions

def random_products():    
    file = open(settings.PATH_FILE, 'a')
    for i in range(300):
        product_id = random.randint(100, 1000)
        price = random.randint(1000, 10000)
        file.write('{0} {1}'.format(product_id, price))
        file.write('\n')
    file.close()

def load_tree():
    print('Initializing B+ tree...')
    bplustree = BPlusTree(order=5)

    position = 1
    with open(settings.PATH_FILE, 'r') as file:
        for line in file:
            bplustree.insert(line.split()[0], position)
            position += 1
    bplustree.show()

    # Tree in memory
    cache.set('bplustree', bplustree, 600)

def search_by_position(position):
    with open(settings.PATH_FILE, 'r') as file:
        for line in file:
            if line.startswith(position):
                return line.split()[0], line.split()[1], position
    return None

def append_product_to_file(product_id, price):
    file = open(settings.PATH_FILE, 'a')
    file.write('{0} {1}'.format(product_id, price))
    file.write('\n')
    file.close()

def count_file():
    count = 0
    with open(settings.PATH_FILE, 'r') as file:
        for line in file:
            count += 1
    return count

def is_exist(product_id):
    position = 1
    with open(settings.PATH_FILE, 'r') as file:
        for line in file:
            if line.split()[0] == str(product_id):
                return True
            position += 1
    return False
