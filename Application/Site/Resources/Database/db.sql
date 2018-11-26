CREATE TABLE `Reports` (
  `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `tipLocation` TEXT NOT NULL,
  `locationDescription` TEXT NOT NULL,
  `wasteID` INTEGER NOT NULL,
  `wasteSizeID` INTEGER NOT NULL,
  `wasteDescription` TEXT NOT NULL,
  `imageID` TEXT NOT NULL,
  `witness` TEXT NOT NULL,
  `witnessID` INTEGER NOT NULL,
  `emailaddress` TEXT NOT NULL )

CREATE TABLE `Image` (
  `imageID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `imagePath1` TEXT,
  `imagePath2` TEXT,
  `imagePath3` TEXT,
  `imagePath4` TEXT )

CREATE TABLE `Waste` (
  `wasteID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `waste` TEXT NOT NULL )

CREATE TABLE `Waste Size` (
  `wasteSizeID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `size` TEXT NOT NULL )

CREATE TABLE `Witness` (
  `witnessID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `surname` TEXT NOT NULL,
  `contactNumber` INTEGER NOT NULL )
