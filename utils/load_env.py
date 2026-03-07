# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：load_env.py
@Author  ：九成八
@Date    ：2026/3/7 13:15 
"""
from dotenv import load_dotenv
import os

load_dotenv()
def get_env(key):
    return os.getenv(key)
