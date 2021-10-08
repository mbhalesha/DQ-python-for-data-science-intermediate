## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
        row[6] = date
        

## 2. Calculating Artist Ages ##

ages = []

for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)
        
final_ages = []

for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
        
    

# for row in moma:
#     date = row[6]
#     if date != "":
#         date = int(date)
#         row[6] = date

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades = []

for age in final_ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)
        

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}
for d in decades:
    if d not in decade_frequency:
        decade_frequency[d] = 1
    else:
        decade_frequency[d] += 1
    print(decade_frequency)
        



# for f in fruit:
#     if f not in fruit_frequency:
#         fruit_frequency[f] = 1
#     else:
#         fruit_frequency[f] += 1
#     print(fruit_frequency)

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

output = "{}'s birth year is {}".format(artist, birth_year)

# René Magritte's birth year is 1898

print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}

for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1
      
print(artist_freq)
    

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    num_artworks = artist_freq[artist]
    output = "There are {} artworks by {} in the data set.".format(num_artworks, artist)
    print(output)
    
# output = "{}'s birth year is {}".format(artist, birth_year)

print(artist_summary("Henri Matisse"))

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

# "The population of {:,.2f} is {} million.".format(pop_millions[0], pop_millions[1])

for country in pop_millions:
    name = country[0]
    population = country[1]
    output = "The population of {} is {:,.2f} million".format(name, population)
    print(output)

## 9. Challenge: Summarizing Artwork Gender Data ##

# for country in pop_millions:
#     name = country[0]
#     population = country[1]
#     output = "The population of {} is {:,.2f} million".format(name, population)
#     print(output)

# def artist_summary(artist):
#     num_artworks = artist_freq[artist]
#     output = "There are {} artworks by {} in the data set.".format(num_artworks, artist)
#     print(output)
    
# # output = "{}'s birth year is {}".format(artist, birth_year)

# print(artist_summary("Henri Matisse"))

# artist_freq = {}
# for row in moma:
#     artist = row[1]
#     if artist not in artist_freq:
#         artist_freq[artist] = 1
#     else:
#         artist_freq[artist] += 1
      
# print(artist_freq)

gender_freq = {}
for row in moma:
    g = row[5]
    if g not in gender_freq:
            gender_freq[g] = 1
    else:
            gender_freq[g] += 1

print(gender_freq)

for gender, num in gender_freq.items():
    output = "There are {n:,} artworks by {g} artists".format(n=num, g=gender)
    print(output)