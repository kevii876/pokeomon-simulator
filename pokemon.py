import time # Gives us access to time-related functions

print("Professor Oak: Hello, welcome to the world of scuff python pokemon!")
print("Professor Oak: First off, what is your name?")

name = input("Enter your name: ")
print(f"Professor Oak: Hello, {name}! and welcome to the world of pokemon python")

print("Professor Oak: Next lets pick out your starter pokemon!")

starters = ["Charmander", "Bulbasaur", "Squirtle"]

print("Professor Oak: You have 30 seconds to choose!")

start_time = time.time() # Save the current time (in seconds) before asking the question

# The game pauses here and waits for the player to type something
pokemonStarter = input(
    "Select your starter:\nCharmander, Bulbasaur, Squirtle "
).capitalize()

# Save the current time again after the player presses Enter
end_time = time.time()

"""
debugging (test the time and see how much seconds past)
# Calculate how many seconds passed
time_taken = end_time - start_time

print(time_taken)
"""


if end_time - start_time > 30:
    print("Professor Oak: Oh no!")
    print("Professor Oak: You took too long!")
    print("Professor Oak: All the starter Pokémon have been taken!")
    
    pokemonStarter = "Pikachu"

    print("Professor Oak: Luckily, I still have a Pikachu.")
    print("Professor Oak: Take good care of it!")
    print(f"{pokemonStarter} joined your team!")

elif pokemonStarter in starters:
    print(f"Professor Oak: So you are picking {pokemonStarter}! I hope you two can get along and be the best of friends!")

    # Rival picks the stronger starter
    if pokemonStarter == "Charmander":
        rivalPokemon = "Squirtle"
    elif pokemonStarter == "Squirtle":
        rivalPokemon = "Bulbasaur"
    elif pokemonStarter == "Bulbasaur":
        rivalPokemon = "Charmander"
    else:
        rivalPokemon = "Eevee"
    print("Rival: Whats up loser! Im here to get my pokemon too!")
    print(f"Rival: Aah! I see you picking {pokemonStarter}, then i will just have to pick this guy.")
    print(f"Your rival chose {rivalPokemon}!")

else:
    print("That's not a choice, sorry!")