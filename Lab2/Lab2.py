def main():
   welcome_menu()
   numbers = get_num()
   if numbers:
        max_num = max(numbers)
        min_num = min(numbers)
        average_num = calculate_average(numbers)
        display_results(average_num, max_num, min_num)
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

def display_results(average_num, max_num, min_num):
    print("\nTemperature Analysis Results:")
    print(f"Average Number: {average_num:.2f}")
    print(f"Minimum Number: {min_num}")
    print(f"Maximum Number: {max_num}")

if __name__ == "__main__":
    main()

