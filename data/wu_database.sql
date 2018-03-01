CREATE TABLE "production" (
  "id_a" SERIAL CONSTRAINT "pk_production" PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "needablegood" (
  "id_n" SERIAL CONSTRAINT "pk_needablegood" PRIMARY KEY,
  "production" INTEGER NOT NULL
);

CREATE INDEX "idx_needablegood__production" ON "needablegood" ("production");

ALTER TABLE "needablegood" ADD CONSTRAINT "fk_needablegood__production" FOREIGN KEY ("production") REFERENCES "production" ("id_a");

CREATE TABLE "supplier" (
  "id_p" SERIAL CONSTRAINT "pk_supplier" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "phone" TEXT NOT NULL,
  "email" TEXT NOT NULL,
  "addres" TEXT NOT NULL
);

CREATE TABLE "criteria" (
  "id" SERIAL CONSTRAINT "pk_criteria" PRIMARY KEY,
  "supplier" INTEGER NOT NULL,
  "cost" DOUBLE PRECISION,
  "quality" DOUBLE PRECISION,
  "coincidence" DOUBLE PRECISION,
  "reliability" DOUBLE PRECISION,
  "delivery" DOUBLE PRECISION,
  "delivery_rapidity" DOUBLE PRECISION
);

CREATE INDEX "idx_criteria__supplier" ON "criteria" ("supplier");

ALTER TABLE "criteria" ADD CONSTRAINT "fk_criteria__supplier" FOREIGN KEY ("supplier") REFERENCES "supplier" ("id_p");

CREATE TABLE "rangeofgood" (
  "id" SERIAL CONSTRAINT "pk_rangeofgood" PRIMARY KEY,
  "supplier" INTEGER NOT NULL,
  "production" INTEGER NOT NULL,
  "cost" DOUBLE PRECISION,
  "time" TIME
);

CREATE INDEX "idx_rangeofgood__production" ON "rangeofgood" ("production");

CREATE INDEX "idx_rangeofgood__supplier" ON "rangeofgood" ("supplier");

ALTER TABLE "rangeofgood" ADD CONSTRAINT "fk_rangeofgood__production" FOREIGN KEY ("production") REFERENCES "production" ("id_a");

ALTER TABLE "rangeofgood" ADD CONSTRAINT "fk_rangeofgood__supplier" FOREIGN KEY ("supplier") REFERENCES "supplier" ("id_p");

CREATE TABLE "reliability" (
  "id" SERIAL CONSTRAINT "pk_reliability" PRIMARY KEY,
  "supplier" INTEGER NOT NULL,
  "completed_ord" INTEGER,
  "all_orders" INTEGER,
  "cust_rate" DOUBLE PRECISION
);

CREATE INDEX "idx_reliability__supplier" ON "reliability" ("supplier");

ALTER TABLE "reliability" ADD CONSTRAINT "fk_reliability__supplier" FOREIGN KEY ("supplier") REFERENCES "supplier" ("id_p");

INSERT INTO supplier VALUES
  (0, 'Мираторг', '89211241242', 'brom@gmail.com', 'ul Krasnaya'),
  (1, 'ПензКолбасы', '89211241241', 'penzcolb@gmail.com', 'ul Presnenskaya');

SELECT * FROM supplier
