strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
group = {}
for i in strs :
  kelime = "".join(sorted(i))
  if kelime in group :
    group[kelime].append(i)
  else :
    group[kelime] = [i]
print(group)














