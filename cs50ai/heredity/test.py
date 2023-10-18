from heredity import *


def main():
    people = load_data("data/family0.csv")

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
    names = set(people)
    p_set = powerset(names)
    joint = joint_probability(people, {"Harry"}, {"James"}, {"James"})
    print(p_set)
    print(powerset(names - {"James", "Harry"}))


if __name__ == "__main__":
    main()