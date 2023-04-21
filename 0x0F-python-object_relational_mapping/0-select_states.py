#!/usr/bin/env python3
"""
file: 0-select_states.py
"""

from sys import argv
from typing import List, Tuple
import MySQLdb


def select_states(argv: List[str]) -> List[Tuple[int, str]]:
    """Connects to the MySQL database and selects all states from states table.

    Args:
        argv: A list of command-line arguments.

    Returns:
        A list of tuples containing the id and name of each state in the database.
    """
    if len(argv) < 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        exit(1)

    sql_query = "SELECT * FROM states ORDER BY id ASC"

    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            ) as db:
        with db.cursor() as cur:
            cur.execute(sql_query)
            states_info = cur.fetchall()

    return states_info


if __name__ == "__main__":
    states = select_states(argv)
    for state in states:
        print(f"{state[0]}: {state[1]}")

