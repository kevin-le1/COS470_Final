BASE_PROMPT = '''
Note, if the user gives code, and asks to resolve the code,
give correct code.

Analyze the following query in the context of the 
provided blockchain network implementation. Provide 
a clear explanation of how the context relates to the query. 
Focus on key concepts such as peer-to-peer communication, 
blockchain structures (e.g., Merkle trees, blocks, transactions),
and their interactions. Conclude the explanation with a summary 
of the main points.
'''