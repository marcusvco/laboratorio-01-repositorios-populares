from datetime import datetime


class Repository:
    def __init__(self, name, stars, created_at, open_issues_count, pull_requests_count, releases_count, language, closed_issues_count):
        self.name = name
        self.stars = stars
        self.created_at = created_at
        self.open_issues_count = open_issues_count
        self.pull_requests_count = pull_requests_count
        self.releases_count = releases_count
        self.language = language
        self.closed_issues_count = closed_issues_count

    def getAge(self):
        created_at_dt = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.now()
        age = now.year - created_at_dt.year
        return age
    
    def print(self):
        print(f"Repository: {self.name}")
        print(f"Stars: {self.stars}")
        print(f"Created at: {self.created_at}")
        print(f"Open issues: {self.open_issues_count}")
        print(f"Pull requests: {self.pull_requests_count}")
        print(f"Releases: {self.releases_count}")
        print(f"Language: {self.language}")
        print(f"Closed issues: {self.closed_issues_count}")
        print("================================")
