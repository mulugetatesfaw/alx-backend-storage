#!/usr/bin/env python3
"""MongoDB Find functionality"""


def schools_by_topic(mongo_collection, topic):
    """
    Use an aggregate to find documents
    :parameter mongo_collection: Pymongo connection
    :parameter topic: The topic to search
    :returns: The list of school that having the same topics
    """
    return [i for i in mongo_collection.find({"topics": topic})]
