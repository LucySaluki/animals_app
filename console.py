import pdb

from models.owner import Owner
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

animal_repository.delete_all()
owner_repository.delete_all()

owner1 = Owner("Tim","Sanders")
owner2 = Owner("Lucy","Arnold")
owner_repository.save(owner1)
owner_repository.save(owner2)


animal1 = Animal("Rasputin","Cat","Scottish Fold", 4 , "Rasputin.jpg", owner1)
animal2 = Animal("Sputnik","Cat","Ragdoll", 5 , "Sputnik.jpg", owner1)

animal3 = Animal("Sonny","Dog","Saluki Greyhound",9, "Sonny.jpg", owner2)
animal_repository.save(animal1)
animal_repository.save(animal2)
animal_repository.save(animal3)

pdb.set_trace()