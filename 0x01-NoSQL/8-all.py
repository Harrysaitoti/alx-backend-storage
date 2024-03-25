#!/usr/bin/env python3
"""
List all documents in a collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of all documents in the collection.
        Returns an empty list if no documents are found.
    """
    documents = []
    cursor = mongo_collection.find({})
    for document in cursor:
        documents.append(document)
    return documents

# For testing purposes
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specified collection
    school_collection = client.my_db.school
    
    # Call the list_all function
    schools = list_all(school_collection)

    # Print document details
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
