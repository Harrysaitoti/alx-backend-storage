#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def get_log_count(collection):
    """Get the number of documents in the collection"""
    return collection.count_documents({})

def get_method_counts(collection):
    """Get counts of different methods in logs"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        count = collection.count_documents({"method": method})
        method_counts[method] = count
    return method_counts

def get_status_check_count(collection):
    """Get count of logs with method=GET and path=/status"""
    count = collection.count_documents({"method": "GET", "path": "/status"})
    return count

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    # Get total logs count
    total_logs = get_log_count(collection)
    print(f"{total_logs} logs")

    # Get method counts
    method_counts = get_method_counts(collection)
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    # Get count of logs with method=GET and path=/status
    status_check_count = get_status_check_count(collection)
    print(f"{status_check_count} status check")
