print("Welcome to the acronym generator!")

# Ask the user to enter the full meaning of an organization or concept
full_meaning = input("Please enter the full meaning of an organization or concept: ")

# Split the words of the full_meaning string into a list of words
words = full_meaning.split(" ")

# Create the acronym by looping through the list of words
acronym = ""
for word in words:
  acronym += word[0]

# Print the acronym
print("The acronym for '{}' is '{}'".format(full_meaning, acronym))
