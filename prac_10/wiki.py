import wikipedia


def main():
    wiki_page = input("Enter wiki page tile/ search phrase: ")
    while wiki_page != "":
        page = wikipedia.page(wiki_page, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(page))
        print(page.url)
        wiki_page = input("Enter wiki page tile/ search phrase: ")


main()
