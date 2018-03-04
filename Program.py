import csv
from enum import Enum
from itertools import count

class Database():
	Dictionary = {}
	FILENAME = "Database.csv"

	def __init__(self):
		self.defaultProfile = Profile("Dummy", 0000)
		self.Dictionary[self.defaultProfile.UID] = self.defaultProfile
	
	def New(self, name, password):
		profile = Profile(name, password)
		self.Dictionary[profile.UID] = profile
		return profile.UID

	def SetProperty(self, password, variable, value):
		for profile in self.Dictionary.items():
			if profile[1].Password == password:
				setattr(profile[1], variable, value)	

	def Serialize(self):
		with open(self.FILENAME, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=Profile.Fields)
			writer.writeheader()

			for key, value in self.Dictionary.items():
				print(str(key))
				print(str(value))
				writer.writerow(
					{
						'UID': value.UID,
						'Name': value.Name,
						'Password': value.Password,
						'Location': value.Location,
						'HomeValue': value.HomeValue,
						'CarValue': value.CarValue,
						'HotelValue': value.HotelValue
					})

	def Deserialize(self):
		with open(self.FILENAME, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['Name'], row['Password'], row['Location'], row['HomeValue'], row['CarValue'], row['HotelValue'])

class Profile(Database):
	NextUID = count(-1)
	Fields = ['UID', 'Name', 'Password', 'Location', 'HomeValue', 'CarValue', 'HotelValue']
	def __init__(self, name, password):
		self.UID = next(self.NextUID)
		self.Name = name
		self.Password = password
		self.Location = Location.Unknown
		self.HomeValue = Preference.Unknown
		self.CarValue = Preference.Unknown
		self.HotelValue = Preference.Unknown

	def __str__(self):
		return self.Name + " UID:" + str(self.UID)

class Preference(Enum):
	Unknown = -1
	Off = 0
	On = 1
	Slow = 2
	Fast = 3

class Location(Enum):
	Unknown = -1
	Home = 0
	Car = 1
	Hotel = 2


#----------------------------------------------------------
#----------------------------------------------------------

database = Database()

database.Deserialize() # read in existing database

database.New("Tommy", 7314)
database.New("Johnny", 4979)
database.New("Donny", 1147)
database.New("Mike", 7894)
database.New("Taylor", 4649)
database.New("Sammy", 1547)
database.New("Kyle", 4401)
database.New("Jonah", 2018)
database.New("Matt", 1234)
database.New("Nathan", 8975)
database.New("Max", 8875)

database.SetProperty(4401, "HomeValue", Preference.Fast) # Set the property of a profile.
database.SetProperty(8975, "CarValue", Preference.Fast) # duplicates passwords?

database.Serialize()
database.Deserialize()
