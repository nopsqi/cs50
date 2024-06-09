-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it
CREATE DATABASE project;

-- \c project
-- table contains manufacturers that produce notebooks and/or components
CREATE TABLE
manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(32) NOT NULL UNIQUE
);

-- table contains models that manufacturers create for notebooks or components
CREATE TABLE
  models (
    id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES manufacturers (id),
    name VARCHAR(32) NOT NULL
  );

-- table contains notebooks that manufacturers produce
CREATE TABLE
  notebooks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    model_id INT REFERENCES models (id),
    year DATE NOT NULL,
    price DECIMAL(6, 2) NOT NULL
  );

-- table contains components that manufacturers produce
CREATE TYPE component_types AS ENUM ('cpu', 'memory', 'storage');
CREATE TABLE
  components (
    id SERIAL PRIMARY KEY,
    model_id INT REFERENCES models (id),
    name VARCHAR(32) NOT NULL,
    type component_types NOT NULL
  );

-- table contains cpus components
CREATE TABLE
  cpus (
    component_id INT REFERENCES components (id),
    cores SMALLINT NOT NULL,
    threads SMALLINT NOT NULL,
    frequency DECIMAL(2, 1) NOT NULL
  );

-- table contains memories components
CREATE TYPE memory_types AS ENUM ('ddr3', 'ddr4', 'ddr5');
CREATE TABLE
  memories (
    component_id INT REFERENCES components (id),
    type memory_types NOT NULL,
    size INT NOT NULL,
    clock SMALLINT NOT NULL
  );

-- table contains storages components
CREATE TYPE storage_types AS ENUM ('hdd', 'ssd');
CREATE TABLE
  storages (
    component_id INT REFERENCES components (id),
    type storage_types NOT NULL,
    size SMALLINT NOT NULL,
    write_speed SMALLINT NOT NULL,
    read_speed SMALLINT NOT NULL
  );

-- table that contains the relation between notebook and components
CREATE TABLE
  contains (
    notebook_id INT REFERENCES notebooks (id),
    component_id INT REFERENCES components (id)
  );

CREATE INDEX search_by_manufacturers ON manufacturers (name);
CREATE INDEX search_by_notebooks ON notebooks (name, year);
CREATE INDEX search_by_cpus ON cpus (cores, threads, frequency);
CREATE INDEX search_by_memories ON memories (type, size, clock);
CREATE INDEX search_by_storages ON storages (type, size, write_speed, read_speed);

CREATE VIEW
  list_all AS
SELECT
  n.id AS notebook_id, n.name AS notebook_name, md1.name AS notebook_model, n.year AS notebook_year_release, n.price AS notebook_price,
  mn1.name AS notebook_manufacturer,
  cm.name AS component_name, cm.type AS component_type, mn2.name AS component_manufacturer,
  cpu.cores, cpu.threads, cpu.frequency,
  mem.type AS memory_type, mem.size AS memory_size, mem.clock,
  sr.type AS storage_type, sr.size AS storage_size, sr.read_speed, sr.write_speed
FROM
  notebooks n
  INNER JOIN models md1 ON md1.id = n.model_id
  INNER JOIN manufacturers mn1 ON mn1.id = md1.manufacturer_id
  INNER JOIN contains c ON c.notebook_id = n.id
  INNER JOIN components cm ON cm.id = c.component_id
  INNER JOIN models md2 ON md2.id = cm.model_id
  INNER JOIN manufacturers mn2 ON mn2.id = md2.manufacturer_id
  LEFT OUTER JOIN cpus cpu ON cpu.component_id = cm.id
  LEFT OUTER JOIN memories mem ON mem.component_id = cm.id
  LEFT OUTER JOIN storages sr ON sr.component_id = cm.id;
