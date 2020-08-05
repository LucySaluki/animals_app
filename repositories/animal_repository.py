from db.run_sql import run_sql as run_sql
from models.owner import Owner
import repositories.owner_repository as owner_repository
from models.animal import Animal


def save(animal):
    sql = "INSERT INTO animals (name, species, breed, age, picture, owner_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.species, animal.breed, animal.age, animal.picture, animal.owner.id]
    result = run_sql(sql, values)[0]
    id = result['id']
    animal.id = id
    return animal

def select_all():
    animals=[]
    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['name'], row['species'], row['breed'], row['age'], row['picture'], owner, row['id'])
        animals.append(animal)

    return animals

def select(id):
    animal=None
    sql = "SELECT * FROM animals WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        animal = Animal(result['name'], result['species'], result['breed'], result['age'], result['picture'], owner, id)
    
    return animal

def delete(id):
    sql = "DELETE FROM animals WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)
