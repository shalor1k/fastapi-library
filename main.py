#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException, Query

import sqlite3

conn = sqlite3.connect('mysqlite.db', check_same_thread=False)
c = conn.cursor()
app = FastAPI()


@app.get("/")
def atention():
    return "Эта страница пуста, но вы можете поискать в /library)"


@app.get("/library")
def read_root():
    first_return = []
    second_return = []
    returned = []
    c = conn.cursor()
    for f_row in c.execute('''SELECT DISTINCT name FROM library'''):
        first_return.append(f'{f_row}')

    for i in range(len(first_return)):
        returned.append(f"{first_return[i][2:-3]}")

    return returned


@app.get("/library/{author}")
def read_author(author: str):
    if c.execute('SELECT * FROM library WHERE name=?', (author,)).fetchone():
        returned = []

        for row in c.execute('SELECT DISTINCT title FROM library WHERE name=?', (author,)):
            returned.append(row[0])

        return returned

    else:
        return HTTPException(status_code=404, detail="Item not found")


@app.get("/library/{author}/{title}")
def get_text(author: str, title: str, skip: int = 0, limit: int = 100):

    if c.execute('SELECT * FROM library WHERE name=? AND title=?', (author, title,)).fetchone():
        returned = []

        for row in c.execute('SELECT DISTINCT strings FROM library WHERE name=? AND title=?', (author, title,)):
            returned.append(row[0].split(f'\n'))

        if skip > limit or skip > len(returned[0]):
            return HTTPException(status_code=400, detail="Boundaries are not correct")

        return returned[0][skip:skip+limit]

    else:
        return HTTPException(status_code=404, detail="Item not found")
