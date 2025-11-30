from pathlib import Path
import pandas as pd

# Adjust paths
RAW_CSV = Path("data/raw/sample_data.csv")  # make sure this exists
PROCESSED_CSV = Path("data/processed/processed.csv")

def main():
    print("📥 Reading raw data...")
    df = pd.read_csv(RAW_CSV)

    print("🗓 Converting date column...")
    df['date'] = pd.to_datetime(df['date'])

    print("🔃 Sorting by date...")
    df = df.sort_values('date')

    # Create folder if it doesn't exist
    PROCESSED_CSV.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(PROCESSED_CSV, index=False)
    print(f"✅ Done! Processed file saved to: {PROCESSED_CSV}")

if __name__ == "__main__":
    main()

