# Pharmacy Management System - Schema and Queries

## Conceptual Schema

### Drugs

- **Attributes:**
  - `name`: NOT NULL
  - `type`: NOT NULL
  - `barcode`: PRIMARY KEY
  - `dose`: NOT NULL
  - `code`: NOT NULL
  - `cost_price`: NOT NULL
  - `selling_price`: NOT NULL
  - `expiry`: NOT NULL
  - `company_name`: FOREIGN KEY references `company(name)`
  - `production_date`: NOT NULL
  - `expiration_date`: NOT NULL
  - `place`: NOT NULL
  - `quantity`: NOT NULL

### History Sales

- **Attributes:**
  - `user_name`: NOT NULL
  - `barcode`: FOREIGN KEY references `drugs(barcode)`
  - `name`: NOT NULL
  - `type`: NOT NULL
  - `dose`: NOT NULL
  - `quantity`: NOT NULL
  - `price`: NOT NULL
  - `amount`: NOT NULL
  - `date1`: NOT NULL
  - `time`: NOT NULL

### Purchase

- **Attributes:**
  - `barcode`: FOREIGN KEY references `drugs(barcode)`
  - `name`: NOT NULL
  - `type`: NOT NULL
  - `company_name`: FOREIGN KEY references `company(name)`
  - `quantity`: NOT NULL
  - `price`: NOT NULL
  - `amount`: NOT NULL

### Sales

- **Attributes:**
  - `barcode`: FOREIGN KEY references `drugs(barcode)`
  - `name`: NOT NULL
  - `type`: NOT NULL
  - `dose`: NOT NULL
  - `quantity`: NOT NULL
  - `price`: NOT NULL
  - `amount`: NOT NULL
  - `date2`: NOT NULL

### Company

- **Attributes:**
  - `name`: PRIMARY KEY
  - `address`: NOT NULL
  - `phone`: NOT NULL

## Relational Schema

### Company

```sql
CREATE TABLE company (
    name VARCHAR(50) PRIMARY KEY,
    address VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
```

### Drugs

```sql
CREATE TABLE drugs (
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL,
    barcode VARCHAR(20) PRIMARY KEY,
    dose VARCHAR(10) NOT NULL,
    code VARCHAR(10) NOT NULL,
    cost_price NUMBER NOT NULL,
    selling_price NUMBER NOT NULL,
    expiry VARCHAR(20) NOT NULL,
    company_name VARCHAR(50),
    FOREIGN KEY (company_name) REFERENCES company(name),
    production_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    place VARCHAR(20) NOT NULL,
    quantity NUMBER NOT NULL
);
```

### History Sales

```sql
CREATE TABLE history_sales (
    user_name VARCHAR(20) NOT NULL,
    barcode VARCHAR(20),
    FOREIGN KEY (barcode) REFERENCES drugs(barcode),
    name VARCHAR(50) NOT NULL,
    type VARCHAR(10) NOT NULL,
    dose VARCHAR(10) NOT NULL,
    quantity NUMBER NOT NULL,
    price NUMBER NOT NULL,
    amount NUMBER NOT NULL,
    date1 VARCHAR(15) NOT NULL,
    time VARCHAR(20) NOT NULL
);
```

### Purchase

```sql
CREATE TABLE purchase (
    barcode VARCHAR(20),
    FOREIGN KEY (barcode) REFERENCES drugs(barcode),
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL,
    company_name VARCHAR(20),
    FOREIGN KEY (company_name) REFERENCES company(name),
    quantity NUMBER NOT NULL,
    price NUMBER NOT NULL,
    amount NUMBER NOT NULL
);
```

### Sales

```sql
CREATE TABLE sales (
    barcode VARCHAR(20),
    FOREIGN KEY (barcode) REFERENCES drugs(barcode),
    name VARCHAR(50) NOT NULL,
    type VARCHAR(10) NOT NULL,
    dose VARCHAR(10) NOT NULL,
    quantity NUMBER NOT NULL,
    price NUMBER NOT NULL,
    amount NUMBER NOT NULL,
    date2 VARCHAR(15) NOT NULL
);
```

## Inserting Values

### Insert into Company Table

```sql
INSERT INTO company VALUES ('Cipla', 'Mumbai', '9039876542');
INSERT INTO company VALUES ('Sun Pharma', 'Mysore', '8907844302');
INSERT INTO company VALUES ('Med_City', 'Nellore', '7832010114');
INSERT INTO company VALUES ('Aurobindo Pharma', 'Bangalore', '7561234569');
INSERT INTO company VALUES ('DR.Reddy', 'Hyderabad', '8107844302');
```

### Insert into Drugs Table

```sql
INSERT INTO drugs VALUES('Novalo', 'Bills', 'sgnfsjkfnsdjfkb', 'normal', '3d00', 2, 3, 'Available for use', 'Med_City', '2023-03-03', '2019-03-03', 'N-Right', 40);
INSERT INTO drugs VALUES('Ace Proxyvon Tablet', 'Bills', 'nbhdl4978549', 'normal', '2xaa', 33, 40, 'Available for use', 'DR.Reddy', '2016-01-01', '2023-01-01', 'N-Left', 27);
INSERT INTO drugs VALUES('OXECAINE', 'Bills', 'fsdjkbdfjkffds', 'normal', '2xaa', 33, 40, 'Available for use', 'Sun Pharma', '2016-01-01', '2023-01-01', 'N-Left', 27);
INSERT INTO drugs VALUES('Zaleplon Caps 10 mg', 'Bills', 'AnyBarcodedaf', 'normal', '2xaa', 33, 40, 'Available for use', 'Aurobindo Pharma', '2016-01-01', '2023-01-01', 'N-Left', 27);
INSERT INTO drugs VALUES('Lamivudine Tabs 150 mg', 'Bills', 'ftrkl432432md', 'normal', '2xaa', 33, 40, 'Available for use', 'Cipla', '2016-01-01', '2023-01-01', 'N-Left', 27);
```

### Insert into History Sales Table

```sql
INSERT INTO history_sales VALUES('admin', 'sgnfsjkfnsdjfkb', 'Novalo', 'Bills', 'Free used', 2, 6, 12, '2023-02-12', '05:02:06');
INSERT INTO history_sales VALUES('admin', 'sgnfsjkfnsdjfkb', 'Novalo', 'Bills', 'Free used', 2, 6, 12, '2023-02-12', '05:02:26');
INSERT INTO history_sales VALUES('admin', 'sgnfsjkfnsdjfkb', 'Novalo', 'Bills', 'Free used', 4, 6, 24, '2023-02-12', '05:02:40');
INSERT INTO history_sales VALUES('admin', 'nbhdl4978549', 'Ace Proxyvon Tablet', 'Injection', '1 (Day)', 2, 14, 28, '2023-02-13', '05:03:07');
```

### Insert into Purchase Table

```sql
INSERT INTO purchase VALUES('sgnfsjkfnsdjfkb', 'Novalo', 'Bills', 'Med_City', 10, 6, 60);
INSERT INTO purchase VALUES('nbhdl4978549', 'Ace Proxyvon Tablet', 'Injection', 'DR.Reddy', 5, 14, 70);
```

### Insert into Sales Table

```sql
INSERT INTO sales VALUES('sgnfsjkfnsdjfkb', 'Novalo', 'Bills', 'Free used', 4, 6, 24, '2023-02-12');
INSERT INTO sales VALUES('nbhdl4978549', 'Ace Proxyvon Tablet', 'Injection', '1 (Day)', 2, 14, 28, '2023-02-13');
```

## Query Examples

### Retrieve Drug Information

```sql
SELECT * FROM drugs WHERE name = 'Novalo';
```

### Retrieve Purchase History for a Specific Drug

```sql
SELECT * FROM purchase WHERE barcode = 'sgnfsjkfnsdjfkb';
```

### Retrieve Sales History for a Specific Drug

```sql
SELECT * FROM sales WHERE barcode = 'sgnfsjkfnsdjfkb';
```

### Retrieve History Sales by User

```sql
SELECT * FROM history_sales WHERE user_name = 'admin';
```

### Retrieve Drugs by Company Name

```sql
SELECT * FROM drugs WHERE company_name = 'Cipla';
```
