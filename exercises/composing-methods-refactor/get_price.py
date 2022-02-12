# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.

def base_price():
    quantity = int(input("How many items? "))
    item_price = float(input("Price per item: "))
    return quantity * item_price

def get_price():
    total_price = base_price()
    if total_price > 1000:
        return total_price * 0.95
    else:
        return total_price * 0.98

get_price()