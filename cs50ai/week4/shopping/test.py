from shopping import *


def main():
    evidence, labels = load_data("shopping.csv")
    model = train_model(evidence, labels)
    predictions = model.predict()


if __name__ == "__main__":
    main()