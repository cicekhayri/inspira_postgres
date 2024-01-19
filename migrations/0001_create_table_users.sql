
CREATE TABLE users (
	id SERIAL NOT NULL, 
	name VARCHAR(50), 
	email VARCHAR(120), 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
