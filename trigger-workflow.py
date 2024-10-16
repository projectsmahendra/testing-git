import os
import sys
import time
import json
import requests

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
    "X-GitHub-Api-Version": "2022-11-28",
    "Content-Type": "application/x-www-form-urlencoded"
}
repo_name = os.getenv('repo_name')
workflow_name = os.getenv('workflow_name')
branch = os.getenv('branch', 'main')

data = {"ref":branch}

try:
    response = requests.post(
        f"https://api.github.com/repos/{repo_name}/actions/workflows/{workflow_name}/dispatches",
        headers=headers,
        json=data
    )
    time.sleep(10) # Need to put program to sleep as it takes sometime for GitHub to invoke the run
    if response.status_code in (200, 204):
        run_id = requests.get(
            f"https://api.github.com/repos/{repo_name}/actions/workflows/{workflow_name}/runs",
            headers=headers
        ).json().get('workflow_runs')[0].get('id')

        run_log_url = f"https://api.github.com/repos/{repo_name}/actions/runs/{run_id}"
        print("run_log_url",run_log_url)
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            print(f"INFRA_WORKFLOW_ID={run_id}", file=f)
    else:
        print("-----------------------------------")
        print(f"ERROR: Failed to run the workflow")
        print(response.status_code, response.content)
        raise

except Exception as err:
    print(f"Exception occurred while processing your request - please verify the logs for more information")
    print(err)
    raise
