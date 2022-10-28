CREATE DATABASE lab11;

CREATE TABLE lab11.teacher (
  TeacherPersonalNumber varchar(4) NOT NULL,
  LastName varchar(20) DEFAULT NULL,
  Position varchar(20) DEFAULT NULL,
  Department varchar(50) DEFAULT NULL,
  HomePhone varchar(3) DEFAULT NULL,
  PRIMARY KEY (TeacherPersonalNumber)
);

 CREATE TABLE lab11.student_group (
  StudentGroupCodeNumber varchar(3) NOT NULL,
  Name varchar(4) DEFAULT NULL,
  NumberOfMembers int DEFAULT NULL,
  HeadmanLastName varchar(20) DEFAULT NULL,
  PRIMARY KEY (StudentGroupCodeNumber),
  CONSTRAINT student_group_chk_1 CHECK ((NumberOfMembers > 0))
);


 CREATE TABLE lab11.subject (
  SubjectCodeNumber varchar(3) NOT NULL,
  Name varchar(20) DEFAULT NULL,
  Hours int DEFAULT NULL,
  Semester char(1) DEFAULT NULL,
  PRIMARY KEY (SubjectCodeNumber),
  CONSTRAINT subject_chk_1 CHECK ((Hours > 0))
);

CREATE TABLE lab11.specialty (
  Name varchar(70) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE lab11.teacher_subject_group (
  StudentGroupCodeNumber varchar(3) NOT NULL,
  SubjectCodeNumber varchar(3) NOT NULL,
  TeacherPersonalNumber varchar(4) NOT NULL,
  AudienceNumber int NOT NULL,
  PRIMARY KEY (StudentGroupCodeNumber,SubjectCodeNumber,TeacherPersonalNumber,AudienceNumber),
  CONSTRAINT teacher_subject_group_chk_1 CHECK ((AudienceNumber > 0))
);

 CREATE TABLE lab11.specialty_subject (
  SpecialtyName varchar(70) DEFAULT NULL,
  SubjectCodeNumber varchar(3) DEFAULT NULL
);

 CREATE TABLE lab11.specialty_teacher (
  SpecialtyName varchar(70) DEFAULT NULL,
  TeacherPersonalNumber varchar(4) DEFAULT NULL
);


CREATE TABLE lab11.student_group_specialty (
  SpecialtyName varchar(70) DEFAULT NULL,
  StudentGroupCodeNumber varchar(3) DEFAULT NULL
)






