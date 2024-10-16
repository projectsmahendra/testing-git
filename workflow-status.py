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
run_id = os.getenv('INFRA_WORKFLOW_ID')
repo_name = os.getenv('repo_name')

try:
    for i in range(0, 60):
        print(f"https://api.github.com/repos/{repo_name}/actions/runs/{run_id}")
        response = requests.get(
            f"https://api.github.com/repos/{repo_name}/actions/runs/{run_id}",
            headers=headers
        ).json()
        if response.get('status') == "completed":
            if response.get('conclusion') == "success":
                print("================================================")
                print("SUCCESS")
                print("================================================")
                break
            else:
                print("------------------------------------------------")
                print("FAILURE")
                print("------------------------------------------------")
                raise
        else:
            print(f"The job is being run: {response.get('status')}")
        time.sleep(30)
        if i == 59:
            print(f"The job is unable to complete/start within given time - pls check below URL for more information")
            print(run_log_url)

except Exception as err:
    print(f"Exception occurred while processing your request - please verify the logs for more information")
    print(err)
    raise
