#!/usr/bin/env python
import argparse
import markdown
from string import Template


def initialize_parser():
    md = markdown.Markdown(extensions=['toc'])
    return md

def read_filename():
    parser = argparse.ArgumentParser(description='Convert a MD file into HTML.')
    parser.add_argument('filename', nargs='+',
                        help='The markdown filename')

    args = parser.parse_args()
    filename = args.filename[0]
    return filename

def open_file(filename):
    with open("input.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        return text

def render(html, toc):
    context = {'content':html, 'toc':toc}
    with open('src/template.html', 'r') as f:
        src = Template(f.read())
        result = src.substitute(context)
        return result

def save(text):
    with open("output.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(text)
    
    
def main():
    filename = read_filename()
    md = initialize_parser()
    text = open_file(filename)
    html = md.convert(text)
    toc = md.toc
    page = render(html,toc)
    save(page)
    
if __name__ == "__main__":
    main()
