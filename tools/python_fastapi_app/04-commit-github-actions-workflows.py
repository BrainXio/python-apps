import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def create_branch(branch_name):
    run_command(f"git checkout -b {branch_name}")

def add_files(directory):
    run_command(f"git add {directory}")

def commit_files(message):
    run_command(f'git commit -m "{message}"')

def push_branch(branch_name):
    run_command(f"git push -u origin {branch_name}")

def main():
    branch_name = "feature/add-github-actions-workflows"
    create_branch(branch_name)
    
    github_dir = ".github"
    if os.path.exists(github_dir):
        add_files(github_dir)
        commit_files("Add GitHub Actions workflows and Dependabot configuration")

    push_branch(branch_name)

if __name__ == "__main__":
    main()
