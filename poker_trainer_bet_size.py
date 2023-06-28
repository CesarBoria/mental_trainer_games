import random

def generate_random_number_list():
    num_numbers = random.randint(2, 5)  # Randomly determine the number of numbers in the list
    number_list = [20]  # Initialize the list with the first random number

    for _ in range(num_numbers - 1):
        previous_number = number_list[-1]
        if random.random() < 0.2:
            new_number = previous_number  # 20% of the time, use the same number as the previous one
        else:
            min_value = previous_number * 2
            max_value = 3 * min_value if min_value <= 1000 else min_value

            if min_value > max_value:
                new_number = previous_number  # Keep the previous number if the range is empty
            else:
                new_number = random.randint(min_value, max_value)
                if new_number > 1000:
                    new_number = 1000  # If the number exceeds 1000, set it to 1000

        number_list.append(new_number)

    return number_list

# Example usage
result_list = generate_random_number_list()
print("Number List:", result_list)
