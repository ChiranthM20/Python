'''Read and Count Lines

Read any file and count how many lines it has.
Example: How many students are listed?'''



with open("append.txt", "r") as file:
    lines = file.readlines()          
    count = len(lines)                
    print(f"Total lines: {count}")
