#!/usr/bin/env python3
"""python module to interact with redis server"""
import redis
import uuid
#import typer
from typing import Union


class Cache:
    """class to store Redis client information"""

    def __init__(self):
        self.___redis = redis.Redis()
        self.___redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: uuid.UUID = uuid.uuid1()
        self.___redis.set(str(key), data)
        return str(key)
