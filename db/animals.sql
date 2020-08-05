DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  surname VARCHAR(255)
);

CREATE TABLE animals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  species VARCHAR(255),
  breed VARCHAR(255),
  age INT,
  picture VARCHAR(255),
  owner_id INT REFERENCES owners(id)
);