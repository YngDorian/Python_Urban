from math import inf 
def divide(first, second):
    result = first / second
    if second == 0:
        return inf
    else:
        return result
    