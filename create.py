import sys 
import os
from github import Github

def git_init(foldername: str):
    token = os.environ.get('gt') 
    gh=Github(token)

    user = gh.get_user()
    login = user.login

    repo = user.create_repo(foldername)

    commands = [f'echo # {repo.name} >> README.md',
            'git init',
            'git add .',
            'git commit -m "Initial commit"',
            'git branch -M main',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git push -u origin main']

    for c in commands:
        os.system(c)
    
    print("git repository initialized and pushed to github")

def touch(name):
    with open(os.getcwd()+"/"+name,"w") as _:
        pass

def create_directory(foldername):

    path = str(os.environ.get('workspace_path'))
    _dir = path + "/" + foldername

    os.mkdir(_dir)
    os.chdir(_dir)

    # Possibility to create sass projects with a third parameter = "web" 
    if len(sys.argv)==3:
        if sys.argv[2] == "web":
            os.mkdir("css")
            os.mkdir("sass")
            touch("index.html")
            os.chdir("sass")
            touch("_main.scss")
            os.mkdir("abstracts")
            os.mkdir("base")
            os.mkdir("components")
            os.mkdir("layout")
            os.mkdir("pages")
            os.chdir(_dir)

    print(f'Project {foldername} created locally: {_dir}')

def main():
    # given as first parameter
    foldername = str(sys.argv[1])

    create_directory(foldername)
    git_init(foldername)
    
    os.system('code .')

if __name__ == "__main__":
    main()

    

 
    