# scripts/set_output.py
import os

def main():
    # Define multiple output variables
    octopus_project_id = "Hello"

    # env_file = os.getenv('GITHUB_ENV')
    # print(env_file,'-----')
    # with open(env_file, "a") as outputfile:
    #     print(f"OCTOPUS_PID={octopus_project_id}")
    #     outputfile.write(f"OCTOPUS_PID={octopus_project_id}")
    with open('octopus_project_id.txt', 'w') as f:
        f.write(octopus_project_id)

if __name__ == "__main__":
    main()
