import pandas as pd

# File path
file_path = r"C:\Users\sindu\Downloads\run-1743756488551-part-block-0-r-00000-snappy (2).parquet"

try:
    # Load the Parquet file
    df = pd.read_parquet(file_path, engine="pyarrow")

    # Show first 5 rows
    print("✅ Data Preview:")
    print(df.head())

    # Save as CSV
    df.to_csv("processed_output.csv", index=False, encoding="utf-8")

    print("✅ CSV saved successfully with", df.shape[0], "rows and", df.shape[1], "columns!")

except Exception as e:
    print("❌ Error:", e)
