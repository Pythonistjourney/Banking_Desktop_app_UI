import os

def read_all_files(directory, encoding="utf-8"):
    """
    Recursively reads all files in the given directory and returns a dictionary
    mapping file paths to their contents.

    Args:
        directory (str): The root directory to start reading files from.
        encoding (str): The encoding to use when reading files.

    Returns:
        dict: {relative_file_path: file_content}
    """
    files_content = {}
    # List of binary file extensions to skip
    binary_extensions = {'.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.bin', '.jpg', '.jpeg', '.png', '.gif', '.ico'}
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file_path)
            
            # Skip binary files
            if ext.lower() in binary_extensions:
                continue
                
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    rel_path = os.path.relpath(file_path, directory)
                    files_content[rel_path] = f.read()
            except UnicodeDecodeError:
                # Skip files that can't be decoded as text
                continue
            except Exception as e:
                print(f"Could not read {file_path}: {e}")
    
    return files_content

# Example usage:
# all_files = read_all_files("src")
# for path, content in all_files.items():
#     print(f"--- {path} ---\n{content}\n")