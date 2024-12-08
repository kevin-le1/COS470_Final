import json
from explainable_rag import ExplainableRetriever

def load_texts_from_files(file_paths):
    texts = []
    for file_path in file_paths:
        print(f"Loading texts from {file_path}")
        with open(file_path, 'r') as file:
            if file_path.endswith(".jsonl"):
                for line in file:
                    try:
                        texts.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        pass
            elif file_path.endswith(".json"):
                try:
                    data = json.load(file)
                    if isinstance(data, list):
                        texts.extend([item for item in data])
                    else:
                        texts.extend(data.values())
                except json.JSONDecodeError:
                    pass
    return texts
