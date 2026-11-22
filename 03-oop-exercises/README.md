# Exercise 3 - OOP Problems (Operator Overloading & Inheritance)

## Part 1: Operator Overloading
- **Problem 1 (Complex):** Implement a complex number class and overload `+` (`__add__`) and `-` (`__sub__`).
- **Problem 2 (Person):** `name`, `age`, `gender`; overload `>` (`__gt__`) to compare by `age`.
- **Problem 4 (Vector):** 3D vector with `x`, `y`, `z`; overload `*` (`__mul__`) to compute the dot product.
- **Problem 5 (Circle):** Compare circles by `radius` across `<`, `>`, `==`, `!=`, `>=`, and `<=`.
- **Problem 6 (Point2D):** 2D point with `x`, `y`; overload comparison operators based on Euclidean distance from `(0, 0)` (`sqrt(x^2 + y^2)`).
- **Problem 7 (Matrix):** Overload `*` (`__mul__`) to multiply two matrices.

## Part 2: Inheritance
- **Problem 1 (Vehicle):** Base class with `drive()` returning `"Driving a vehicle"`; subclasses `Car` and `Bicycle` override `drive()`.
- **Problem 2 (Person / Student / Employee):** `Person` (`name`, `age`, `address`, `introduce()`) with subclasses `Student` (`field_of_study`) and `Employee` (`company`) overriding `introduce()`.
- **Problem 3 (BankAccount / SavingsAccount):** `BankAccount` (`account_number`, `balance`, `deposit()`, `withdraw()`, `transfer()`) and subclass `SavingsAccount` (`interest_rate`, `add_interest()`, `check_balance()`).

## Usage
Run `python3 oop_exercises.py` from inside `03-oop-exercises/`.
