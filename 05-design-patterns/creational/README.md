# Creational Design Patterns

- **factory_payment.py**: Refactor payment processing using an `ABC` processor interface, concrete processors (`CreditCardProcessor`, `BankTransferProcessor`, `PayPalProcessor`), and `PaymentFactory` with a type-to-class dictionary.
- **builder_employee.py**: Refactor `create_employee` into `Employee` and a fluent `EmployeeBuilder` (plus preset support).
- **singleton_config.py** + **config.json**: Refactor repeated `load_config()` calls into a `ConfigManager` singleton with `get_instance()` and `get(key)` dot-path lookup.
