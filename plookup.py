import sys
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar_lines(filename, search_string, threshold=0.90):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        count=0

        for i, line in enumerate(lines, start=1):
            line_stripped = line.strip()
            similarity = similar(search_string, line_stripped)
            if similarity >= threshold:
                print(f"{i}: {line_stripped}")
                count=count+1

        print(f"{count} passwords found to match by at least {threshold*100}%")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <search_string>")
    else:
        filename = sys.argv[1]
        search_string = sys.argv[2]
        find_similar_lines(filename, search_string)
