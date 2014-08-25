game = {}
game.running = true
game.state = "char_create" -- char_create == character creation | game == game loop

player = {}
player.name = ""
player.hp = 100
player.level = 1
player.class = ""
player.inventory = {}
player.classMade = false
player.dead = false
player.location = "Main Hall"






function handlePlayerLocation()
    if player.location == "Main Hall" then
        player.locationDescription = "You are standing in the middle of a narrow hall. There are three doors."
    elseif player.location == "Door 1" then
        player.locationDescription = "You are where door 1 leads good sir!"
        if r == nil then r = math.random(1,5) end
        player.locationDescription = "There are " .. r .. " monsters in front of you!"
    elseif player.location == "Door 2" then
        player.locationDescription = "You are where door 1 leads good sir!"
        if r == nil then r = math.random(1,5) end
        player.locationDescription = "There are " .. r .. " monsters in front of you!"
    elseif player.location == "Door 3" then
        player.locationDescription = "You are where door 1 leads good sir!"
        if r == nil then r = math.random(1,5) end
        player.locationDescription = "There are " .. r .. " monsters in front of you!"
    end
end


while game.running == true do

    if game.state == "char_create" then

        print("Welcome to ZockRPG!\n")
        print("Name your character...")
        player.name = io.read()

        if player.classMade == false then
            print("Will you be a Human, Elf, or God? (human, elf, or god)")
            print("Please type clearly..............")
            player.class = io.read()
            if player.class == "human" or player.class == "elf" or player.class == "god" then
                player.classMade = true
            else
                print("Type human, elf, or god please! >_>")
            end
        end
        
        print("Ok, your character name is " .. player.name .. " and you are a " .. player.class .. "!\n")
        print("For command list, type 'help'...")
        print("The rest you will learn on the way! Goodluck adventurer!")
        print("Tell JesseH how much you love his game!")

        
        game.state = "game"

    elseif game.state == "game" then -- THIS IS THE GAME LOOP
        
        if player.dead == false then
            handlePlayerLocation()
            print(player.locationDescription .. "\n" .. player.location .. "\n" .. "What will you do?")
            choice = io.read()
            if choice == "attack" then
                if r ~= nil then
                    killed = math.random(1,2)
                    if killed == 1 then
                        success = true
                        r = r - 1
                    else
                        player.hp = player.hp - 10
                        success = false
                    end
                end
            elseif choice == "move" then
                if player.location == "Main Hall" then
                    print("Ok son, type door1, door2, or door3....If you fudge this up, I will hit you....in the face...")
                elseif player.location == "Door 1" then
                    print("Ok son, type mainhall...")
                elseif player.location == "Door 2" then
                    print("Ok son, type mainhall...")
                elseif player.location == "Door 3" then
                    print("Ok son, type mainhall...")
                end
            elseif choice == "mainhall" then
                player.location = "Main Hall"
            elseif choice == "door1" then
                player.location = "Door 1"
            elseif choice == "door2" then
                player.location = "Door 2"
            elseif choice == "door3" then
                player.location = "Door 3"
            elseif choice == "help" then
                print("To move type 'move'")
                print("To attack type 'attack'")
            end
            if player.hp == 0 then player.dead = true end
        else
            print("HAHAHA YOU THOUGHT THIS WAS A FULL GAME FULL OF AWESOME SHIT? YOU WERE WRONG! Anyhow.... You are dead!")
            print("THANKS FOR PLAYING! EMAIL j.horne2796@gmail.com AND TELL HIM HOW MUCH YOU FUCKING LOVED THIS GAME!")
            print("press something to continue...")
            io.read()
            game.running = false
        end

    end

end
