import json

# Input and output file paths
input_file = "fine_tune.jsonl"
output_file = "chat_formatted_data.jsonl"

# Open the input file and convert
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        entry = json.loads(line)
        chat_entry = {
            "messages": [
                {"role": "user", "content": entry["prompt"]},
                {"role": "assistant", "content": entry["completion"]}
            ]
        }
        outfile.write(json.dumps(chat_entry) + "\n")

print(f"Converted dataset saved as {output_file}")
