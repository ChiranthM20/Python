# 8. Use a Python program to store features of AI and natural intelligence and print the categorized comparison.

def compare_ai_natural():
    comparison = {
        "Artificial Intelligence": ["Fast computation", "Data-driven learning", "No emotions"],
        "Natural Intelligence": ["Creative thinking", "Emotional understanding", "Adaptability"]
    }
    for category, features in comparison.items():
        print(f"\n{category}:")
        for feature in features:
            print("-", feature)

compare_ai_natural()