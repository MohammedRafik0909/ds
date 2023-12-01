sub = ['Math', 'English', 'Science', 'Math', 'History', 'English', 'Math', 'Science', 'Science']
sub_fre ={}

for i in sub:
    if i in sub_fre:
        sub_fre[i]+=1
    else:
        sub_fre[i]=1
print("subject frequency distribution")
for i,j in sub_fre.items():
    print(f"{i}:{j}students")
most_popular_subject = max(sub_fre, key=sub_fre.get)
print(f"\nThe most popular subject is: {most_popular_subject} with {sub_fre[most_popular_subject]} students.")
