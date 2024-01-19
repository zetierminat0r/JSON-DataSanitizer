import ast
import random
import string
import re
import sys

# Function to replace non-binary values with random data
def replace_values(data):
    if isinstance(data, dict):
        return {key: replace_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [replace_values(item) for item in data]
    elif isinstance(data, (str, int, float)):
        if isinstance(data, str) and data.lower() in ('true', 'false', 'null'):
            return data
        elif isinstance(data, str):
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(data)))
        else:
            return random.randint(0, 100)
    else:
        return data

if __name__ == "__main__":
    try:
        # Read input data from stdin
        input_data = sys.stdin.read()
        
        # Parse the input as data using ast.literal_eval
        parsed_data = ast.literal_eval(input_data)
        
        # Sanitize the data
        sanitized_data = replace_values(parsed_data)
        
        # Convert sanitized data to string for replacement
        sanitized_string = str(sanitized_data)

        # Replace the quotes around the keys
        keys = re.findall(r"'(.*?)':", sanitized_string)
        for key in keys:
            sanitized_string = re.sub(fr"'{key}':", f'"{key}":', sanitized_string)

        print(sanitized_string)

    except Exception as e:
        print(f"Error: {str(e)}")

