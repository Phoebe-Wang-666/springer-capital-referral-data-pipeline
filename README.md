# springer-capital-referral-data-pipeline

A Python-based data pipeline for profiling, preprocessing, and validating referral data, built as part of the Springer Capital internship program.

This project focuses on understanding referral data quality, joining multiple source tables, and applying basic business rules to determine valid referrals and reward eligibility.

---

## Data Profiling

Before any data cleaning or joins, we first performed basic data profiling on all raw source tables to understand overall data quality.

The profiling step includes:
- row counts per table
- null value counts for each column
- basic column-level inspection

From the profiling results, most tables contain no missing values.  
The remaining null values mainly appear in reward- and transaction-related fields (e.g. reward ID, transaction ID), which is expected given the referral flow — not every referral leads to a completed transaction or reward.

This profiling step helps confirm that the data structure is consistent and that missing values are meaningful rather than data quality issues.

---

## Data Preprocessing

After profiling, the raw tables are joined using `user_referrals` as the base table.

During preprocessing:
- referral status descriptions are mapped from status IDs
- transaction and reward information is joined where available
- referrer and referee user information is enriched from user logs
- timestamps are standardized for downstream use

The output of this step is a single cleaned dataset saved as:

output/preprocessed_referrals.csv


---

## Business Logic Validation

In the final step, simple business rules are applied to determine:
- whether a referral is valid
- whether a referral is eligible for a reward

The current rules include:
- a referral must have an associated transaction
- the transaction must be marked as paid
- the referrer account must not be deleted
- reward eligibility depends on both referral validity and reward availability

The final output is saved as:

output/final_referral_results.csv

## Project Structure
springer-capital-referral-data-pipeline/
├── data/ # raw input CSV files
├── output/ # profiling, preprocessing, and final outputs
├── profiling.py
├── preprocess.py
├── business_logic.py
├── README.md
└── src/ # reserved for future extensions

---

## Notes

This project is designed as a simple, end-to-end data pipeline to demonstrate data profiling, table joins, and rule-based validation in a real referral business context.
