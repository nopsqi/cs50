-- Insert manufacturers
INSERT INTO manufacturers (name) VALUES 
('Manufacturer A'), 
('Manufacturer B'), 
('Manufacturer C'), 
('Manufacturer D'), 
('Manufacturer E');

-- Insert models for notebooks
INSERT INTO models (manufacturer_id, name) VALUES 
(1, 'Notebook Model A1'), 
(2, 'Notebook Model B1'), 
(3, 'Notebook Model C1'), 
(4, 'Notebook Model D1'), 
(5, 'Notebook Model E1'),
(1, 'CPU Model 1'), 
(4, 'CPU Model 2'), 
(2, 'Memory Model 1'), 
(5, 'Memory Model 2'),
(3, 'Storage Model 1'); 

-- Insert notebooks
INSERT INTO notebooks (name, model_id, year, price) VALUES 
('Notebook 1', 1, '2022-01-01', 1000.00), 
('Notebook 2', 1, '2022-01-01', 1100.00),
('Notebook 3', 2, '2022-01-01', 1200.00),
('Notebook 4', 2, '2022-01-01', 1300.00),
('Notebook 5', 3, '2022-01-01', 1400.00),
('Notebook 6', 3, '2022-01-01', 1500.00),
('Notebook 7', 4, '2022-01-01', 1600.00),
('Notebook 8', 4, '2022-01-01', 1700.00),
('Notebook 9', 5, '2022-01-01', 1800.00),
('Notebook 10', 5, '2022-01-01', 1900.00),
('Notebook 11', 1, '2022-01-01', 2000.00),
('Notebook 12', 2, '2022-01-01', 2100.00),
('Notebook 13', 3, '2022-01-01', 2200.00);

-- Insert components
INSERT INTO components (model_id, name, type) VALUES 
(6, 'CPU 1', 'cpu'), 
(6, 'CPU 2', 'cpu'), 
(7, 'CPU 3', 'cpu'), 
(8, 'Memory 1', 'memory'), 
(8, 'Memory 2', 'memory'), 
(9, 'Memory 3', 'memory'), 
(10, 'Storage 1', 'storage'), 
(10, 'Storage 2', 'storage'), 
(10, 'Storage 3', 'storage');

-- Insert CPUs
INSERT INTO cpus (component_id, cores, threads, frequency) VALUES 
(1, 4, 8, 3.5), 
(2, 6, 12, 3.7), 
(3, 8, 16, 3.9);

-- Insert memories
INSERT INTO memories (component_id, type, size, clock) VALUES 
(4, 'ddr4', 8, 2400), 
(5, 'ddr4', 16, 2600), 
(6, 'ddr5', 32, 3200);

-- Insert storages
INSERT INTO storages (component_id, type, size, write_speed, read_speed) VALUES 
(7, 'ssd', 512, 2000, 3000), 
(8, 'ssd', 1024, 2500, 3500), 
(9, 'hdd', 2048, 150, 200);

-- Insert contains (notebooks to components relationships)
INSERT INTO contains (notebook_id, component_id) VALUES 
(1, 1), (1, 4), (1, 5), (1, 7), 
(2, 1), (2, 4), (2, 8), 
(3, 2), (3, 5), (3, 7), 
(4, 2), (4, 5), (4, 6), (4, 9), 
(5, 3), (5, 6), (5, 7), 
(6, 3), (6, 6), (6, 8), (6, 9), 
(7, 1), (7, 4), (7, 7), (7, 9), 
(8, 2), (8, 5), (8, 7), 
(9, 3), (9, 4), (9, 6), (9, 8), 
(10, 1), (10, 4), (10, 7), 
(11, 2), (11, 5), (11, 8), 
(12, 3), (12, 6), (12, 9), 
(13, 1), (13, 4), (13, 7), (13, 9);

