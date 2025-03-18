import json
import sys

def filter_majority_vulnerabilities(src, dst):
    print(f"⚖️ Filtering majority-based vulnerabilities from {src} to {dst}...")
    
    with open(src, "r") as file:
        data = json.load(file)
    
    # Placeholder: Filter vulnerabilities (simulated)
    majority_data = {"majority_vulnerabilities": ["Reentrancy", "Integer Overflow"]}

    with open(dst, "w") as json_file:
        json.dump(majority_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 parse_final_json.py --src <source_file> --dst <destination_file>")
        sys.exit(1)

    src_file = sys.argv[2]
    dst_file = sys.argv[4]
    filter_majority_vulnerabilities(src_file, dst_file)
