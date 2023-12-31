import csv
from functools import reduce
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    zero_gene = {p for p in people if p not in one_gene | two_genes}


    def calculate(person, people=people, zero_gene=zero_gene, one_gene=one_gene, two_genes=two_genes, have_trait=have_trait):
        index = lambda p: 0 if p in zero_gene else 1 if p in one_gene else 2 if p in two_genes else None

        if not (people[person]["father"] and people[person]["mother"]):
            return PROBS["gene"][index(person)] * PROBS["trait"][index(person)][person in have_trait]

        parent_case = {0: PROBS["mutation"], 1: 0.5, 2: 1 - PROBS["mutation"]}
        person_case = {
            0: lambda: (1 - parent_case[index(people[person]["father"])]) * (1 - parent_case[index(people[person]["mother"])]),
            1: lambda: (1 - parent_case[index(people[person]["father"])]) * parent_case[index(people[person]["mother"])] + (1 - parent_case[index(people[person]["mother"])]) * parent_case[index(people[person]["father"])],
            2: lambda: parent_case[index(people[person]["father"])] * parent_case[index(people[person]["mother"])]
        }

        return PROBS["trait"][index(person)][person in have_trait] * person_case[index(person)]()


    probs = lambda data: {p: calculate(p) for p in data}
    # print("0 \t", zero_gene, end="\t")
    # print(probs(zero_gene).values())
    # print("1 \t", one_gene)
    # print("2 \t", two_genes)
    # print("t \t", have_trait)
    if one_gene == {"Harry", "Lily", "James"} and have_trait == {"James"}:
        print(probs(one_gene))

    return reduce(lambda x, y: x * y, itertools.chain(probs(zero_gene).values(), probs(one_gene).values(), probs(two_genes).values()))


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    zero_gene = {p for p in probabilities if p not in one_gene | two_genes}


    index = lambda p: 1 if p in one_gene else 2 if p in two_genes else 0 if p in zero_gene else None


    for person in probabilities:
        probabilities[person]["gene"][index(person)] += p
        probabilities[person]["trait"][person in have_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    def calculate(distribution):
        total = sum(distribution.values())
        return {probability: distribution[probability] / total for probability in distribution}


    for person in probabilities:
        probabilities[person] = {kind: calculate(probabilities[person][kind]) for kind in probabilities[person]}


if __name__ == "__main__":
    main()
