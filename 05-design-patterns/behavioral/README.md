# Behavioral Design Patterns

- **strategy_report.py**: Refactor multi-format report generation (`pdf`, `excel`, `csv`, `json`, plus `html`) using a strategy interface, concrete strategies, `set_strategy()`, and `save_report()`.
- **template_etl.py**: Refactor duplicate ETL pipelines (`CSVPipeline`, `APIPipeline`, `DatabasePipeline`, plus `XMLPipeline`) using a base class template method `run()` and hook methods.
