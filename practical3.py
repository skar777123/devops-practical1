def sum_two_numbers(a: str, b: str) -> float:
    """Return the sum of two numeric values provided as strings."""
    try:
        return float(a) + float(b)
    except ValueError:
        raise ValueError('Please enter valid numbers.')


def main() -> None:
    first = input('Enter the first number: ').strip()
    second = input('Enter the second number: ').strip()
    try:
        total = sum_two_numbers(first, second)
        print(f'Sum of the two numbers = {total}')
    except ValueError as error:
        print(f'Invalid input: {error}')


if __name__ == '__main__':
    main()
