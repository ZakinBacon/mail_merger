#TODO: Create a letter using starting_letter.txt

name_replace = "[name],"

with open("../mail_merger/Input/Letters/starting_letter.txt", mode="r") as letter:
    contents = letter.read()
    print(contents)

with open("../mail_merger/Input/Names/invited_names.txt", mode="r") as names:
    names = names.read()
    filtered_names = names.split()
    count = 0

for name in filtered_names:
    print(filtered_names[count])
    with open(f"../mail_merger/Output/ReadyToSend/{filtered_names[count]}", mode="w") as file:
        new_contents = contents.replace("[name]", filtered_names[count])
        file.write(new_contents)
    count += 1

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp