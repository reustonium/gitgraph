from subprocess import check_output
import re


def locgraph():
    logs = check_output('git log --pretty=format:"%ai" --shortstat').decode('utf-8')

    dates=[]
    data=[]
    commits = logs.split('\n\n')
    for commit in commits:
        date = re.match(r'(.*)', commit)
        dates.append(date.group(0)[:-5])

        additions = commit.split('\n')[1].split(' insertion')[0][-1:]
        data.append(additions)
