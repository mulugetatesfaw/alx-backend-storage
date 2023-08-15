#!/usr/bin/env python3
"""write pymongo list """

import pymongo


def list_all(mongo_collection):
    """ List all elements in a collection here"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
