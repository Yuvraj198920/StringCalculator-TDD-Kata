from string_calculator import StringCalculator


def test_string_calculator():
    calculator = StringCalculator()

    # Test empty string
    assert calculator.add('') == 0

    # Test single number
    assert calculator.add('1') == 1

    # Test two numbers
    assert calculator.add('1,5') == 6

    # Test multiple numbers
    assert calculator.add('1,2,3') == 6

    # Test handling new lines as delimiters
    assert calculator.add('1\n2,3') == 6

    # Test custom delimiter
    assert calculator.add('//;\n1;2') == 3

    # Test multiple custom delimiters
    assert calculator.add('//|\n1|2|3') == 6

    # Test negative number exception
    try:
        calculator.add('1,-2,3')
    except ValueError as e:
        assert str(e) == "Negative numbers not allowed: -2"

    # Test multiple negative numbers exception
    try:
        calculator.add('1,-2,-3')
    except ValueError as e:
        assert str(e) == "Negative numbers not allowed: -2, -3"


test_string_calculator()

if __name__ == "__main__":
    test_string_calculator()
    print("All tests passed.")
