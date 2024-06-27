-- CreateTable
CREATE TABLE "Character" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "range" TEXT NOT NULL,
    "base_atk" INTEGER NOT NULL,
    "base_def" INTEGER NOT NULL,
    "max_atk" INTEGER NOT NULL,
    "max_def" INTEGER NOT NULL,
    "acc" INTEGER NOT NULL,
    "eva" INTEGER NOT NULL,

    CONSTRAINT "Character_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Character_name_key" ON "Character"("name");
