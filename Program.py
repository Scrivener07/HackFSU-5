import csv
from enum import Enum
from itertools import count

class Database():
	Dictionary = {}
	FILENAME = "Database.csv"

	def __init__(self):
		self.defaultProfile = Profile("Dummy", 1000)
		self.Dictionary[self.defaultProfile.UID] = self.defaultProfile
	
	def Add(self, element):
		database.Dictionary[element.UID] = element

	def Serialize(self):
		with open(Database.FILENAME, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=Profile.Fields)
			writer.writeheader()

			for key, value in Database.Dictionary.items():
				print(str(key))
				print(str(value))

				writer.writerow(
					{
						'Name': value.Name,
						'Password': value.Password,
						'Location': value.Location,
						'HomeColor': value.HomeColor,
						'CarColor': value.CarColor,
						'HotelColor': value.HotelColor
					})

	def Deserialize(self):
		with open(Database.FILENAME, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['Name'], row['Password'], row['Location'], row['HomeColor'], row['CarColor'], row['HotelColor'])

class Profile():
	NextUID = count(-1)
	Fields = ['Name', 'Password', 'Location', 'HomeColor', 'CarColor', 'HotelColor']
	def __init__(self, name, password):
		self.UID = next(self.NextUID)
		self.Name = name
		self.Password = password
		self.Location = Location.Nill
		self.HomeColor = Color.Nill
		self.CarColor = Color.Nill
		self.HotelColor = Color.Nill

	def __str__(self):
		return self.Name + " UID:" + str(self.UID)

class Color(Enum):
	Nill = 0
	Red = 1
	Yellow = 2
	Blue = 3

class Location(Enum):
	Nill = 0
	Home = 1
	Car = 2
	Hotel = 3

#----------------------------------------------------------
#----------------------------------------------------------

database = Database()

kyleProfile = Profile("Kyle", 4401)
kyleProfile.HomeColor = Color.Yellow
kyleProfile.CarColor = Color.Yellow
kyleProfile.HotelColor = Color.Yellow

jonahProfile = Profile("Jonah", 2018)
jonahProfile.HomeColor = Color.Red
jonahProfile.CarColor = Color.Red
jonahProfile.HotelColor = Color.Red

mattProfile = Profile("Matt", 1234)
mattProfile.HomeColor = Color.Blue
mattProfile.CarColor = Color.Blue
mattProfile.HotelColor = Color.Blue

nathanProfile = Profile("Nathan", 8975)
nathanProfile.HomeColor = Color.Yellow
nathanProfile.CarColor = Color.Red
nathanProfile.HotelColor = Color.Blue

database.Add(kyleProfile)
database.Add(jonahProfile)
database.Add(mattProfile)
database.Add(nathanProfile)

database.Serialize()
database.Deserialize()
