def main():
   welcome_menu()
   numbers = get_num()
   if numbers:
        max_num = max(numbers)
        min_num = min(numbers)
        average_num = calculate_average(numbers)
        median_num = calc_median_number(numbers)
        display_results(average_num, max_num, min_num, median_num)
   else:
        print("No numbers input")

def welcome_menu():
    print("Welcome to average calculator")
    print("Please enter a list of temperature values separated by commas.")

def get_num():
    try:
        numbers_input = input("Input your values: ")
        numbers = [float(num.strip()) for num in numbers_input.split(",")]
        return numbers
    except ValueError:
        print("Wrong input values")
        return []

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
def calc_median_number(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        # If the length is even, calculate the average of the middle two numbers
        middle_index = length // 2
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        # If the length is odd, take the middle number
        median = sorted_numbers[length // 2]
    return median

def display_results(average_num, max_num, min_num, median_num):
    print("\nTemperature Analysis Results:")
    print(f"Average Number: {average_num:.2f}")
    print(f"Minimum Number: {min_num}")
    print(f"Maximum Number: {max_num}")
    print(f"Median Number: {median_num}")

if __name__ == "__main__":
    main()

