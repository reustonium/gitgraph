from subprocess import call


def locgraph():
    logs = call('git log --pretty=format:"%ai" --shortstat')
    print(logs)
    print('hi')
