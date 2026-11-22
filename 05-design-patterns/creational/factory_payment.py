from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def validate(self, details: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        raise NotImplementedError


class CreditCardProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        # TODO: Validate card_number (16 chars) and cvv (3 chars)
        raise NotImplementedError

    def process(self, amount: float, details: dict) -> dict:
        # TODO: Validate, calculate 2.9% fee, and return result dict
        raise NotImplementedError


class BankTransferProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        # TODO: Validate iban (length >= 15)
        raise NotImplementedError

    def process(self, amount: float, details: dict) -> dict:
        # TODO: Validate, calculate 1.50 flat fee, and return result dict
        raise NotImplementedError


class PayPalProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        # TODO: Validate email contains "@"
        raise NotImplementedError

    def process(self, amount: float, details: dict) -> dict:
        # TODO: Validate, calculate 3.4% + 0.30 fee, and return result dict
        raise NotImplementedError


class PaymentFactory:
    _processors: dict[str, type[PaymentProcessor]] = {
        # TODO: Map "credit_card", "bank_transfer", "paypal" to processor classes
    }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        # TODO: Return processor instance or raise ValueError for unknown type
        raise NotImplementedError


if __name__ == "__main__":
    factory = PaymentFactory()
    print("Starter loaded for factory_payment.py")
