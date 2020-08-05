from db.run_sql import run_sql as run_sql
from models.owner import Owner
from models.animal import Animal

def save(owner):
    sql = "INSERT INTO owners (name) VALUES (%s) RETURNING *"
    values = [owner.name]
    result = run_sql(sql, values)[0]
    id = result['id']
    owner.id = id
    return owner

def select_all():
    owners=[]
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'], row['id'])
        owners.append(owner)

    return owners

def select(id):
    owner=None
    sql = "SELECT * FROM owners WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        owner = Owner(result['name'], id)
    
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)