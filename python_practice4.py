def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
number1 = 10
number2 = 20
number3 = 30

print(max_num(number1, number2, number3))




def mult_list(numbers):
    result = 1  

    for num in numbers:
        result *= num

    return result


the_list = [2, 3, 4, 5]
result = mult_list(the_list)
print(f"The product of all numbers in the list is: {result}")


def rev_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string


original_string = "Hello, World!"
reversed_str = rev_string(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_str}")


def num_within(number, range_start, range_end):
    if range_start <= number <= range_end:
        return True
    else:
        return False




number_to_check = 5
start_of_range = 1
end_of_range = 10

if num_within(number_to_check, start_of_range, end_of_range):
    print(f"{number_to_check} falls within the range [{start_of_range}, {end_of_range}]")
else:
    print(f"{number_to_check} does not fall within the range [{start_of_range}, {end_of_range}]")
