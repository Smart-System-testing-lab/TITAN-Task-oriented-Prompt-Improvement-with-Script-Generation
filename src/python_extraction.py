import re

def extract_first_function(text):
    # Regular expression pattern to match a basic Python function definition
    # This pattern is simplified and may not work for all valid Python functions
    pattern = r"def\s+[a-zA-Z_][a-zA-Z_0-9]*\s*\((?:[^()]*|\([^()]*\))*\)\s*(?:->\s*[^:]+)?\s*:"
    
    # Find all matches of Python function definitions in the text
    matches = re.finditer(pattern, text, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        # Extract the start and end indices of the first match
        start, end = match.span()
        # Attempt to extract the whole function by counting indentation levels
        # This is a naive approach and might not work correctly for all cases
        indent_level = len(text[start:end]) - len(text[start:end].lstrip())
        function_lines = []
        for line in text[end:].split('\n'):
            current_indent = len(line) - len(line.lstrip())
            # Break if the current line is less indented than the function definition line
            if line.strip() == "" or current_indent < indent_level:
                break
            function_lines.append(line)
        
        # Combine the matched function definition with its body
        full_function = text[start:end] + "\n" + "\n".join(function_lines)
        return full_function
    return None

# Example usage
text = """
import os

def example_function(param1, param2):
    # Function body
    print(param1, param2)
    
    def nested_function():
        pass

# Another function
def another_function():
    pass
"""

extracted_function = extract_first_function(text)
print(extracted_function)
