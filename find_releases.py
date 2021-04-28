from datetime import datetime as dt
from github import Github

import os

repos = [
    'pydata/sparse',
    'ipython/ipython',
    'ipython/ipykernel',
    'sympy/sympy',
    'pytorch/pytorch',
    'scipy/scipy',
    'numpy/numpy',
    'jupyterlab/jupyterlab',
    'deshaw/pyflyby',
    'spyder-ide/spyder',
]

QUANSIGHT_BOT_TOKEN = os.environ.get("QUANSIGHT_BOT_TOKEN")
gh = Github(QUANSIGHT_BOT_TOKEN)
today = dt.today()
new_releases = []
for repo in repos:
    r = gh.get_repo(repo)
    release = r.get_tags()[0]
    latest = release.commit.raw_data['commit']['author']['date']
    latest = dt.strptime(latest, '%Y-%m-%dT%H:%M:%SZ')

    if (today - latest).days < 30:
        new_releases.append(' '.join([repo, release.name, latest.strftime('%m-%d-%Y')]))

with open('new_releases.txt', 'w') as f:
    f.write('\n'.join(new_releases))
