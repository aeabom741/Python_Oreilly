from collections import Counter
breakfast = ['spam','spam','spam','egg']
breakfast_count = Counter(breakfast)

print(breakfast_count.most_common())

lunch = ['egg','egg','bacon']
lunch_count = Counter(lunch) 
print(breakfast_count + lunch_count)
print(breakfast_count & lunch_count)
print(lunch_count - breakfast_count) 
print(breakfast_count | lunch_count)  