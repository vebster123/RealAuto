CREATE DATABASE real_auto;

CREATE TABLE real_auto.car (
  id      SERIAL PRIMARY KEY,
  concern TEXT NOT NULL,
  model   TEXT NOT NULL
);

ALTER TABLE real_auto.car
MODIFY id BIGINT (20) NOT NULL AUTO_INCREMENT;

CREATE TABLE real_auto.type_part (
  id   SERIAL PRIMARY KEY,
  type TEXT NOT NULL,
  part TEXT NOT NULL
);

ALTER TABLE real_auto.type_part
MODIFY id BIGINT (20) NOT NULL AUTO_INCREMENT;

CREATE TABLE real_auto.part_advert (
  id           SERIAL PRIMARY KEY,
  car_id       BIGINT  NOT NULL,
  name         TEXT    NOT NULL,
  cost         INTEGER NOT NULL,
  type_part_id BIGINT  NOT NULL
);

ALTER TABLE real_auto.part_advert
MODIFY id BIGINT (20) NOT NULL AUTO_INCREMENT;

CREATE INDEX idx_partadvert__car_id ON real_auto.part_advert (car_id);

CREATE INDEX idx_partadvert__type_part_id ON real_auto.part_advert (type_part_id);

ALTER TABLE real_auto.part_advert
  ADD CONSTRAINT fk_part_advert_car_id FOREIGN KEY (car_id) REFERENCES real_auto.car (id);

ALTER TABLE real_auto.part_advert
  ADD CONSTRAINT fk_part_advert__type_part_id FOREIGN KEY (type_part_id) REFERENCES type_part (id);

CREATE TABLE real_auto.user (
  id       SERIAL PRIMARY KEY,
  login    TEXT NOT NULL,
  password TEXT NOT NULL,
  phone    INTEGER,
  name     TEXT,
  surname  TEXT
);

ALTER TABLE real_auto.user
MODIFY id BIGINT (20) NOT NULL AUTO_INCREMENT;

CREATE TABLE real_auto.car_advert (
  id      SERIAL PRIMARY KEY,
  user_id BIGINT  NOT NULL,
  car_id  BIGINT  NOT NULL,
  text    TEXT    NOT NULL,
  cost    INTEGER NOT NULL
);

ALTER TABLE real_auto.car_advert
MODIFY id BIGINT (20) NOT NULL AUTO_INCREMENT;

CREATE INDEX idx_caradvert__car_id ON real_auto.car_advert (car_id);

CREATE INDEX idx_caradvert__user_id ON real_auto.car_advert (user_id);

ALTER TABLE real_auto.car_advert
  ADD CONSTRAINT fk_caradvert__car_id FOREIGN KEY (car_id) REFERENCES car (id);

ALTER TABLE real_auto.car_advert
  ADD CONSTRAINT fk_caradvert__user_id FOREIGN KEY (user_id) REFERENCES user (id);

CREATE TABLE defect_car_advert (
  id            SERIAL PRIMARY KEY,
  car_advert_id BIGINT NOT NULL,
  type_part_id  BIGINT NOT NULL
);

CREATE INDEX idx_defectcaradvert__car_advert_id ON defect_car_advert (car_advert_id);

CREATE INDEX idx_defectcaradvert__type_part_id ON defect_car_advert (type_part_id);

ALTER TABLE defect_car_advert
  ADD CONSTRAINT fk_defectcaradvert__car_advert_id FOREIGN KEY (car_advert_id) REFERENCES real_auto.car_advert (id);

ALTER TABLE defect_car_advert
  ADD CONSTRAINT fk_defectcaradvert__type_part_id FOREIGN KEY (type_part_id) REFERENCES real_auto.type_part (id);

CREATE TABLE real_auto.picture (
  id            SERIAL PRIMARY KEY,
  link          TEXT   NOT NULL,
  car_advert_id BIGINT NOT NULL
);

CREATE INDEX idx_picture__car_advert_id ON real_auto.picture (car_advert_id);

ALTER TABLE real_auto.picture
  ADD CONSTRAINT fk_picture__car_advert_id FOREIGN KEY (car_advert_id) REFERENCES car_advert (id);
