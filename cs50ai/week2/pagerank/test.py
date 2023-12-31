from pagerank import *


def main():
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    corpus = crawl("corpus0")
    t_model = transition_model(corpus, "1.html", DAMPING)
    s_pagerank = sample_pagerank(corpus, DAMPING, 10000)
    it_pagerank = iterate_pagerank(corpus, DAMPING)
    print(s_pagerank)
    print(it_pagerank)


if __name__ == "__main__":
    main()