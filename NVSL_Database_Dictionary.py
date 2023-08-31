import os
import pandas as pd
import NVSL_Team_Class as NVSL_Team

def create_nvsl_instances_from_csv(folder_path):
    nvsl_instances = {}
    print[folder_path]
    for row in folder_path:
        print(row)
        if r[0] not in nvsl_instances:
            nvsl_instances[r[0]]=NVSL_Team(r[0],r[1],r[2],r[1]+r[2]+r[3],r[7])
    return nvsl_instances

if __name__ == "__main__":
    for i in range(2001,2024,1):
        folder_path = "CSV_Data/team_rankings_{year}.csv".format(year = i)  # Replace with the path to your folder containing the CSV files
        nvsl_instances_dict = create_nvsl_instances_from_csv(folder_path)
        print(nvsl_instances_dict)

    
