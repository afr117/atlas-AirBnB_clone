# atlas-AirBnB_clone
AirBnB Clone - The Console
This repository contains the command interpreter for a clone of the AirBnB website. The console manages the serialization and deserialization of various classes and allows users to create, show, destroy, and update instances.

Table of Contents
Installation
Usage
Files
Classes
BaseModel
User
State
City
Amenity
Place
Review
Command Interpreter
Testing
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/atlas-AirBnB_clone.git
cd atlas-AirBnB_clone
Usage
To start the command interpreter, run:

bash
Copy code
./console.py
Files
Python Files
console.py: The command interpreter for managing objects.
models/: Directory containing the class definitions and the storage engine.
base_model.py: Defines the BaseModel class.
user.py: Defines the User class.
state.py: Defines the State class.
city.py: Defines the City class.
amenity.py: Defines the Amenity class.
place.py: Defines the Place class.
review.py: Defines the Review class.
engine/: Directory containing the storage engine.
file_storage.py: Defines the FileStorage class.
Classes
BaseModel
models/base_model.py:

Attributes:
id: A unique identifier for each instance.
created_at: The datetime when the instance was created.
updated_at: The datetime when the instance was last updated.
Methods:
save(): Updates updated_at and saves the instance to storage.
to_dict(): Returns a dictionary representation of the instance.
__str__(): Returns the string representation of the instance.

User
models/user.py:

Inherits from BaseModel.
Attributes:
email: User's email.
password: User's password.
first_name: User's first name.
last_name: User's last name.
State
models/state.py:

Inherits from BaseModel.
Attributes:
name: The name of the state.
City
models/city.py:

Inherits from BaseModel.
Attributes:
state_id: The State.id of the state to which the city belongs.
name: The name of the city.
Amenity
models/amenity.py:

Inherits from BaseModel.
Attributes:
name: The name of the amenity.
Place
models/place.py:

Inherits from BaseModel.
Attributes:
city_id: The City.id of the city to which the place belongs.
user_id: The User.id of the user who owns the place.
name: The name of the place.
description: Description of the place.
number_rooms: Number of rooms in the place.
number_bathrooms: Number of bathrooms in the place.
max_guest: Maximum number of guests.
price_by_night: Price per night to stay at the place.
latitude: Latitude of the place.
longitude: Longitude of the place.
amenity_ids: List of Amenity.id of amenities available at the place.
Review
models/review.py:

Inherits from BaseModel.
Attributes:
place_id: The Place.id of the place being reviewed.
user_id: The User.id of the user who wrote the review.
text: The text of the review.
Command Interpreter
The command interpreter allows the following commands:

create <class>: Creates a new instance of a class and prints its id.
show <class> <id>: Prints the string representation of an instance.
destroy <class> <id>: Deletes an instance.
all [class]: Prints all instances, or all instances of a specific class.
update <class> <id> <attribute name> <attribute value>: Updates an instance by adding or updating an attribute.
Example Usage
bash
Copy code
(hbnb) create User
(hbnb) show User <id>
(hbnb) destroy User <id>
(hbnb) all User
(hbnb) update User <id> email "example@example.com"
Testing
The tests folder contains the unit tests for the models.

Run the tests using:

bash
Copy code
python3 -m unittest discover tests
Code Style
All Python files are checked with pycodestyle for compliance. To check your files, run:

bash
Copy code
pycodestyle <filename>

Author
Alfredo Figueroa
