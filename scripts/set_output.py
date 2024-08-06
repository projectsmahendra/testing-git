# scripts/set_output.py

def main():
    # Define multiple output variables
    octopus_project_id = "Hello, GitHub Actions, project id!"

    env_file = os.getenv('GITHUB_ENV')
    with open(env_file, "a") as outputfile:
        outputfile.write(f"OCTOPUS_PID={octopus_project_id}")

if __name__ == "__main__":
    main()
