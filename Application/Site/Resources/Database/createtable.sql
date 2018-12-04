CREATE TABLE `Reports` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tipLocation`	TEXT NOT NULL,
	`locationDescription`	TEXT ,
	`wastetypeID`	TEXT,
	`wasteSize`	TEXT,
	`wasteDescription`	TEXT,
	`imageID`	INTEGER ,
	`witness`	TEXT,
	`firstname`	TEXT,
	`surname`	TEXT,
	`contactnumber`	TEXT,
	`emailaddress`	TEXT
);
CREATE TABLE `Image` (
	`imageID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`imagePath1`	TEXT,
	`imagePath2`	TEXT,
	`imagePath3`	TEXT,
	`imagePath4`	TEXT
);
CREATE TABLE `wastetypeID` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`blackbags-househould`	TEXT,
	`whiteGoods`	TEXT,
	`furniture`	TEXT,
	`mattress`	TEXT,
	`otherUnidentified`	TEXT,
	`greenWaste`	TEXT,
	`blackBags-commercial`	TEXT,
	`otherCommercialWaste`	TEXT,
	`vehicleParts`	TEXT,
	`asbestos`	TEXT,
	`chemicalDrums/oil/fuel `	TEXT,
	`clinical`	TEXT,
	`animalCarcass`	TEXT
);