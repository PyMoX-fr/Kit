import subprocess
import re
from collections import defaultdict

# 🔧 Paramètres personnalisables
MAX_COMMITS = 100  # Limite d'affichage
GITHUB_REPO_URL = "https://github.com/PyMoX-fr/PyMoX-fr.github.io/commits/main"


def run_git_log():
    output = subprocess.check_output(
        ["git", "log", "--pretty=format:%h|%an|%ad|%s", "--date=short"]
    ).decode("utf-8")
    print(output) 
    return output.splitlines()


def detect_versions(commits):
    version_pattern = re.compile(r"(?:chore\(release\):|Set\s+v|v\s*)?(\d+\.\d+\.\d+)")
    # version_pattern = re.compile(r"chore\(release\):\s*v?(\d+\.\d+\.\d+)")

    versions = []
    for i, line in enumerate(commits):
        parts = line.split("|", 3)
        if len(parts) < 4:
            continue
        message = parts[3]
        match = version_pattern.search(message)
        if match:
            version = match.group(1)
            versions.append((i, version))
    return versions


def group_commits_by_version(commits, versions):
    grouped = defaultdict(list)
    versions = [(None, "Unreleased")] + versions + [(len(commits), None)]

    for i in range(len(versions) - 1):
        start_idx = versions[i][0]
        version_name = versions[i][1]
        end_idx = versions[i + 1][0]
        for line in commits[start_idx + 1 if start_idx is not None else 0 : end_idx]:
            grouped[version_name].append(line)
    return grouped


def format_changelog(grouped):
    changelog = "# Changelog\n\n"
    count = 0

    for version, entries in grouped.items():
        if count >= MAX_COMMITS:
            break
        changelog += f"## v{version}\n\n"
        for line in entries:
            if count >= MAX_COMMITS:
                break
            hash_, author, date, message = line.split("|", 3)
            changelog += f"- {message} ({author}, {date})\n"
            count += 1
        changelog += "\n"

    changelog += f"\n\n\n## 👉 [1234567 Voir plus sur GitHub]({GITHUB_REPO_URL})\n"
    return changelog


if __name__ == "__main__":
    commits = run_git_log()
    # commits = list(reversed(commits))
    versions = detect_versions(commits)
    grouped = group_commits_by_version(commits, versions)
    changelog = format_changelog(grouped)

    with open("docs/outils/logs/CHANGELOG.md", "w", encoding="utf-8") as f:
        f.write('oki22<br>\n\n---')
        f.write(changelog)

    print("✅ Changelog généré avec limite et lien vers GitHub")
