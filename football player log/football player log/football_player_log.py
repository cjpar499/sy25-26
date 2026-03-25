


from multiprocessing import pool


while True:  
    print("1. add player, 2. delete player, 3. view players, 4.edit lineup 5. exit")  
    choice = int(input("Choose an option: "))
    
    if choice ==1:  
        name = input("Enter player name: ")  
        position = input("Enter player position: ")  
        height = input("Enter player height: ")
        weight= input("Enter player weight: ")
        with open("position.txt", "a") as f:  
            f.write(f"name:{name},   height:{height},   weight: {weight},   position: {position}\n")  
            f.close()
   
    elif choice == 2:
        with open("position.txt", "r") as f:  
            players = f.readlines()  
        for i, line in enumerate(players):  
            print(f"{i+1}. {line.strip()}")  
        delete = int(input("Choose a player number to delete: "))  
        del players[delete - 1]  
        with open("position.txt", "w") as f:  
            f.writelines(players)
            f.close()
    
    elif choice == 3:
        with open("position.txt", "r") as f:  
            for line in f:  
             print(line.strip())  

    elif choice == 4:
        with open("position.txt", "r") as f:  
            players = f.readlines()  
        for i, line in enumerate(players):  
            print(f"{i+1}. {line.strip()}")  
        edit = int(input("Choose a player number to edit: "))  
        poo=int(input("1. Name\n2. Position\n3. Height\n4. Weight"))
        if poo== 1:
             name = input("Enter new player name: ")
             player_line = players[edit - 1].strip()  
             parts = player_line.split(",") 
             parts[0] = "name:" + name 
             players[edit - 1] = ",".join(parts) + "\n"  
             with open("position.txt", "w") as f:  
                f.writelines(players)  
        if poo== 2:
             position = input("Enter new player position: ")
             player_line = players[edit - 1].strip()  
             parts = player_line.split(",") 
             parts[3] = "position:" + position 
             players[edit - 1] = ",".join(parts) + "\n"  
             with open("position.txt", "w") as f:  
                f.writelines(players)
        if poo== 3:
                height = input("Enter new player height: ")
                player_line = players[edit - 1].strip()  
                parts = player_line.split(",") 
                parts[1] = "height:" + height 
                players[edit - 1] = ",".join(parts) + "\n"  
                with open("position.txt", "w") as f:  
                    f.writelines(players)
        if poo== 4:
                weight = input("Enter new player weight: ")
                player_line = players[edit - 1].strip()  
                parts = player_line.split(",") 
                parts[2] = "weight:" + weight 
                players[edit - 1] = ",".join(parts) + "\n"  
                with open("position.txt", "w") as f:  
                    f.writelines(players)
          
          
         
           
    elif choice == 5:  
        break  

    else:
        print("Invalid choice. Please try again.")
