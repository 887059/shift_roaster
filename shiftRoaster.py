import pandas as pd

# Create the shift roster DataFrame
shift_roaster = {
    "shift_members": ["bhuvneswari", "parkavi", "ragavi", "Mounika"],
    "week_off": ["sunday", "monday", "tuesday", "wednesday"]
}

df_roaster = pd.DataFrame(shift_roaster)

# Display original data
print("Original Shift Roaster:")
print(df_roaster)

# Get user input for modification
member_name = input("\nEnter the shift member's name to modify: ").strip()
new_week_off = input("Enter the new week off day: ").strip()

# Convert column to lowercase for case-insensitive matching
df_roaster["shift_members"] = df_roaster["shift_members"].str.lower()

# Check if the member exists in the DataFrame
if member_name.lower() in df_roaster["shift_members"].values:
    df_roaster.loc[df_roaster["shift_members"] == member_name.lower(), "week_off"] = new_week_off
    print("\nUpdated Shift Roaster:")
    print(df_roaster)

    # Save updated data
    df_roaster.to_csv("updated_shift_roaster.csv", index=False)
    print("\nUpdated shift roster saved to 'updated_shift_roaster.csv'")
else:
    print("\n Name Error: Member not found. Please check the name and try again.")