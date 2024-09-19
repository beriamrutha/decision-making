'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00

'''
cost_price = float(input())  # Total cost of a dozen bananas
selling_price = float(input())  # Selling price of one banana
total_selling_price = selling_price * 12
profit_or_loss = total_selling_price - cost_price

if profit_or_loss > 0:
    print("Profit : Rs.{:.2f}".format(profit_or_loss))
elif profit_or_loss < 0:
    print("Loss : Rs.{:.2f}".format(abs(profit_or_loss)))
else:
    print("No Profit No Loss")
