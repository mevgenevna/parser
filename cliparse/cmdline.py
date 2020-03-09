import argparse

from cliparse.commands import find_html


def parse():
    parser = argparse.ArgumentParser(prog='scraper')
    parser.add_argument('-g', '--greeting', metavar='NAME', default="world", help='greet NAME', dest='name')
    parser.add_argument('--xpath', default="//*", help='html element', dest='xpath')
    args = parser.parse_args()
    find_html.execute(args.name, args.xpath)


