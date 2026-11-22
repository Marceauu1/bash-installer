from abc import ABC, abstractmethod
import time


class BaseETLPipeline(ABC):
    def __init__(self, source: str) -> None:
        self.source = source
        self.data = None

    def run(self) -> str:
        # Template method defining fixed workflow order
        self.connect()
        self.extract()
        self.transform()
        self.validate()
        self.load()
        self.cleanup()
        return f"{self.__class__.__name__} finished"

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def extract(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def transform(self) -> None:
        raise NotImplementedError

    def validate(self) -> None:
        # Common validation hook/step (can be overridden if needed)
        if not self.data:
            raise ValueError("No data to validate")

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    def cleanup(self) -> None:
        print("Cleaning up resources...")
        self.data = None
        print("Cleanup complete")


class CSVPipeline(BaseETLPipeline):
    def connect(self) -> None:
        raise NotImplementedError

    def extract(self) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError


class APIPipeline(BaseETLPipeline):
    def connect(self) -> None:
        raise NotImplementedError

    def extract(self) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError


class DatabasePipeline(BaseETLPipeline):
    def connect(self) -> None:
        raise NotImplementedError

    def extract(self) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError


class XMLPipeline(BaseETLPipeline):
    def connect(self) -> None:
        raise NotImplementedError

    def extract(self) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for template_etl.py")
