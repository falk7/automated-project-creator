import os
import sys
from github import Github

def main():
    project_name = str(sys.argv[1])
    workspace_path = "C:/Users/falka/Workspace"
    directory_path = workspace_path + "/" + project_name

    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
        os.chdir(directory_path)
        print(f'Projekt lokal erstellt: {directory_path}')

        github_access_token = os.environ.get('gt')
        gh=Github(github_access_token)
        
        user = gh.get_user()
        login = user.login

        repo = user.create_repo(project_name)

        commands = [f'echo # {repo.name} >> README.md',
        'git init',
        'git add .',
        'git commit -m "Initial commit"',
        'git branch -M main',
        f'git remote add origin git@github.com:{login}/{project_name}.git',
        'git push -u origin main']

        for c in commands:
            os.system(c)
    
        print("git repository initialisiert und nach github gepusht")


    else:
        print(f"Projekt {project_name} existiert bereits im Workspace {workspace_path}")



if __name__ == "__main__":
    main()