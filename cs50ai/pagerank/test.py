from pagerank import crawl, transition_model, sample_pagerank, iterate_pagerank


def main():
    c = crawl("corpus1")
    print(c)


if __name__ == "__main__":
    main()