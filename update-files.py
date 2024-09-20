import os
import sys
import yaml



if __name__ == '__main__':
  
  # CI Values
  cwd = os.getcwd()
  print(cwd,"========")
  sys.path.append(cwd)
  APPLICATION_TYPE = os.environ.get('APPLICATION_TYPE')
  app_dir = "api/1-Api/PROJECTNAME.Api" if APPLICATION_TYPE == "1" else "api/PROJECTNAME.Api"
  environment = "Dev Integration"

  #########################################
  ''' CUSTOMIZE GITHUB ACTIONS CI FILES '''
  #########################################
  with open(f'{cwd}/workflows/cicd.yaml') as istream:
    wf_file['jobs']['dotnet-build']['with']['app_dir'] = app_dir

  with open(f'{cwd}/workflows/cicd-output.yaml', 'w') as ostream:
    yaml.safe_dump(wf_file, ostream, width=1000, default_flow_style=False, sort_keys=False)
