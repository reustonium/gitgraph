from subprocess import check_output
import re


def locgraph():
    logs = check_output('git log --pretty=format:"%ai" --shortstat')
    logs = logs.decode('utf-8')
    commits = re.split(r'(.)\n\n', logs)
    for commit in commits:
        print('new')
        print(commit)

