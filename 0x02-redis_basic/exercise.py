#!/usr/bin/env python3
"""python module to interact with redis server"""
import redis
import uuid
#import typer
from typing import Union


class Cache:
    """class to store Redis client information"""

    def __init__(self):
        """ iniitalize Redis DB """
        self.___redis = redis.Redis()
        self.___redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ create a random key & stores it with data """
        key: uuid.UUID = uuid.uuid1()
        self.___redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        if (!self.___redis.exists(key)):
            return 0
        if fn:
            data = self.___redis.get(key)
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """convert data to string"""
        return str(data, 'UTF-8')

    def get_int(self, data: bytes) -> int:
        """convert data to init"""
        return int.from_bytes(data, "big")
