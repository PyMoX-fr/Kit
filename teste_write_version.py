import re

with open("src/pymox_tools1/__init__.py", "r+") as f:
    content = f.read()
    content = re.sub(
        r'__version__\s*=\s*["\'].*?["\']', '__version__ = "0.10.0"', content
    )
    f.seek(0)
    f.write(content)
    f.truncate()
