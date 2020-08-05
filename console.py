import pdb

from models.owner import Owner
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

animal_repository.delete_all()
owner_repository.delete_all()

owner1 = Owner("Tim")
owner2 = Owner("Lucy")
owner_repository.save(owner1)
owner_repository.save(owner2)


animal1 = Animal("Rasputin","cat","Scottish Fold",owner1)
animal2 = Animal("Sputnik","cat","Ragdoll",owner1)

animal3 = Animal("Sonny","dog","Saluki Greyhound",owner2)
animal_repository.save(animal1)
animal_repository.save(animal2)
animal_repository.save(animal3)

pdb.set_trace()