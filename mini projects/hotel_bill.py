bill = float(input("Total Bill:- "))
tip_percentage = float(input("Tip percentage:- "))
people = int(input("No. of people splitting:- "))

tip_decimal = tip_percentage / 100
tip_amount = bill * tip_decimal
total_amount = tip_amount + bill
splitting_divide = total_amount / people
print("===========BILL===========\n")
print(f"Total Bill = {bill}")
print(f"Tip Percentage = {tip_percentage}% \n Total Amount = {total_amount}")
print(f"No. of People splitting = {people} \n Per person = {splitting_divide:.2f}")
