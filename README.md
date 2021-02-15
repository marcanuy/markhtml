Markdown to HTML
====================

Markdown to HTML converter. Converts a Markdown file into an HTML file
formed of two columns:

- TOC (left-column)
  - An auto generated Table of Contents based in the markdown headings
- Markdown content (right-column)

![example](https://raw.githubusercontent.com/marcanuy/markhtml/main/example.png)


# Install

1. Create virtualenv.

~~~
python3 -m venv ~/.virtualenvs/markhtml
~~~

2. Activate venv.

~~~
source ~/.virtualenvs/markhtml/bin/activate
~~~

3. Install requirements.
   
~~~
pip install -r requirements.txt
~~~

# Notes

Uses
[python-markdown](https://python-markdown.github.io/reference/index.html)
with [TOC](https://python-markdown.github.io/extensions/toc/#usage) extension.
