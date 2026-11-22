from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    department: str
    position: str
    salary: float
    start_date: str
    manager_id: int | None = None
    phone: str | None = None
    address: str | None = None
    emergency_contact: str | None = None
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False
    office_location: str | None = None
    contract_type: str = "permanent"


class EmployeeBuilder:
    def __init__(self) -> None:
        # TODO: Initialize default fields/state
        raise NotImplementedError

    def with_name(self, first_name: str, last_name: str) -> "EmployeeBuilder":
        raise NotImplementedError

    def with_email(self, email: str) -> "EmployeeBuilder":
        raise NotImplementedError

    def with_job(self, department: str, position: str, salary: float, start_date: str = "2026-01-01") -> "EmployeeBuilder":
        raise NotImplementedError

    def with_equipment(self, laptop: bool = False, parking: bool = False) -> "EmployeeBuilder":
        raise NotImplementedError

    def with_access(self, vpn: bool = False, admin: bool = False) -> "EmployeeBuilder":
        raise NotImplementedError

    def build(self) -> Employee:
        # TODO: Validate required fields and return Employee instance
        raise NotImplementedError


if __name__ == "__main__":
    print("Starter loaded for builder_employee.py")
