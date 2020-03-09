from parsel import Selector

from cliparse.html import text


def execute(name, element):
    print(f'Hello {name}')
    html_title = Selector(text).xpath('//title/text()').get()
    print(f'This is title of your html: {html_title}')
    html_list = Selector(text).xpath(element)
    for e in html_list:
        print(e.get())
