import sys

def generate_graph(choice):
    print(f"📊 Generating graph for choice {choice}...")
    # Placeholder for visualization logic

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 graph.py <choice>")
        sys.exit(1)

    choice = int(sys.argv[1])
    generate_graph(choice)
