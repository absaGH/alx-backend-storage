#!/usr/bin/env python3
""" PyMongo sorting """


def top_students(mongo_collection):
    """ function that returns all students sorted by average score"""
    return list(mongo_collection.find())
