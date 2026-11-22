from abc import ABC, abstractmethod
import json


class ReportFormatStrategy(ABC):
    @abstractmethod
    def format(self, data: list[dict]) -> str:
        raise NotImplementedError

    @abstractmethod
    def extension(self) -> str:
        raise NotImplementedError


class PDFFormatStrategy(ReportFormatStrategy):
    def format(self, data: list[dict]) -> str:
        raise NotImplementedError

    def extension(self) -> str:
        return ".pdf"


class ExcelFormatStrategy(ReportFormatStrategy):
    def format(self, data: list[dict]) -> str:
        raise NotImplementedError

    def extension(self) -> str:
        return ".xlsx"


class CSVFormatStrategy(ReportFormatStrategy):
    def format(self, data: list[dict]) -> str:
        raise NotImplementedError

    def extension(self) -> str:
        return ".csv"


class JSONFormatStrategy(ReportFormatStrategy):
    def format(self, data: list[dict]) -> str:
        return json.dumps(data, indent=2)

    def extension(self) -> str:
        return ".json"


class HTMLFormatStrategy(ReportFormatStrategy):
    def format(self, data: list[dict]) -> str:
        raise NotImplementedError

    def extension(self) -> str:
        return ".html"


class ReportGenerator:
    def __init__(self, data: list[dict], strategy: ReportFormatStrategy | None = None) -> None:
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy: ReportFormatStrategy) -> None:
        self.strategy = strategy

    def generate_report(self) -> str:
        # TODO: Delegate to self.strategy.format(self.data)
        raise NotImplementedError

    def save_report(self, filename: str) -> None:
        # TODO: Write generated report to filename + self.strategy.extension()
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for strategy_report.py")
