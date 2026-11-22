# Structural Design Patterns

- **adapter_report.py**: Adapt `LegacyReportGenerator` (XML) to `ReportGeneratorInterface` (`generate(data) -> str` returning JSON) for `AnalyticsDashboard`.
- **decorator_order.py**: Refactor boolean-flag pricing into `OrderComponent`, `BaseOrder`, and decorators (`ExpressShippingDecorator`, `InsuranceDecorator`, `GiftWrapDecorator`, `DiscountDecorator`, `PremiumMemberDecorator`).
