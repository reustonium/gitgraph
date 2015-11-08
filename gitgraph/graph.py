from subprocess import check_output
import re


def locgraph():
    logs = check_output('git log --pretty=format:"%ai" --shortstat').decode('utf-8')
    #
    commits = logs.split('\n\n')
    for commit in commits:
        date = re.match(r'(.*)', commit)
        print(date.group(0)[:-5])

