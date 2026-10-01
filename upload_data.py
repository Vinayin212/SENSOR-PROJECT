from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://vinaygoswami212_db_user:Qp1bKVfbsOdt7Gf9@cluster0.advenvj.mongodb.net/"
#create a new client and connectt to server

client = MongoClient(uri)

db = client["sensorchip"]
collection = db["waferfault"]


df=pd.read_csv("wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

collection.insert_many(json_record)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)