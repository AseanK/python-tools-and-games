import sys

def remove_duplicate_lines(input_file, output_file):
    unique_lines = []
    seen_lines = set()

    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                line = line.rstrip()
                if line not in seen_lines:
                    unique_lines.append(line)
                    seen_lines.add(line)

        with open(output_file, 'w') as outfile:
            for line in unique_lines:
                outfile.write(line + '\n')

        print(f"The file with duplicates removed has been saved as {output_file}.")

    except FileNotFoundError:
        print(f"The file {input_file} was not found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        remove_duplicate_lines(input_file, output_file)

