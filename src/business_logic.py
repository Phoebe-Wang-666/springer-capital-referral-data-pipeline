import pandas as pd

# load preprocessed data
df = pd.read_csv("output/preprocessed_referrals.csv")


# default flags
df["is_valid_referral"] = True
df["invalid_reason"] = ""
df["is_reward_eligible"] = False


# rule 1: referral must have a transaction
mask_no_transaction = df["transaction_id"].isna()
df.loc[mask_no_transaction, "is_valid_referral"] = False
df.loc[mask_no_transaction, "invalid_reason"] = "no_transaction"


# rule 2: transaction must be paid
mask_not_paid = df["transaction_status"] != "PAID"
df.loc[mask_not_paid & df["is_valid_referral"], "is_valid_referral"] = False
df.loc[mask_not_paid & df["is_valid_referral"], "invalid_reason"] = "transaction_not_paid"


# rule 3: referrer must not be deleted
mask_referrer_deleted = df["referrer_is_deleted"] == True
df.loc[mask_referrer_deleted & df["is_valid_referral"], "is_valid_referral"] = False
df.loc[mask_referrer_deleted & df["is_valid_referral"], "invalid_reason"] = "referrer_deleted"


# reward eligibility
mask_reward_eligible = (
    df["is_valid_referral"]
    & df["reward_value"].notna()
)

df.loc[mask_reward_eligible, "is_reward_eligible"] = True


# save final result
df.to_csv("final_referral_results.csv", index=False)

print("Business logic processing completed.")
print(df["is_valid_referral"].value_counts())
print(df["is_reward_eligible"].value_counts())
