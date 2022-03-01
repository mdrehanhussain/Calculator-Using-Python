num_1, type, num_2 = input("Enter Numbers: ").split()
num_1 = int(num_1)
num_2 = int(num_2)
add = f"{num_1} + {num_2} = {num_1 + num_2}"
sub = f"{num_1} - {num_2} = {num_1 - num_2}"
multiply = f"{num_1} x {num_2} = {num_1 * num_2}"
divide = f"{num_1} ÷ {num_2} = {num_1 / num_2}"
if(type == "+"):
        print(add)
elif(type == "-"):
        print(sub)
elif(type == "x"):
        print(multiply)
elif(type == "÷"):
        print(divide)
else:
    print(f"Error 404 {type} Not Defined")
# Note: to type ÷ symbol press (alt+0247)
