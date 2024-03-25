#!/usr/bin/env python3
"""
Insert a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the specified MongoDB collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the document fields and values.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

# For testing purposes
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specified collection
    school_collection = client.my_db.school
    
    # Call the insert_school function to insert a new document
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
