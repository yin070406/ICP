import os

def read_data(filename):
    with open(filename, "r") as f:
        return f.readlines()
    
def list_to_dict(aList):
    new_dict = {}
    for i in aList:
        i = i.strip()
        fruit, price = i.split("=")
        new_dict[fruit.strip()] = float(price.strip())
    return new_dict

def cust_spend(adict):
    total = 0
    for fruit, price in adict.items():
        weight = float(input(f"How many grams of the fruit {fruit} [price:{price}]? "))
        total += weight * price
    return total

def main():
    Is_allPrices = read_data("productsList.txt")
    dict_ProductPrice = list_to_dict(Is_allPrices)
    todayOrder = []
    while True:
        customer_id = input("Please enter your customer ID [type 'end' to exit]: ")
        if customer_id.lower() == "end":
            break
        print(f"Hi, {customer_id}! Please enter the weight[in grams] for each fruit: ")
        total_amount = cust_spend(dict_ProductPrice)
        print(f"Thank you, {customer_id}! You have spent ${total_amount:.2f} in this order")
        todayOrder.append((customer_id, total_amount))
    print(f"Today's orders: {todayOrder}")

if __name__ == "__main__":
    main()