#Let’s say you want to skip counting sheep that are number 4:

sheep_count = 1

while sheep_count<=5:
    if sheep_count==4:
        sheep_count+=1
        continue
    print(f"sheep {sheep_count}")
    sheep_count+=1
   
