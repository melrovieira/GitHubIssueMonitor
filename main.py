import requests

## TOKEN DE FICARÁ EM VARIAVEL DE AMBIENTE PROVISÓRIAMENTE.
import os
token = os.environ.get('GITHUB_TOKEN')

headers = {
    "Authorization": f"token {token}"
}
class Repositories:
    def __init__(self, repository_name, repository_owner):
        self.repository_name = repository_name
        self.repository_owner = repository_owner
        self.issues_labels = []

    def add_labels(self, issue_labels):
        self.issues_labels = issue_labels

    def search_issues(self):
        if not self.issues_labels:
            return ['None']

        results_issues = []
        for label in self.issues_labels:
            results_issues.append(
                requests.get(
                    f'https://api.github.com/search/issues?q=repo:{self.repository_owner}/{self.repository_name}+label:"{label}"&state:open', headers=headers).json()
            )
        return results_issues



