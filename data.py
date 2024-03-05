import pandas as pd

# Reading in Military Exporters Data 2022
exporters = pd.read_csv('assets/MilExporters2022.csv')
exporters.head()



# Reading in Lockheed Contracts Over $10 million in 2022
lockheed = pd.read_csv('assets/Lockheed2022_10mil.csv')
agencies = lockheed['Contracting Agency'].unique()

# Understanding the agencies that awarded over $10,000,000 to Lockheed in 2022
for agency in agencies:
    print(agency)

# Grouping by 'Contracting Agency ID' and summing 'Action Obligation ($)'
agency_obligation = lockheed.groupby('Contracting Agency')['Action Obligation ($)'].sum()

# Finding the agency with the highest total obligation
agency_highest_obligation = agency_obligation.idxmax()
highest_obligation_amount = agency_obligation.max()

print("Agency with the highest total obligation:")
print("Agency ID:", agency_highest_obligation)
print("Total Obligation ($):", highest_obligation_amount)

