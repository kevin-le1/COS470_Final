import pandas as pd

def convert_csv_to_jsonl(csv_path, jsonl_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)
        
        # Convert the DataFrame to JSONL format
        df.to_json(jsonl_path, orient="records", lines=True)
        
        print(f"Successfully converted CSV to JSONL.\nJSONL saved at: {jsonl_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_path = "./data/blockchain_dataset.csv"
jsonl_path = "./data/output.jsonl"
convert_csv_to_jsonl(csv_path, jsonl_path)

