# 5. Simulate supervised learning by writing a function that learns from labeled input data and prints the learned labels.

def supervised_learning(data):
    learned_labels = {}
    for feature, label in data:
        learned_labels[feature] = label
    print("Learned Labels:", learned_labels)

supervised_learning([("cat", "animal"), ("rose", "flower"), ("2", "number")])
