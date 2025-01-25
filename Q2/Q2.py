print("Do you want some snacks? (yes/no): " )
snack = input()
if snack == "no" :
    print("Good! Let's paly games instead.")
elif snack == "yes" :
    print("Enter your choice (ice-cream / cookies / candies ): " )
snack_choice = input()
if snack_choice == "ice-cream" :
    print("Remember to wash your hands")
elif snack_choice == "cookies" :
    print("Can you share with your friends?")
else: 
    print("Dont's eat too much")
