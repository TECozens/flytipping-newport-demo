CREATE TABLE "Reports" ( 
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
