import textwrap

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"

def display_issues(result):
    for label_result in result:
        total_count = label_result.get('total_count', 0)
        print(f"Total de issues para este label: {total_count}\n{'=' * 40}")

        for issue in label_result.get('items', []):
            url_issue = issue.get('html_url')
            number_issue = issue.get('number')
            title_issue = issue.get('title')
            reporter_issue = issue.get('user', {}).get('login')
            state_issue = issue.get('state')
            assignee_people = issue.get('assignee', {}).get('login') if issue.get('assignee') else None

            print(textwrap.dedent(f"""\
            Issue #{yellow}{number_issue}{reset}: {cyan}{title_issue}{reset}
            URL: {blue}{url_issue}{reset}
            Reportada por: {magenta}{reporter_issue}{reset}
            Estado: {red if state_issue == 'closed' else green}{state_issue}{reset}
            Designado: {magenta}{assignee_people}{reset}
            {'-' * 40}
            """))
