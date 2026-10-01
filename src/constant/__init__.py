import os

AWS_S3_BUCKET_NAME = "wafer-fault-detection-mlops"
MONGO_DATABASE_NAME = "sensorchip"
MONGO_COLLECTION_NAME = "waferfault"


TARGET_COLUMN = "quality"
MONGO_DB_URL="mongodb+srv://vinaygoswami212_db_user:Qp1bKVfbsOdt7Gf9@cluster0.advenvj.mongodb.net/"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"