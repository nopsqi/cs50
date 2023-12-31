import os
import random
import re
import sys
import math

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus.get(page)
    if len(links) == 0:
        probability = damping_factor / len(corpus)
        return {p: probability for p in corpus}

    random_probability = 1 - damping_factor
    link_probability = damping_factor / len(links)
    page_probability = random_probability / len(corpus)
    link_probability += page_probability
    result = {p: round(link_probability, 3) if p in links else round(page_probability, 3) for p in corpus}

    return dict(sorted(result.items()))


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    t_models = {}
    result = {key: 0 for key in corpus}
    page = random.choice(list(corpus))
    t_model = transition_model(corpus, page, damping_factor)
    for _ in range(n):
        page = random.choices(list(t_model.keys()), list(t_model.values()))[0]
        result[page] += 1
        t_model = t_models.get(page)
        if t_model is None:
            t_model = transition_model(corpus, page, damping_factor)
            t_models[page] = t_model

    return dict(sorted({key: round(value / n, 4) for key, value in result.items()}.items()))


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    length = {page: len(corpus[page]) if len(corpus[page]) > 0 else len(corpus) for page in corpus}
    length["corpus"] = len(corpus)
    starting_value = 1 / length["corpus"]
    rank = {page: starting_value for page in corpus}
    contain_page = {page: {p for p in corpus if page in corpus[p]} for page in corpus}
    diff = {page: math.inf for page in corpus}

    while any(d > 0.001 for d in diff.values()):
        rank_prev = rank.copy()
        for page in rank:
            rank[page] = (( 1 - damping_factor ) / length["corpus"]) + damping_factor * sum(rank[pr] / length[pr] for pr in contain_page[page])
        diff = {page: abs(rank[page] - rank_prev[page]) for page in corpus}

    return dict(sorted({r: round(rank[r], 4) for r in rank}.items()))


if __name__ == "__main__":
    main()
