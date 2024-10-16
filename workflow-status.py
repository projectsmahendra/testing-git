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

try:
    while True:
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
        time.sleep(10)

except Exception as err:
    print(f"Exception occurred while processing your request - please verify the logs for more information")
    print(err)
    raise
