  -- CREATING ADMIN USER
DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

  -- CREATING TABLES
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

CREATE TABLE store (
    store_id    INT           NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)  NOT NULL,
    PRIMARY KEY(store_id)
);
CREATE TABLE book (
    book_id    INT            NOT NULL    AUTO_INCREMENT,
    book_name  VARCHAR(200)   NOT NULL,
    details    VARCHAR(500)   NULL,
    author     VARCHAR(200)   NOT NULL,
    PRIMARY KEY(book_id)
);
CREATE TABLE user (
    user_id     INT           NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)   NOT NULL,
    last_name   VARCHAR(75)   NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE wishlist (
    wishlist_id INT           NOT NULL    AUTO_INCREMENT,
    user_id     INT           NOT NULL,
    book_id     INT           NOT NULL,
    PRIMARY KEY(wishlist_id),
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);


  -- FILLING TABLES WITH 1 STORE, 9 BOOKS, 3 USERS (1 WISHLIST BOOK EACH)
INSERT INTO store(locale)
    VALUES('2604 Georgia Ave, Bellevue, NE 68147');

INSERT INTO book(book_name, author)
    VALUES('The Pilgrims Progress', 'John Bunyan');
INSERT INTO book(book_name, author)
    VALUES('The Count of Monte Cristo', 'Alexandre Dumas');
INSERT INTO book(book_name, author)
    VALUES('Three Men in a Boat', 'Jerome K. Jerome');
INSERT INTO book(book_name, author)
    VALUES('Oliver Twist', 'Charles Dickens');
INSERT INTO book(book_name, author)
    VALUES('Moby Dick', 'Herman Melville');
INSERT INTO book(book_name, author)
    VALUES('A Christmas Carol', 'Charles Dickens');
INSERT INTO book(book_name, author)
    VALUES('The Adventures of Tom Sawyer', 'Mark Twain');
INSERT INTO book(book_name, author)
    VALUES('Little Men', 'Louisa May Alcott');
INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO user(first_name, last_name) 
    VALUES('James', 'Jones');
INSERT INTO user(first_name, last_name)
    VALUES('John', 'Johnson');
INSERT INTO user(first_name, last_name)
    VALUES('Will', 'Williams');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'James'), 
        (SELECT book_id FROM book WHERE book_name = 'Moby Dick')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Three Men in a Boat')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Will'),
        (SELECT book_id FROM book WHERE book_name = 'Little Men')
    );
    