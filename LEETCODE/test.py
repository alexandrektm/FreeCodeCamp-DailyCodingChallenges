import random

# Function to generate random buy and sell lists
def generate_buy_sell_lists(num_items, max_price=10, max_budget=100):
    buy_list = [random.randint(1, max_price) for _ in range(num_items)]
    sell_list = [random.randint(buy + 1, buy + max_price) for buy in buy_list]  # Sell price > Buy price
    budget = random.randint(10, max_budget)
    
    return buy_list, sell_list, budget

# Generate random buy and sell lists for testing
num_items = 10
buy_list, sell_list, budget = generate_buy_sell_lists(num_items)

print("Buy List:", buy_list)
print("Sell List:", sell_list)
print("Budget:", budget)