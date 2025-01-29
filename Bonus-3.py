Phrase = input()
mots = Phrase.split()
voyelle = ["a","A","e","E","i","I","o","O","u","U"]
vowel_list = 0
print(f"caractere= {len(Phrase)}")
print(f"mots= {len(mots)}")

for i in range(0,len(Phrase)):
    if Phrase[i] in voyelle:
        vowel_list = vowel_list + 1

print(f"voyelle= {vowel_list}")