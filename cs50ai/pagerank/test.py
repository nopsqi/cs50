from pagerank import *


def main():
    corpus = crawl("corpus0")
    t_model = transition_model(corpus, "1.html", DAMPING)
    print(t_model)


if __name__ == "__main__":
    main()