def is_numeric_palindrome(value: str) -> bool:
    """Return True if the given value is a numeric palindrome."""
    if not value.isdigit():
        raise ValueError('Input must contain only digits.')
    return value == value[::-1]


def main() -> None:
    user_input = input('Enter a numeric value to check for palindrome: ').strip()
    try:
        if is_numeric_palindrome(user_input):
            print('Yes, it is a numeric palindrome.')
        else:
            print('No, it is not a numeric palindrome.')
    except ValueError as error:
        print(f'Invalid input: {error}')


if __name__ == '__main__':
    main()
