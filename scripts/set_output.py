# scripts/set_output.py

def main():
    # Define multiple output variables
    output_1 = "Hello, GitHub Actions!"
    output_2 = "This is another output."

    # Write outputs to a file in key=value format
    with open('output.txt', 'w') as f:
        f.write(f'output_1={output_1}\n')
        f.write(f'output_2={output_2}\n')

if __name__ == "__main__":
    main()
