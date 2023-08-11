import wikipedia


def main():
    wiki_page = input("Enter wiki page tile/ search phrase: ")
    page = wikipedia.page(wiki_page, auto_suggest=False)
    while wiki_page != "":
        print(wikipedia.summary(page))
        wiki_page = input("Enter wiki page tile/ search phrase: ")


main()
