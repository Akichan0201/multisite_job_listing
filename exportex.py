import pandas as pd


def export_data(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

    print(f"Data exported to {filename}")