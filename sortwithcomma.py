input_sequence = input("Enter a comma-separated value of sequence of words : ")
words = input_sequence.split(',')
sorted_words = sorted(words)
sorted_join = ','.join(sorted_words)
print("Sorted words : ",sorted_join)