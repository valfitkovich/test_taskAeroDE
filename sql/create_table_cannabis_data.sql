CREATE TABLE cannabis_data (
    id INT PRIMARY KEY,
    uid UUID NOT NULL,
    strain VARCHAR(255),
    cannabinoid_abbreviation VARCHAR(50),
    cannabinoid VARCHAR(255),
    terpene VARCHAR(255),
    medical_use VARCHAR(255),
    health_benefit TEXT,
    category VARCHAR(255),
    type VARCHAR(50),
    brand VARCHAR(255)
);
