from abc import ABC, abstractmethod


class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class BaseOrder(OrderComponent):
    def __init__(self, base_price: float) -> None:
        self.base_price = base_price

    def get_cost(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return f"Base order ({self.base_price}€)"


class OrderDecorator(OrderComponent):
    def __init__(self, wrapped: OrderComponent) -> None:
        self.wrapped = wrapped

    def get_cost(self) -> float:
        return self.wrapped.get_cost()

    def get_description(self) -> str:
        return self.wrapped.get_description()


class ExpressShippingDecorator(OrderDecorator):
    def get_cost(self) -> float:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError


class InsuranceDecorator(OrderDecorator):
    def get_cost(self) -> float:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError


class GiftWrapDecorator(OrderDecorator):
    def get_cost(self) -> float:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError


class DiscountDecorator(OrderDecorator):
    def __init__(self, wrapped: OrderComponent, percent: float) -> None:
        super().__init__(wrapped)
        self.percent = percent

    def get_cost(self) -> float:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError


class PremiumMemberDecorator(OrderDecorator):
    def get_cost(self) -> float:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for decorator_order.py")
