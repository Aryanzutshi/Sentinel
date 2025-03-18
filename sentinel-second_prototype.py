import argparse
import subprocess
import json
import os

def scan_contract(file_path):
    print(f"🔍 Scanning file: {file_path} using ScrawID database")

    try:
        # Run ScrawID parsing pipeline
        subprocess.run(["bash", "scripts/call_main.sh", "4", "all"], check=True)
        subprocess.run(["python3", "scripts/get_final_json.py", "--src", "data/scrawld_res_all.txt", "--dst", "data/vulnerabilities.json"], check=True)
        subprocess.run(["python3", "scripts/parse_final_json.py", "--src", "data/vulnerabilities.json", "--dst", "data/majority_result.json"], check=True)

        # Read parsed vulnerability report
        with open("data/majority_result.json", "r") as file:
            vulnerabilities = json.load(file)

        print("✅ Scan Results:")
        print(json.dumps(vulnerabilities, indent=4))

    except Exception as e:
        print(f"❌ Error running ScrawID analysis: {e}")

def visualize_results(choice):
    print(f"📊 Generating graph for choice {choice}")
    subprocess.run(["python3", "scripts/graph.py", str(choice)], check=True)

def main():
    parser = argparse.ArgumentParser(description="Sentinel: Smart Contract Security Analyzer")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scans a Solidity contract for vulnerabilities")
    scan_parser.add_argument("file", help="Solidity contract file to analyze")

    visualize_parser = subparsers.add_parser("visualize", help="Generate vulnerability graphs")
    visualize_parser.add_argument("choice", type=int, help="1: Total Contracts per Vulnerability, 2: Total Warnings, 3: Unique Vulnerabilities")

    args = parser.parse_args()

    if args.command == "scan":
        scan_contract(args.file)
    elif args.command == "visualize":
        visualize_results(args.choice)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
