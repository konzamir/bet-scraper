from scrapers.scrapers import BookmakerScraper


def main():
    bookmaker = BookmakerScraper()
    result = bookmaker.scrape()
    print(result)


if __name__ == '__main__':
    main()
