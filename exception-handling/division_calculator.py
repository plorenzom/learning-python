"""Python exception handling example."""

from non_positive_error import NonPositiveError
import sys

print("Division calculator")

while True:
    try:
        dividend = int(input("Please enter the first positive integer (dividend): "))

        if (dividend < 0):
            raise NonPositiveError("The value must be greater or equal to zero")
        
        divisor = int(input("Please enter the second positive integer (divisor): "))

        if (divisor < 0):
            raise NonPositiveError("The value must be greater or equal to zero")
        
        floatingPointQuotient = dividend / divisor
        integerQuotient = dividend // divisor
    except ValueError:
        print("Oops! The value is not a valid integer")
    except NonPositiveError as nonPositiveError:
        print("Oops!", nonPositiveError)
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed")
    except:
        print("Oops! Unexpected error", sys.exc_info()[0])
    else:
        print(f"Floating point division: {dividend} / {divisor} = {floatingPointQuotient}")
        print(f"Integer division: {dividend} // {divisor} = {integerQuotient}")
    finally:
        answer = None
        
        while (answer not in ["n", "y"]):
            answer = input("Do you want to try it again? (n/y): ").lower()
        
        if (answer == "n"):
            break