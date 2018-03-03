import csv
from enum import Enum
from itertools import count

# The context of the application contains the database.
class Application():
	Database = {}

	def __init__(self):
		self.defaultProfile = Profile("Dummy", 1000)
		self.Database[self.defaultProfile.UID] = self.defaultProfile

	def Add(self, element):
		application.Database[element.UID] = element

	def Serialize(self):
		with open('Database.csv', 'w') as csvfile:
			dbWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

			for key, value in Application.Database.items():	
				print(str(value))
				dbWriter.writerow(
					[
						key,
						value.Name,
						value.Password,
						value.Location,
						value.HomeColor,
						value.CarColor,
						value.HotelColor
					])

	def Deserialize(self):
		with open('Database.csv', newline='') as csvfile:
			dbReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in dbReader:
				print(', '.join(row))

# Database object for storing profile information.
class Profile():
	NextUID = count(-1)
	
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

application = Application()

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

application.Add(kyleProfile)
application.Add(jonahProfile)
application.Add(mattProfile)
application.Add(nathanProfile)

application.Serialize()
application.Deserialize()
