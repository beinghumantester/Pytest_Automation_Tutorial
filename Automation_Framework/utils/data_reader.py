
import csv

def get_login_data():
    data=[]

    with open("test_data/login_data.csv") as file:
        reader = csv.DictReader(file) 
        for row in reader:
            data.append(
                (row["username"],row["password"])
                )

    return data

