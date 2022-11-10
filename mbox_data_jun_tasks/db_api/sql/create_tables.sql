-- choosing database
\c prod_cat

-- creation of the products table
CREATE TABLE IF NOT EXISTS products(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- creation of the categories table
CREATE TABLE IF NOT EXISTS categories(
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- creation of the prodcategories table
CREATE TABLE IF NOT EXISTS prodcategories(
    product_id int REFERENCES products(id) NULL,
    category_id int REFERENCES categories(id) NULL,
    UNIQUE (product_id, category_id)
);

-- insertion data into products table
DO 
$$ BEGIN 
    IF (select count(*) from products) = 0 THEN
        COPY products FROM '/app/init_data/products.csv' 
        DELIMITER ',' CSV;
    END IF;
END $$;

-- insertion data into categories table
DO 
$$ BEGIN 
    IF (select count(*) from categories) = 0 THEN
        COPY categories FROM '/app/init_data/categories.csv' 
        DELIMITER ',' CSV;
    END IF;
END $$;

-- insertion data into prodcategories table
DO 
$$ BEGIN 
    IF (select count(*) from prodcategories) = 0 THEN
        COPY prodcategories FROM '/app/init_data/prodcategories.csv' 
        DELIMITER ',' CSV;
    END IF;
END $$;

