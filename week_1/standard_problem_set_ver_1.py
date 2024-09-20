# Problem 1 Hundred Acre Wood
def welcome():
    return "Welcome to the Hundred Acre Wood!"

print(welcome())


def greetings(name):
    print("Hello " + name + "!")

greetings("Michael")
greetings("Winnie the Pooh")

def print_catchphrase(character):
    if character == "Pooh":
        return "Oh bother!"
    elif character == "Tigger":
        return "TTFN - Ta Ta For Now!"

    elif character == "Eeyore":
        return "Thanks for noticin' me."

    elif character == "Christopher Robin":
        return "Silly old bear."

    else:
        return "Catchphrase not found."
    return character + " says " + catchphrase

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print(print_catchphrase(character))


def sum_honey(hunny_jars):
    sum_honey = 0
    
    for i in range(hunny_jars):
        sum_honey += i
    return sum_honey

def sum_honey(hunny_jars):
    if isinstance(hunny_jars, list):
        hunny_jars = sum(hunny_jars)
    sum_honey = 0
    return [sum_honey + i for i in range(hunny_jars)]

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

def doubled(hunny_jars):
    def sum_honey(hunny_jars):
        if isinstance(hunny_jars, list):
            return [hunny_jars * 2 for i in range(hunny_jars)]

hunny_jars = [1, 2, 3]
doubled(hunny_jars)

def count_less_than(race_times, threshold):
    return len([i for i in race_times if i < threshold])

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)