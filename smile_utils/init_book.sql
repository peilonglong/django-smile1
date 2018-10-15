BEGIN;
--
-- Create model Author
--
CREATE TABLE "books_author" (
  "id"         INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "first_name" VARCHAR(30)  NOT NULL,
  "last_name"  VARCHAR(40)  NOT NULL,
  "mobile"     VARCHAR(20)  NOT NULL,
  "email"      VARCHAR(254) NOT NULL
);
--
-- Create model Book
--
CREATE TABLE "books_book" (
  "id"               INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "book_no"          VARCHAR(200) NOT NULL,
  "title"            VARCHAR(200) NOT NULL,
  "publication_date" DATE         NOT NULL
);
CREATE TABLE "books_book_authors" (
  "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "book_id"   INTEGER NOT NULL REFERENCES "books_book" ("id"),
  "author_id" INTEGER NOT NULL REFERENCES "books_author" ("id")
);
--
-- Create model Borrower
--
CREATE TABLE "books_borrower" (
  "id"            INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "borrower_name" VARCHAR(40)  NOT NULL,
  "mobile"        VARCHAR(20)  NOT NULL,
  "email"         VARCHAR(254) NOT NULL,
  "create_date"   DATE         NOT NULL
);
--
-- Create model Publisher
--
CREATE TABLE "books_publisher" (
  "id"             INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name"           VARCHAR(50)  NOT NULL,
  "address"        VARCHAR(50)  NOT NULL,
  "city"           VARCHAR(70)  NOT NULL,
  "state_province" VARCHAR(80)  NOT NULL,
  "country"        VARCHAR(50)  NOT NULL,
  "website"        VARCHAR(200) NOT NULL
);
--
-- Create model Relation
--
CREATE TABLE "books_relation" (
  "id"               INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "book_no"          VARCHAR(200) NOT NULL,
  "start_date"       DATE         NOT NULL,
  "end_date"         DATE         NOT NULL,
  "book_name_id"     INTEGER      NOT NULL REFERENCES "books_book" ("id"),
  "borrower_name_id" INTEGER      NOT NULL REFERENCES "books_borrower" ("id")
);
--
-- Add field publisher to book
--
CREATE TABLE "books_book" (
  "id"               INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
  "book_no"          VARCHAR(200) NOT NULL,
  "title"            VARCHAR(200) NOT NULL,
  "publication_date" DATE         NOT NULL,
  "publisher_id"     INTEGER      NOT NULL REFERENCES "books_publisher" ("id")
);
INSERT INTO "books_book" ("book_no", "publication_date", "publisher_id", "id", "title") SELECT
                                                                                          "book_no",
                                                                                          "publication_date",
                                                                                          NULL,
                                                                                          "id",
                                                                                          "title"
                                                                                        FROM "books_book";
CREATE INDEX "books_relation_534109ae"  ON "books_relation" ("book_name_id");
CREATE INDEX "books_relation_cdd793f5"  ON "books_relation" ("borrower_name_id");
CREATE INDEX "books_book_2604cbea"  ON "books_book" ("publisher_id");
COMMIT;
