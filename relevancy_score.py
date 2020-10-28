# import pandas as pd
# import json
# import pickle
# import csv
#
# with open('step_2.csv') as csvfile:
#     input_df = pd.read_csv(csvfile, header=0)
#     print(input_df)
#
# # with open("deal_object", "rb") as f:
# #     Deal = pickle.load(f)
# #     # print(type(Deal))
# #     # print(Deal)
# #     for idx, row in input_df.iterrows():
# #         print(row["List of deals"])
# #         print(type(row["List of deals"]))
#
#
# #Relvancy metric will be a summatiuon of attribute scores based on 1/attribute weight
# # hyperparameters
# us_cities = pd.read_csv("uscities.csv", sep=",", usecols=["city_ascii"], squeeze=True)
#
# Primary_Investor_Type_list = ["Angel (individual)", "Early Stage VC", "Later Stage VC", "Seed Round"]
#
# Keywords_list = []
# m = int(input("Enter number of Keywords"))
# for i in range(0, m):
#     ele = input()
#     Keywords_list.append(ele)
#
# Primary_Industry_Sector_list = []
# o = int(input("Enter number of Primary Industry Sectors (Needs to match pitchbook exactly):"))
# for i in range(0, o):
#     ele = input()
#     Primary_Industry_Sector_list.append(ele)
#
# Investment_Size_min = input("Enter investment size min (millions): ")
# Investment_Size_max= input("Enter investment size max (millions):")
#
# investment_size_weight = int(input("Enter multipler/weight for investment size attribute"))
#
#
# def rank(df):  # Input relevancy df from happynest_comparables.py
#     # Investment Size
#     for idx1, line in input_df.iterrows():
#         print(len(df["List of deals"]))
#         for i in df["List of deals"]:
#             print(i)
#
#             i = json.loads(i)
#             print(type(i))
#             print(len(i))
#             print(i["Deal Size"])
#             if int(i["Deal Size"]) in range(Investment_Size_min, Investment_Size_max):
#                 df["Rank Score"] += investment_size_weight
#
#         # Geography
#         line["Preferred Geography"] = str(line["Preferred Geography"]).split(",")
#         for city in line["Preferred Geography"]:
#             if city in us_cities:
#                 df["Rank Score"] += 1
#
#         # Is Industry?
#         for j in df["List of deals"]:
#             if j[2] in Primary_Industry_Sector_list:
#                 df["Rank Score "] += 1
#
#         # Target Primary Investor Type?
#         if line["Primary Investor Type"] in Primary_Investor_Type_list:
#             df["Rank Score"] += 1
#
#         # Investments
#         investments_score = int(df["Investments in the last 5 years"])
#         # ratio of # total investments vs. investments in comprable sector
#         # # of investments in the lst 5 years/ total investments in the last 5 years
#         total_investment_score = int(df["Investments"])
#         df["Rank Score"] += investments_score
#         df["Rank Score"] += total_investment_score
#         return df
#
#
# relevance_df = rank(input_df)
# relevance_df = relevance_df.sort_values("Rank Score")
#
#
# relevance_df.to_excel("Ranked_LinkedIn_Output.xlsx")
