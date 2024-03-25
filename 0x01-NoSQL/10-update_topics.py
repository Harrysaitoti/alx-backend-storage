#!/usr/bin/env python3
"""
Change all topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name (string): School name to update.
        topics (list of strings): List of topics approached in the school.

    Returns:
        None
    """
    # Update documents with matching name
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)

# For testing purposes
if __name__ == "__main__":
    from pymongo import MongoClient
    from pprint import pprint

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specified collection
    school_collection = client.my_db.school
    
    # Update topics for "Holberton school"
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Print updated documents
    schools = list(school_collection.find())
    pprint(schools)

    # Update topics for "Holberton school" again
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Print updated documents again
    schools = list(school_collection.find())
    pprint(schools)
