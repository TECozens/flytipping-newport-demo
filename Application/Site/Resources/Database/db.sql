  CREATE TABLE `Reports` ( 
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tipLocation` TEXT NOT NULL,
    `locationDescription` TEXT NOT NULL,
    `wasteID` INTEGER NOT NULL,
    `wasteSize` TEXT NOT NULL,
    `pathID` TEXT NOT NULL )
