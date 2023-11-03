#word=input("Enter a word:").lower()
def count_occur(word):
  dict={}
  for letter in word:
    key=dict.keys()
    if letter in key:
      dict[letter]+= 1
    else:
      dict[letter]=1
  print(dict)

count_occur('america')