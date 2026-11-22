from abc import ABC, abstractmethod
import json


class LegacyReportGenerator:
    def generate_report(self, data: dict) -> str:
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml


class AnalyticsDashboard:
    def display(self, json_data: str) -> None:
        data = json.loads(json_data)
        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"  {key}: {value}")


class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        raise NotImplementedError


class LegacyReportAdapter(ReportGeneratorInterface):
    def __init__(self, legacy_generator: LegacyReportGenerator) -> None:
        self.legacy_generator = legacy_generator

    def generate(self, data: dict) -> str:
        # TODO: Call legacy_generator.generate_report(data) and return JSON string
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for adapter_report.py")
