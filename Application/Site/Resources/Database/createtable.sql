CREATE TABLE `Reports` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tipLocation`	TEXT NOT NULL,
	`locationDescription`	TEXT ,
	`waste`	INTEGER ,
	`wasteSizeID`	INTEGER ,
	`wasteDescription`	TEXT,
	`imageID`	INTEGER ,
	`witness`	TEXT DEFAULT 'No',
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