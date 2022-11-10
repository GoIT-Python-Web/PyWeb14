# Створення таблиць

Для демонстрації використовуємо SQLite базу даних. Виконуємо оператори пояснюючи кожен рядок.

```sqlite
CREATE TABLE IF NOT EXISTS genders (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(30),
    createAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(30),
    email VARCHAR(30),
    password VARCHAR(30),
    age TINYINT UNSIGNED,
    gender_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (gender_id) REFERENCES genders (id)
          ON DELETE SET NULL
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(30),
    email VARCHAR(30),
    phone VARCHAR(30),
    favorite BOOLEAN,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);
```



# Додаємо дані до бази даних

```sql
INSERT INTO users (id, name, email, password, age, gender_id)
VALUES (1, 'Boris', 'boris@test.com', 'password', 23, 1),
(2, 'Alina', 'alina@test.com', 'password', 32, 2),
(3, 'Maksim', 'maksim@test.com', 'password', 40, 1);


INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);
```

# Запити

Знайти перші 100 контактів, які не є вибраними

```sql
SELECT id, name as fullname 
FROM contacts
WHERE favorite <> TRUE 
ORDER BY fullname ASC
LIMIT 100;
```

Знайти всіх користувачів вік яких дорівнює 20, 30 або 40 років

```sql
SELECT name, email
FROM users
WHERE age IN(20, 30, 40)
ORDER BY name;
```

Знайти всіх користувачів вік яких в межах від 20 до 32 років

```sql
SELECT name, email
FROM users
WHERE age BETWEEN 20 AND 32
ORDER BY name;
```

Знайти всі контакти, які в полі `name` мають букву `l`

```sql
SELECT name, email
FROM contacts
WHERE name LIKE '%L%'
ORDER BY name;
```

Знайти всіх користувачів вік яких знаходиться в межах до 30 та понад 40 років

```sql
SELECT name, email, age
FROM users
WHERE age NOT BETWEEN 30 AND 40
ORDER BY name;
```

Знайти загальну кількість контактів для кожного користувача

```sql
SELECT COUNT(user_id) as total_contacts, user_id
FROM contacts
GROUP BY user_id;
```

Знайти всіх користувачів вік яких менш як 35 років

```sql
SELECT id, name
FROM users
WHERE age < 35;
```

Використаємо попередній запит, щоб знайти всі контакті для таких користувачів

```sql
SELECT *
FROM contacts
WHERE user_id IN (SELECT id
    FROM users
    WHERE age < 35);
```
    
Знайти всі контакти, але через `JOIN` добавити стовпчик з іменем користувача, якому належить контакт

```sql
SELECT c.id, c.name, c.email, u.name owner
FROM contacts c
INNER JOIN users u ON u.id = c.user_id;
```

Знайти всі контакти навіть ті які без поля користувача. Ти видна різниця між `INNER JOIN` та `LEFT JOIN`

```sql
SELECT c.id, c.name, c.email, u.name owner
FROM contacts c
LEFT JOIN users u ON u.id = c.user_id;
```

Додати безхозному контакту користувача

```sql
UPDATE contacts SET user_id = 3 WHERE id = 5;
```

Зробити повторний запит, щоб побачити зміни

```sql
SELECT c.id, c.name, c.email, u.name owner
FROM users u
LEFT JOIN contacts c ON u.id = c.user_id;
```

Далі в залежності від запитань. Зв'язок багато до багатьох на наступному занятті.
