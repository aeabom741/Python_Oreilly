#extend()為結合串列
marxes = ['Harpo', 'Chico', 'Groucho','Zeppo']
other = ["Gummo",'Karl']
marxes.extend(other)
print(marxes)

marxes = ['Harpo', 'Chico', 'Groucho','Zeppo']
other = ["Gummo",'Karl']

marxes += other
print(marxes)

marxes = ['Harpo', 'Chico', 'Groucho','Zeppo']
other = ["Gummo",'Karl']
marxes.append(other)
print(marxes)