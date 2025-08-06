# import flet as ft # Just for local dev for hotreload

import subprocess, re
from collections import defaultdict

# 🔧 Paramètres personnalisables
MAX_COMMITS = 21  # Limite d'affichage
CHANGELOG_PATH = "docs/outils/logs/CHANGELOG.md"
GITHUB_REPO_URL = "https://github.com/PyMoX-fr/PyMoX-fr.github.io/commit"


def get_git_log():
    output = subprocess.check_output(
        [
            "git",
            "log",
            f"--max-count={MAX_COMMITS}",
            "--pretty=format:%h|%an|%ad|%s %d",
            "--date=short",
        ]
    ).decode("utf-8")
    return output.splitlines()


def extract_tag(line):
    match = re.search(r"tag:\s*([^\),]+)", line)
    return match.group(1) if match else None


def group_commits_by_tag(commits):
    tag_commits = defaultdict(list)
    current_tag = "Unreleased"

    for commit in commits:
        tag = extract_tag(commit)
        if tag:
            current_tag = tag
        tag_commits[current_tag].append(commit)

    return tag_commits


def format_changelog(tag_commits):
    lines = ["# 📝 Changelog\n"]
    for tag, commits in tag_commits.items():
        lines.append(f"\n## 📦 Version `{tag}`\n")
        for commit in commits:
            parts = commit.split("|")
            if len(parts) >= 4:
                sha, author, date, message = parts[:4]
                commit_url = f"{GITHUB_REPO_URL}/{sha}"
                # f"* {date} : [{message}]({commit_url}) by **{author}** (`{sha}`)"
                lines.append(
                    f"* {date} : [{message}]({commit_url}) (`{sha}`)"
                )
    return "\n".join(lines)


def update_changelog_file(content):
    with open(CHANGELOG_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def showChangelog():
    commits = get_git_log()
    grouped = group_commits_by_tag(commits)
    content = format_changelog(grouped)
    update_changelog_file(content)


if __name__ == "__main__":
    showChangelog()
    print("✅ Changelog généré avec succès 12 34 !")
    print("Ready.")
