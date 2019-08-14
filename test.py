with open('t.txt', 'r+') as f1:
     dict = {}
     for line in f1:
         (key, val) = line.split()
         dict[str(key)] = val
     def add_words(w1,s1):
         new_words = {w1:s1}

         added = False       
         for k in dict.keys():
             if k in new_words.keys():
                 dict[k] = [dict[k]] # Reassign the fruit into a list format
                 dict[k].append(new_words[k])  # Append new fruit into the inputlist
                 added = True
                 break       
         if not added:
             dict.update(new_words)
             f1.write(f'\n{w1}')
             f1.write(f' {s1}')
     add_words('green', 'hello')
     print(dict)
