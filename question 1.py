def remove_duplicates(numbers):
    seen = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)

    return unique_numbers


def find_average(numbers):
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def multiply_by_scalar(numbers, scalar):
    return [number * scalar for number in numbers]


def main():
    numbers = [4, 7, 2, 7, 9, 4, 1, 9, 5, 2]
    scalar = 3

    print("Question # 01: List Operations Using Functions")
    print("-" * 55)
    print("Original list             :", numbers)

    unique_numbers = remove_duplicates(numbers)
    print("After removing duplicates :", unique_numbers)

    average = find_average(numbers)
    print(f"Average of all elements   : {average:.2f}")

    scaled_numbers = multiply_by_scalar(numbers, scalar)
    print(f"List multiplied by {scalar}      :", scaled_numbers)


if __name__ == "__main__":
    main()