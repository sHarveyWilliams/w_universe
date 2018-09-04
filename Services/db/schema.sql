CREATE TABLE "needablegoods" (id INTEGER CONSTRAINT "pk_needablegoods" PRIMARY KEY AUTOINCREMENT, "production_id" INTEGER NOT NULL REFERENCES "production" (id));
CREATE TABLE "rangeofgoods" (id INTEGER CONSTRAINT "pk_rangeofgoods" PRIMARY KEY AUTOINCREMENT, "name" TEXT NOT NULL);
CREATE TABLE "production" ("id" INTEGER CONSTRAINT "pk_production" PRIMARY KEY AUTOINCREMENT, "cost" REAL, "speed" REAL, "supplier_id" INTEGER NOT NULL REFERENCES "suppliers" (id), "production_id" INTEGER NOT NULL REFERENCES "rangeofgoods" (id));
CREATE TABLE "ratings" ("id" INTEGER CONSTRAINT "pk_rating" PRIMARY KEY AUTOINCREMENT, "supplier_id" INTEGER NOT NULL REFERENCES "suppliers" (id), "quality" REAL, "completed_orders_count" INTEGER, "all_orders_count" INTEGER, "customers_rating" REAL);
CREATE TABLE "suppliers" (id INTEGER CONSTRAINT "pk_suppliers" PRIMARY KEY AUTOINCREMENT, "name" TEXT NOT NULL, "phone" TEXT NOT NULL, "email" TEXT NOT NULL, "address" TEXT NOT NULL);
CREATE INDEX "idx_needablegoods__production" ON "needablegoods" ("production");
CREATE INDEX "idx_production__rangeofgoods" ON "production" ("rangeofgoods");
CREATE INDEX "idx_production__suppliers" ON "production" ("suppliers");
CREATE INDEX "idx_ratings__suppliers" ON "ratings" ("suppliers");
