# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', \n
         'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew',\n
         'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', \n
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', \n
          'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', \n
          'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, \n
         1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, \n
                       185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], \n
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], \n
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], \n
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], \n
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], \n
                  ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], \n
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], \n
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], \n
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], \n
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], \n
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], \n
                  ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], \n
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], \n
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], \n
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], \n
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', \n
           '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', \n
           '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

updated_damages = []
for damage in damages:
  if damage[-1] == 'B':
    updated_damages.append(float(damage[0:-1]) * float(10 ** 9))
  elif damage == 'Damages not recorded':
    updated_damages.append('Damages not recorded')
  else:
    updated_damages.append(float(damage[0:-1]) * float(10 ** 6))

info_names = {}
for i in range(len(names)):
  info_names.update({names[i - 1]: {"Name": names[i - 1], "Month": months[i - 1], "Year": years[i - 1], "Max Sustained Wind": max_sustained_winds[i - 1], \n
                                    "Areas Affected": areas_affected[i - 1], "Damage": damages[i - 1], "Deaths": deaths[i - 1]}})

info_years = {}
for i in range(len(names)):
  info_years.update({years[i - 1]: {"Name": names[i - 1], "Month": months[i - 1], "Year": years[i - 1], "Max Sustained Wind": max_sustained_winds[i - 1], \n
                                    "Areas Affected": areas_affected[i - 1], "Damage": damages[i - 1], "Deaths": deaths[i - 1]}})

areas = {}
for locations in areas_affected:
  for location in locations:
    if location not in areas.keys():
      areas[location] = 1
    else:
      areas[location] += 1

areas_list = list(areas.items())
highest_location = 0
affected_location = ""
for couple in areas_list:
  if couple[1] > highest_location:
    highest_location = couple[1]
    affected_location = couple[0]
print("The most affected area across all cat 5 hurricanes is " + affected_location + " with " + str(highest_location) + " times hit.")

deaths_names_combo = list(zip(deaths, names))
highest_death = 0
highest_death_name = ""
for combo in deaths_names_combo:
  if combo[0] > highest_death:
    highest_death = combo[0]
    highest_death_name = combo[1]
print("The deadliest hurricane was {} with {} deaths.".format(highest_death_name, highest_death))

mortality_rating = {}
for combo in deaths_names_combo:
  if combo[0] == 0:
    mortality_rating.update({combo[1]: 0})
  elif combo[0] > 0 and combo[0] <= 100:
    mortality_rating.update({combo[1]: 1})
  elif combo[0] > 100 and combo[0] <= 500:
    mortality_rating.update({combo[1]: 2})
  elif combo[0] > 500 and combo[0] <= 1000:
    mortality_rating.update({combo[1]: 3})
  elif combo[0] > 1000 and combo[0] <= 10000:
    mortality_rating.update({combo[1]: 4})
  else:
    mortality_rating.update({combo[1]: 5})

print(updated_damages)
highest_damage_name = ""
highest_damage = 0
for i in range(len(updated_damages)):
  if updated_damages[i] == "Damages not recorded":
    continue
  else:
    if updated_damages[i] > highest_damage:
      highest_damage = updated_damages[i]
      highest_damage_name = names[i]
print("Hurricane {} costed the most damage, coming in at {} USD.".format(highest_damage_name, highest_damage))

damage_rating = {"Damage not recorded": [], 0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
for i in range(len(updated_damages)):
  if updated_damages[i] == "Damages not recorded":
    damage_rating["Damage not recorded"].append(names[i])
  elif updated_damages[i] == 0:
    damage_rating[0].append(names[i])
  elif updated_damages[i] > 0 and updated_damages[i] <= 100000000:
    damage_rating[1].append(names[i])
  elif updated_damages[i] > 100000000 and updated_damages[i] <= 1000000000:
    damage_rating[2].append(names[i])
  elif updated_damages[i] > 1000000000 and updated_damages[i] <= 10000000000:
    damage_rating[3].append(names[i])
  elif updated_damages[i] > 10000000000 and updated_damages[i] <= 50000000000:
    damage_rating[4].append(names[i])
  else:
    damage_rating[5].append(names[i])

print(damage_rating) 
