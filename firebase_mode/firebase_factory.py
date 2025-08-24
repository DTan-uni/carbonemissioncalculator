import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from uuid import uuid4
from random import randint

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r"firebase_mode/cred.json")

# # Initialize the app with a service account, granting admin privileges

def initialize_db():
    if not firebase_admin._apps:
        firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://ev-carbon-counting-system-default-rtdb.asia-southeast1.firebasedatabase.app/ "
    },
)

    return db


if __name__ == "__main__":
    from faker import Faker
    fake = Faker()

    # # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference("/User_Info")
    for i in range(10):
        ref.child(str(uuid4())).set(  {
                "username": fake.name(),
                "phone_number":f"+60{randint(1111111111,1111111111*9)}",
                "car_model": "tesla_model_x",
                "car_category": "standard_suv",
            })
        

    status = ref.child("910e5b96-061f-4c1b-bbaa-bbd4b5b5e6f5").get()
    print(status)
    # # # # 
    db = initialize_db()
    data = db.reference("/User_Info")
    user_info = data.child("f1751ed2-dbdb-40c9-87e0-8ea6fa4d6eba").get()


    user_name = user_info.get("username")
    print(user_name)
