CREATE TABLE "car" (
  "id" SERIAL PRIMARY KEY,
  "concern" TEXT NOT NULL,
  "model" TEXT NOT NULL
);

CREATE TABLE "typepart" (
  "id" SERIAL PRIMARY KEY,
  "type" TEXT NOT NULL,
  "part" TEXT NOT NULL
);

CREATE TABLE "partadvert" (
  "id" SERIAL PRIMARY KEY,
  "car_id" INTEGER NOT NULL,
  "name" TEXT NOT NULL,
  "cost" INTEGER NOT NULL,
  "type_part_id" INTEGER NOT NULL
);

CREATE INDEX "idx_partadvert__car_id" ON "partadvert" ("car_id");

CREATE INDEX "idx_partadvert__type_part_id" ON "partadvert" ("type_part_id");

ALTER TABLE "partadvert" ADD CONSTRAINT "fk_partadvert__car_id" FOREIGN KEY ("car_id") REFERENCES "car" ("id");

ALTER TABLE "partadvert" ADD CONSTRAINT "fk_partadvert__type_part_id" FOREIGN KEY ("type_part_id") REFERENCES "typepart" ("id");

CREATE TABLE "user" (
  "id" SERIAL PRIMARY KEY,
  "login" TEXT NOT NULL,
  "password" TEXT NOT NULL,
  "phone" INTEGER NOT NULL,
  "name" TEXT NOT NULL,
  "surname" TEXT NOT NULL
);

CREATE TABLE "caradvert" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INTEGER NOT NULL,
  "car_id" INTEGER NOT NULL,
  "text" TEXT NOT NULL,
  "cost" INTEGER NOT NULL
);

CREATE INDEX "idx_caradvert__car_id" ON "caradvert" ("car_id");

CREATE INDEX "idx_caradvert__user_id" ON "caradvert" ("user_id");

ALTER TABLE "caradvert" ADD CONSTRAINT "fk_caradvert__car_id" FOREIGN KEY ("car_id") REFERENCES "car" ("id");

ALTER TABLE "caradvert" ADD CONSTRAINT "fk_caradvert__user_id" FOREIGN KEY ("user_id") REFERENCES "user" ("id");

CREATE TABLE "defectcaradvert" (
  "id" SERIAL PRIMARY KEY,
  "car_advert_id" INTEGER NOT NULL,
  "type_part_id" INTEGER NOT NULL
);

CREATE INDEX "idx_defectcaradvert__car_advert_id" ON "defectcaradvert" ("car_advert_id");

CREATE INDEX "idx_defectcaradvert__type_part_id" ON "defectcaradvert" ("type_part_id");

ALTER TABLE "defectcaradvert" ADD CONSTRAINT "fk_defectcaradvert__car_advert_id" FOREIGN KEY ("car_advert_id") REFERENCES "caradvert" ("id");

ALTER TABLE "defectcaradvert" ADD CONSTRAINT "fk_defectcaradvert__type_part_id" FOREIGN KEY ("type_part_id") REFERENCES "typepart" ("id");

CREATE TABLE "picture" (
  "id" SERIAL PRIMARY KEY,
  "link" TEXT NOT NULL,
  "car_advert_id" INTEGER NOT NULL
);

CREATE INDEX "idx_picture__car_advert_id" ON "picture" ("car_advert_id");

ALTER TABLE "picture" ADD CONSTRAINT "fk_picture__car_advert_id" FOREIGN KEY ("car_advert_id") REFERENCES "caradvert" ("id");
