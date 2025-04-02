print("Welcome to the Telegram Application".center(10,"*"))
#Profile data
Profile={
    "User_name":"Anu123",
    "Bio":"Hey there I'm using Telegram",
    "Mobile_number":"868818XXXx"
}
#Contact list
Contact_list=['sujji','akki','anu','pavi','madhu']
#Settings
Settings={
    "Notifications":True,
    "Privacy":"Everyone can see my profile"
}
#Chats
Chats={
    "sujji":["Hai.."],
    "akki":["Where are u..?"],
    "anu":["What are u dng..?"],
    "pavi":["call mee"],
    "madhu":["Hello...!"]
}
#using while loop for selecting opeartions we want to do
while(True):
    print("\nSelect option you want to perform:")
    print("1.Contact_list")
    print("2.Chats")
    print("3.Profile")
    print("4.Settings")
    print("5.Exit")
    option=input("Enter ur option to perform (1-5): ")
#performing operation on contact list
    if option=="1":
        print("Contacts list")
        for contact in Contact_list:
            print(f"-{contact}")
        print("You want to add a new contact?")
        add_contact=input("press 'yes' to add or 'no' to go back: ").lower()
        if add_contact=='yes':
            new_contact=input("Enter new contact: ")
            if new_contact not in Contact_list:
                Contact_list.append(new_contact)
                print("New contact {} added".format(new_contact))
            else:
                print("Already exits")
        elif add_contact=='no':
            print("Going back to home")
        else:
            print("Invalid")

#operations on chats
    elif option=="2":
        print("\nSelect a contact to chat: ")
        for contacts in Contact_list:
            print(f" {contacts}")
        
        contact_name = input("Enter the contact name: ")
        if contact_name in Chats:
            print(f"\nChat with {contact_name}:")
            for message in Chats[contact_name]:
                print(f"{contact_name}: {message}")
            
            new_message = input(f"\nSend a message to {contact_name}: ")
            Chats[contact_name].append(new_message)
            print(f"Message sent to {contact_name}: {new_message}")
        else:
            print("Contact not found.")
#operations on profile
    elif option == "3":
        print("My profile")
        print(f"User_name :{Profile['User_name']}")
        print(f"Bio : {Profile['Bio']}")
        print(f"Mobile_number : {Profile['Mobile_number']}")
        print("Would you like to update ur profile?")
        print("1.Update Bio")
        print("2.Update mobile_number")
        update_profile=input("Enter ur choice (1-2):")
        if(update_profile=='1'):
            new_bio=input("Enter new bio: ")
            Profile['Bio'] = new_bio
            print(f"New bio updated as {Profile['Bio']}")
        elif(update_profile=='2'):
            new_num=int(input("Enter the new number: "))
            Profile["Mobile_number"] = new_num
            print(f"Mobile number updated to {Profile['Mobile_number']}")
        else:
            print("Invalid...!")
#operations on settings   
    elif option == "4":
        print("Your current setting")
        print(f"Notifications :{Settings['Notifications']}")
        print(f"Privacy :{Settings['Privacy']}")
        print("Want to do changes in settings..?")
        print("1.Changes in notification")
        print("2.Changes in privacy mode")
        Changes=input("Enter ur choice (1-2):")
        if Changes =='1':
            Settings['Notifications'] = not Settings['Notifications']
            print(f"Notifications are now {'Enabled' if Settings['Notifications'] else 'Disabled'}.")
        elif Changes == '2':
            new_privacy = input("Enter new privacy setting (e.g., 'Everyone can contact me', 'Only contacts can contact me'): ")
            Settings['Privacy'] = new_privacy
            print(f"Privacy setting updated to: {Settings['Privacy']}")
        else:
            print("Invalid choice.")
    
    elif option =="5":
        print("Existing from the app..!")
        break

    else:
        print("Invalid option..Please select correct option from(1-5)")