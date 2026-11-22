# UML Modeling Solutions

## Exo 1: Hospital Management System

### Task 1 & 2: Class Diagram (6 Core Classes + Payment Types)
- **Classes:** `Patient`, `Doctor`, `Organizer`, `HealthProblem`, `Prescription`, `Payment`
- **Payment types:** `Check`, `Cash`, `CreditCard` (inheritance or enum)
- **Relationships & Multiplicities:** Sketch associations, composition/aggregation, and multiplicities (`1`, `0..1`, `1..*`, `*`).

### Task 3: Extended Architecture & Sequence Diagrams
- **Superclass:** `User` (`id`, `name`, `password`, `login()`, `logout()`)
- **Polymorphism:** Payment strategy / payment method types
- **State / History:** `HealthProblem` status (`pending`, `in-review`, `resolved`), timestamps, and references to past prescriptions
- **Sequence Scenarios:**
  1. Patient Registration (Organizer creates new member)
  2. Consultation Flow (problem submission -> review/doctor consultation -> prescription delivery)
  3. Payment Processing (patient pays -> organizer forwards to doctor)

### Questions to Consider
1. **Multiple doctors per patient:** How do you model many-to-many / per-consultation assignments?
2. **Prescription reusability:** Should prescriptions be reusable or tied to a specific consultation/episode?
3. **Payment design pattern:** Which pattern fits best (e.g., Strategy) and why?
4. **Data integrity on payments:** How do you prevent partial updates, double charges, or mismatched payouts?

---

## Exo 2: ABCD Records

### Level 1: Basic Use Case & Class Diagrams
- **Actors:** `Member`, `Order Processing Clerk`
- **Use Cases:** `Place Order`, `Verify Membership`, `Process Order`, `Make Payment`
- **Classes:** `Member`, `Order`, `OrderProcessingClerk`

### Level 2: Complete Use Case & Class Diagrams
- **Additional Actors:** `Collection Department Clerk`, `Non-Member`
- **Additional Use Cases:** `Verify Item Availability`, `Apply Discount`, `Print Invoice`, `Print Shipping List`, `Order Unavailable Items`, `Send Membership Application`
- **Use Case Relations:** `<<include>>` vs `<<extend>>` and system boundary
- **Classes & Inheritance:** `Item` (`CD`, `Tape`), `Member` (`Royal`, `Regular`), `Payment` (`Cash`, `Check`, `BankDraft`), `Order`, `OrderLine`, `Invoice`, `ShippingList`, `MembershipApplication`
- **Key Scenario:** Royal member orders 2 CDs (one unavailable), pays by check.

### Level 3: Sequence Diagrams
1. Complete Order Processing Flow
2. Membership Verification (success and failure)
3. Payment Processing (all payment types)
4. Item Reordering for Royal Members
