import json
import sys
import os

# Define the absolute path for vulnerabilities.json
BASE_DIR = "/home/accidentalgenius/DEV/Hackathon Work/Sentinel/ScrawlD"
DATA_DIR = os.path.join(BASE_DIR, "data")
DEFAULT_OUTPUT_PATH = os.path.join(DATA_DIR, "vulnerabilities.json")

def convert_to_json(src, dst=DEFAULT_OUTPUT_PATH):
    print(f"📄 Converting {src} to JSON format at {dst}...")

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    # Placeholder: Read raw text and convert to JSON
    data = {"message": "Parsed data from ScrawID"}
    
    with open(dst, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 get_final_json.py --src <source_file> [--dst <destination_file>]")
        sys.exit(1)

    src_file = sys.argv[2]

    # If destination is provided, use it. Otherwise, default to ScrawlD's data directory
    dst_file = sys.argv[4] if len(sys.argv) > 4 else DEFAULT_OUTPUT_PATH

    convert_to_json(src_file, dst_file)
