from pagerank import *


def main():
    corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
    t_model = transition_model(corpus, "1.html", DAMPING)
    print(t_model)


if __name__ == "__main__":
    main()