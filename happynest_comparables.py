import pandas as pd
import numpy as np
import pickle
import json
import csv
import openpyxl


class Deal:
    """For each deal that investor is apart of, cross-referenceing from deals output"""

    def __init__(self, Company_Name, Description, Primary_Industry_Sector, Keywords, Deal_Date, Deal_Type, HQ_Location,
                 Company_Website, deal_size):
        self.Company_Name = Company_Name
        self.Description = Description
        self.Primary_Industry_Sector = Primary_Industry_Sector
        self.Keywords = Keywords
        self.Deal_Date = Deal_Date
        self.Deal_Type = Deal_Type
        self.HQ_Location = HQ_Location
        self.Company_Website = Company_Website
        self.deal_size = deal_size


with open("deal_object", "wb") as f:
    pickle.dump(Deal, f)

with open('step_1.csv') as csvfile:
    input_df = pd.read_csv(csvfile, header=0)
    print(input_df)

input_investors = input("Enter filename (including extension) of investors downloadable: ") #"Happynest_Comparables_Investors.xlsx"
investors = pd.read_excel(input_investors)

input_deals = input("Enter filename (including extension) of investors downloadable: ") #"Happynest_Deals.xlsx"
deals = pd.read_excel(input_deals)
deals["Deal Size"] = deals["Deal Size"].fillna(0)

# deals = deals.fillna(0, inplace=True)


relevance_df = pd.DataFrame()
relevance_df["Investor Name"] = investors["Investor Name"]
relevance_df["Description"] = investors["Description"]
relevance_df["Primary Investor Type"] = investors["Primary Investor Type"]
relevance_df["Primary Contact"] = investors["Primary Contact"]
relevance_df["Primary Contact Title"] = investors["Primary Contact Title"]
relevance_df["Investments"] = investors["Investments"]
relevance_df["Investments"].fillna(0.0)
relevance_df["Investments"].replace("", 0.0)
relevance_df["Investments in the last 5 years"] = investors["Investments in the last 5 years"]
relevance_df["Investments in the last 5 years"].fillna(0.0)
relevance_df["Investments in the last 5 years"].replace("", 0.0)
relevance_df["Preferred Geography"] = investors["Preferred Geography"]
relevance_df["Investments in the last 5 years"].fillna(0.0)
relevance_df["List of deals"] = np.empty((len(relevance_df), 0)).tolist()
relevance_df = relevance_df.fillna("")
relevance_df["Rank Score"] = relevance_df.loc[:, 'Rank Score'] = 0

print(relevance_df)

# create list of deals that investor is involved in
for idx1, investor in relevance_df.iterrows():
    # return deals that investor appears in
    investor_name = investor["Investor Name"]
    for idx2, row in deals.iterrows():
        if type(row["Investors"]) == float:
            row["Investors"] = ""
        if type(row["Lead/Sole Investors"]) == float:
            row["Lead/Sole Investors"] = ""
        # if row["Investors"].isnull() == True:
        #     pass
        # if row["Lead/Sole Investors"].isnull() == True:
        #     pass
        if (investor_name in row["Investors"]) or (investor_name in row["Lead/Sole Investors"]):
            deal = Deal(row["Company Name"], row["Description"], row["Primary Industry Sector"], row["Keywords"]
                        , row["Deal Date"], row["Deal Type"], row["HQ Location"], row["Company Website"],
                        int(row["Deal Size"]))
            investor["List of deals"].append(deal)

relevance_df = relevance_df.merge(input_df, how="left", left_on=relevance_df["Primary Contact"],
                                  right_on=input_df["Name"])

# Relvancy metric will be a summatiuon of attribute scores based on 1/attribute weight
# hyperparameters
us_cities = pd.read_csv("uscities.csv", sep=",", usecols=["city_ascii"], squeeze=True)

Primary_Investor_Type_list = ["Angel (individual)", "Early Stage VC", "Later Stage VC", "Seed Round"]

Keywords_list = []
m = int(input("Enter number of Keywords"))
for i in range(0, m):
    ele = input()
    Keywords_list.append(ele)

Primary_Industry_Sector_list = []
o = int(input("Enter number of Primary Industry Sectors (Needs to match pitchbook exactly):"))
for i in range(0, o):
    ele = input()
    Primary_Industry_Sector_list.append(ele)

Investment_Size_min = float(input("Enter investment size min (millions): "))
Investment_Size_max = float(input("Enter investment size max (millions):"))

investment_size_weight = int(input("Enter multipler/weight for investment size attribute"))


def rank(input_row):  # Input relevancy df from happynest_comparables.py
    # Investment Size
    rank_score_counter = 0
    list_of_deals = input_row["List of deals"]
    if len(list_of_deals) != 0:
        for i in range(len(list_of_deals)):
            current_deal = list_of_deals[i]
            if Investment_Size_min <= float(current_deal.deal_size) <= Investment_Size_max:
                rank_score_counter += investment_size_weight
    # Geography, divides number of cities by total
    if input_row["Preferred Geography"] is not None or "":
        input_row["Preferred Geography"] = str(input_row["Preferred Geography"]).split(", ")
        counter = 0
        for city in input_row["Preferred Geography"]:
            if city.lower() in us_cities:
                counter += 1
        final_geo = counter / len(input_row["Preferred Geography"])
        rank_score_counter += final_geo

    # Is Industry?
    if len(list_of_deals) is not None:
        for j in range(len(list_of_deals)):
            current_object = list_of_deals[j]
            if current_object.Primary_Industry_Sector in Primary_Industry_Sector_list:
                rank_score_counter += 1
    # Target Primary Investor Type?
    if input_row["Primary Investor Type"] in Primary_Investor_Type_list:
        rank_score_counter += 1

    # Investments
    if input_row["Investments in the last 5 years"] is not None:
        if input_row["Investments in the last 5 years"] != "":
            rank_score_counter += int(input_row["Investments in the last 5 years"])
    # ratio of # total investments vs. investments in comprable sector
    # # of investments in the lst 5 years/ total investments in the last 5 years
    if input_row["Investments"] is not None:
        if input_row["Investments"] != "":
            rank_score_counter += int(input_row["Investments"])
    print(rank_score_counter)
    input_row["Rank Score"] = rank_score_counter
    return input_row

def summarize_deal(row):
    list_of_deals = row["List of deals"]
    if list_of_deals is not []:
        deals_list = []
        for i in list_of_deals:
            deal_to_dict = {"Company Name" : i.Company_Name, "Description" : i.Description, "Primary Industry Sector" : i.Primary_Industry_Sector, "Keywords" : i.Keywords, "Deal_date" : i.Deal_Date,
                "Deal Type" : i.Deal_Type, "HQ Location" : i.HQ_Location,"Company Website" : i.Company_Website, "Deal Size":i.deal_size}
            deals_list.append(deal_to_dict)
    row["List of deals"] = deals_list
    row["# of deals"] = len(deals_list)
    return row

relevance_df = relevance_df.apply(lambda row: rank(row), axis=1)
relevance_df = relevance_df.apply(lambda row: summarize_deal(row), axis=1)

#Cleaning up
relevance_df = relevance_df.drop(labels="key_0", axis=1)
relevance_df = relevance_df.drop(labels="Name", axis=1)
relevance_df = relevance_df.drop(labels="Unnamed: 0", axis=1)

cols = ["Investor Name","Description", "Primary Investor Type", "Primary Contact", "Primary Contact Title","Investments",
       "Investments in the last 5 years", "Preferred Geography","# of deals", "List of deals","Rank Score", "Profile"]

relevance_df = relevance_df[cols]

final_sorted = relevance_df.sort_values("Rank Score", ascending=False)
final_sorted.to_excel("Ranked_LinkedIn_Output.xlsx")

