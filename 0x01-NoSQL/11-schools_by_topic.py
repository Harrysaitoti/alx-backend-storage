#!/usr/bin/env python3
"""
Retrieve schools based on a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools based on a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (string): Topic to search for.

    Returns:
        A list of schools that match the specified topic.
    """
    schools = []
    cursor = mongo_collection.find({"topics": topic})
    for school in cursor:
        schools.append(school)
    return schools

# For testing purposes
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specified collection
    school_collection = client.my_db.school
    
    # Retrieve schools with the topic "Python"
    schools = schools_by_topic(school_collection, "Python")

    # Print details of retrieved schools
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
