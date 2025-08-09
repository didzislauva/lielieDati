import pandas as pd
import random
from datetime import datetime, timedelta

def generate_random_dates_csv(record_count, output_file="random_dates.csv"):
    start_date = datetime(1956, 1, 1)
    end_date = datetime(2023, 12, 31)

    def random_date(start, end):
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    data = {
        "id": list(range(1, record_count + 1)),
        "date": [random_date(start_date, end_date).strftime("%Y-%m-%d") for _ in range(record_count)]
    }

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"✅ CSV fails '{output_file}' ar {record_count} ierakstiem izveidots veiksmīgi!")

# ======= Lietošana =======
# Norādi, cik ierakstus vēlies:
generate_random_dates_csv(600)
