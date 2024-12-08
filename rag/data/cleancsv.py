import json

# Input and output file paths
input_file = "output.jsonl"
output_file = "fine_tune.jsonl"

# Process the .jsonl file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        data = json.loads(line)  # Parse the JSON line
        data.pop("Rationale", None)  # Remove the "response" key if it exists
        json.dump(data, outfile)  # Write the modified JSON object
        outfile.write('\n')  # Add a newline after each JSON object

print(f"The column 'response' has been removed. Modified file saved as '{output_file}'.")
