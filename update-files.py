import os
import sys
#import yaml
from ruamel.yaml import YAML



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
  yaml = YAML()
  yaml.preserve_quotes = True
  with open(f'workflows/cicd.yml') as istream:
    wf_file = yaml.load(istream)
    wf_file['jobs']['dotnet-build']['with']['app_dir'] = app_dir

  print(wf_file,'=========')

  with open(f'workflows/cicd-output.yaml', 'w') as ostream:
    yaml.dump(wf_file, ostream)
