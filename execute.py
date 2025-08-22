import argparse
from main import Repositories
from display import display_issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-name', type=str, required=True, help='Repository name')
    parser.add_argument('--repo-owner', type=str, required=True, help='Repository owner, The account that created the repository')
    parser.add_argument('--labels', nargs='+', type=str, required=True, help="Labels of the wanted issues (use '' if labels have spaces)")
    args = parser.parse_args()

    repos = Repositories(args.repo_name, args.repo_owner)
    repos.add_labels(args.labels)
    result = repos.search_issues()

    display_issues(result)

if __name__ == '__main__':
    main()
