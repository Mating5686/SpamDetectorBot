import time
import pandas as pd
import json
import os
from spam_filter.detector import SpamDetector

with open("config.json") as f:
    config = json.load(f)

os.makedirs(os.path.dirname(config["log_file"]), exist_ok=True)
detector = SpamDetector(config)

def load_bids(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"{csv_file} not found.")
        return []

def save_log(log_file, results):
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

def main():
    print("Starting Spam Detector Bot...")
    while True:
        bids = load_bids(config["input_file"])
        results = []
        for bid in bids:
            res = detector.analyze_bid(bid)
            results.append(res)
        save_log(config["log_file"], results)
        print(f"Scanned {len(bids)} bids | Log updated.")
        time.sleep(config["poll_interval_seconds"])

if __name__ == "__main__":
    main()
