# There are some very useful operations that are specific to str
# You can find a full list of str-specific methods on this webpage: https://docs.python.org/3/library/stdtypes.html#string-methods
# I will  describe a few of them here.

# replace(old,new)
text = "First they champ, then they stamp."
new_text = text.replace("they","we")  # remember, str is immutable -- you must always use assignment to save a modified str value
print("new_text:",new_text)
# str.replace() finds each instance within itself of the 'old' argument substring and replaces it with the contents of the 'new' argument


# split(sep)
text = "1-1-2-3-5-8-13"
split_list = text.split("-")
print("split_list:",split_list)
# str.split() creates a list where the elements are the contents of the original str that were separated by 'sep'
# a more useful example:
sentence = "I can't believe it's not butter!"
words = sentence.split(" ")
print("words:",words)

# join(iterable)
remade_sentence = " ".join(words)   #  " " is the separator being used to join
print("remade_sentence:",remade_sentence)
# str.join() is the reverse of str.split()
# it is applied to a separator and takes a list of substrings as an argument
# it creates a new str which is the concatenation of the elements of 'iterable' with the separator inserted between each pair of substrings


# lower() and upper()
angry = "I'M YELLING REALLY LOUD RIGHT NOW"
calm = angry.lower()
print("calm:",calm)
angry_again = calm.upper()
print("angry_again:",angry_again)
# str.lower() takes all the letters in a str and converts them to lower-case
# str.upper() takes all the letters in a str and converts them to upper-case
