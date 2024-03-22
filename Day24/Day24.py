print("Day 24 - 100 Days of Code.")
print("Welcome to Mail Merger!")

birthday_invitation = "./Output/Birthday Invitation "
text_file = ".txt"
list_of_invitees = []
with open("./Input/Names/ListOfInvitees.txt", mode="r") as invitees:
    for line in invitees:
        list_of_invitees.append(line.replace("\n", ""))
    else:
        print("Went through the entire list of invitees.")

for invitee in list_of_invitees:
    starting_letter = open("./Input/Letter/StartingLetter.txt", mode="r")
    new_file_name = birthday_invitation + invitee + text_file
    new_file = open(new_file_name, mode="w")
    for line in starting_letter:
        new_file.write(line.replace("[Name]", invitee))
    else:
        new_file.close()
        starting_letter.close()
print("Birthday invitations generated for all the invitees.")
