import wordgen

word = wordgen.generate_word()
num_syllable = wordgen.syllable_count(word)

print(word + ", syllables: " + str(num_syllable))

