import pandas as pd
import urllib.request
import json
import datetime
import matplotlib.pyplot as plt


county_url = "http://data.ssb.no/api/v0/dataset/95274.csv?lang=no"
county_csv = pd.read_csv(county_url, encoding="ISO-8859-1", delimiter=";")
print(county_csv.head())

whole_country_url = "http://data.ssb.no/api/v0/dataset/95276.csv?lang=no"
whole_country_csv = pd.read_csv(whole_country_url, encoding="ISO-8859-1", delimiter=";")
print(whole_country_csv.head())


# Use first list, rowbind both data
dframe = pd.concat([county_csv, whole_country_csv])

# Rename data frame columns
dframe.columns = ["region", "date", "variable", "value"]

# Make a new proper date variable
dframe["date"] = pd.to_datetime(dframe["date"], format="%YM%m")

# How many levels has the variable?
unique_variables = dframe["variable"].unique()
print(unique_variables)
print(len(unique_variables))

# Rename variables
dframe["variable"] = dframe["variable"].replace("Utleigde rom", "rentedrooms")
dframe["variable"] = dframe["variable"].replace("Pris per rom (kr)", "roomprice")
dframe["variable"] = dframe["variable"].replace("Kapasitetsutnytting av rom (prosent)", "roomcap")
dframe["variable"] = dframe["variable"].replace("Kapasitetsutnytting av senger (prosent)", "bedcap")
dframe["variable"] = dframe["variable"].replace("Losjiomsetning (1 000 kr)", "revenue")
dframe["variable"] = dframe["variable"].replace("Losjiomsetning per tilgjengeleg rom (kr)", "revperroom")
dframe["variable"] = dframe["variable"].replace("Losjiomsetning, hittil i år (1 000 kr)", "revsofar")
dframe["variable"] = dframe["variable"].replace("Losjiomsetning per tilgjengeleg rom, hittil i år (kr)", "revroomsofar")
dframe["variable"] = dframe["variable"].replace("Pris per rom hittil i år (kr)", "roompricesofar")
dframe["variable"] = dframe["variable"].replace("Kapasitetsutnytting av rom hittil i år (prosent)", "roomcapsofar")
dframe["variable"] = dframe["variable"].replace("Kapasitetsutnytting av senger, hittil i år (prosent)", "bedcapsofar")


# How many levels has the variable?
unique_regions = dframe["region"].unique()
print(unique_regions)
print(len(unique_regions))


# Rename regions
dframe["region"] = dframe["region"].replace("30 Viken", "Viken")
dframe["region"] = dframe["region"].replace("03 Oslo", "Oslo")
dframe["region"] = dframe["region"].replace("34 Innlandet", "Innlandet")
dframe["region"] = dframe["region"].replace("38 Vestfold og Telemark", "Vestfold og Telemark")
dframe["region"] = dframe["region"].replace("42 Agder", "Agder")
dframe["region"] = dframe["region"].replace("11 Rogaland", "Rogaland")
dframe["region"] = dframe["region"].replace("46 Vestland", "Vestland")
dframe["region"] = dframe["region"].replace("15 Møre og Romsdal", "Møre og Romsdal")
dframe["region"] = dframe["region"].replace("50 Trøndelag - Trööndelage", "Trøndelag")
dframe["region"] = dframe["region"].replace("18 Nordland", "Nordland")
dframe["region"] = dframe["region"].replace("54 Troms og Finnmark - Romsa ja Finnmárku", "Troms og Finnmark")
dframe["region"] = dframe["region"].replace("21 Svalbard", "Svalbard")
dframe["region"] = dframe["region"].replace("0N Heile landet", "Whole country")


# Get all the unique region values from region column
unique_regions = dframe["region"].unique()

# Plot the room cap for each region
for region_name in unique_regions:
    # Get rows in data frame only for the given region and room cap
    region = dframe.loc[(dframe["region"] == region_name) & (dframe["variable"] == "roomcap")]

    # Plot the date and value
    plt.plot(region["date"], region["value"], label=region_name)


# Save the dataframe to csv
dframe.to_csv("dataframe.csv", index=False)


# Display labels
plt.legend()

plt.ylabel('Room cap')
plt.xlabel('Time')
plt.show()