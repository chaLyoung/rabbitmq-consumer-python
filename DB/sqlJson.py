# -*- coding: UTF-8 -*-
from DB import dbModule
import os
import re

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql.sql"), "rt", encoding="utf-8") as f:
    sqlFile = f.read()
    f.close()
    sqlCommands = sqlFile.split(';')


def repl(m):
    inner_word = list(m.group(2))
    print("m", inner_word)
    return m


def clean_str(text):
    pattern = '[^\w\s]'  # 특수기호제거
    text = re.sub(pattern=pattern, repl='\\\\\g<0>', string=text)
    text = re.sub(r'\\%', r'%%', text)

    return text


class SqlJson:
    def __init__(self):
        self.tSelect_test = sqlCommands[0]
        self.tInsert_test = sqlCommands[1]

    # 0.
    def select_test(self, pf_id):
        db = dbModule.Database()
        query = self.tSelect_test.format(pf_id=pf_id)
        result = db.executeAll(query)
        return result

    
    # 2.
    def insert_test(self, ):
        db = dbModule.Database()
        query = self.tInsert_test.format()
        result = db.executeAll(query)
        db.commit()