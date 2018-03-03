import csv
from enum import Enum
from itertools import count

# UpdateDB.Location | Store location on initialize

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
		for profile in self.Dictionary:
			if profile.Password == password:
				setattr(profile, variable, value)	

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

class Profile():
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
tommyKey = database.New("Tommy", 7314)
johnnyKey = database.New("Johnny", 4979)
donnyKey = database.New("Donny", 1147)
tommyKey2 = database.New("Tommy 2", 7894)
johnnyKey3 = database.New("Johnny 2", 4649)
donnyKey4 = database.New("Donny 2", 1547)

database.Serialize()
database.Deserialize()



kyleProfile = Profile("Kyle", 4401)
kyleProfile.HomeValue = Preference.On
kyleProfile.CarValue = Preference.Fast
kyleProfile.HotelValue = Preference.Slow

jonahProfile = Profile("Jonah", 2018)
jonahProfile.HomeValue = Preference.Fast
jonahProfile.CarValue = Preference.Slow
jonahProfile.HotelValue = Preference.Off

mattProfile = Profile("Matt", 1234)
mattProfile.HomeValue = Preference.Slow
mattProfile.CarValue = Preference.Off
mattProfile.HotelValue = Preference.Fast

nathanProfile = Profile("Nathan", 8975)
nathanProfile.HomeValue = Preference.Slow
nathanProfile.CarValue = Preference.On
nathanProfile.HotelValue = Preference.Slow

