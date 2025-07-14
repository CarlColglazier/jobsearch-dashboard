#!/usr/bin/env python3

import pandas as pd
import random
from datetime import datetime
import os

statuses = ["Applied", "Rejected", "Screener", "Interview", "Offered"]

def generate_fake_data(n: int):
    start_date = datetime(2025, 1, 1, 00, 00, 00)
    end_date = datetime(2025, 6, 1, 00, 00, 00)
    return pd.DataFrame({
        "Company": [f"Company {i}" for i in range(1, n+1)],
        "Position": [f"Position {i}" for i in range(1, n+1)],
        "Link": "#",
        "Status": random.choices(statuses, k=n),
        "Date": [(start_date + (end_date - start_date) * random.random()).date() for _ in range(n)]
    })


if __name__ == '__main__':
    df = generate_fake_data(100)
    if not os.path.exists("applications.csv"):
        print("Writing fake data to applications.csv")
        df.to_csv("applications.csv", index=False)
    else:
        print("applications.csv already exists. Doing nothing.")
