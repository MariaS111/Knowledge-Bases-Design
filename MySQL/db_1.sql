
-- 1 task
SELECT * FROM lab11.teacher;

-- 2 task
SELECT * FROM lab11.student_group INNER JOIN lab11.student_group_specialty USING(StudentGroupCodeNumber)
WHERE SpecialtyName = 'ЭВМ';

-- 3 task
SELECT DISTINCT TeacherPersonalNumber, AudienceNumber FROM lab11.teacher_subject_group 
INNER JOIN lab11.teacher USING(TeacherPersonalNumber) 	
WHERE SubjectCodeNumber = '18П';

-- 4 task
SELECT DISTINCT SubjectCodeNumber, Name FROM lab11.teacher 
INNER JOIN lab11.teacher_subject_group USING(TeacherPersonalNumber)
INNER JOIN lab11.subject USING(SubjectCodeNumber)
WHERE teacher.LastName = 'Костин';

-- 5 task
SELECT DISTINCT StudentGroupCodeNumber FROM lab11.teacher_subject_group 
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE teacher.LastName = 'Фролов';

-- 6 task
SELECT subject.* FROM lab11.specialty_subject
INNER JOIN lab11.subject USING(SubjectCodeNumber)
WHERE SpecialtyName = 'АСОИ';

-- 7 task
SELECT DISTINCT teacher.* FROM lab11.specialty_teacher
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE SpecialtyName = 'АСОИ';

-- 8 task
SELECT DISTINCT LastName FROM lab11.teacher_subject_group
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE AudienceNumber = 210;

-- 9 task 
SELECT DISTINCT subject.Name, student_group.Name FROM lab11.teacher_subject_group
INNER JOIN lab11.subject USING(SubjectCodeNumber)
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE AudienceNumber BETWEEN 100 and 200;

-- 10 task
SELECT sg1.StudentGroupCodeNumber as First, sg2.StudentGroupCodeNumber as Second
FROM lab11.student_group_specialty sg1 
INNER JOIN lab11.student_group_specialty sg2 ON sg1.SpecialtyName = sg2.SpecialtyName and sg1.StudentGroupCodeNumber <> sg2.StudentGroupCodeNumber
WHERE sg2.StudentGroupCodeNumber > sg1.StudentGroupCodeNumber;

-- 11 task
SELECT SUM(NumberOfMembers) 'количество студентов, обучающихся на специальности ЭВМ'
FROM lab11.student_group 
INNER JOIN lab11.student_group_specialty USING(StudentGroupCodeNumber)
WHERE SpecialtyName = 'ЭВМ';

-- 12 task 
SELECT DISTINCT TeacherPersonalNumber
FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group_specialty USING(StudentGroupCodeNumber)
WHERE SpecialtyName = 'ЭВМ'
;

-- 13 task 
SELECT *
FROM lab11.teacher_subject_group
GROUP BY SubjectCodeNumber
HAVING COUNT(StudentGroupCodeNumber) = (SELECT COUNT(*) FROM lab11.student_group);

-- 14 task 
SELECT DISTINCT LastName FROM lab11.teacher_subject_group
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE SubjectCodeNumber IN (SELECT SubjectCodeNumber
FROM lab11.teacher_subject_group
WHERE TeacherPersonalNumber = (SELECT DISTINCT TeacherPersonalNumber
FROM lab11.teacher_subject_group
WHERE SubjectCodeNumber = '14П'));

-- 15 task 
SELECT DISTINCT * FROM lab11.subject
WHERE SubjectCodeNumber NOT IN (SELECT DISTINCT SubjectCodeNumber FROM lab11.teacher_subject_group
WHERE TeacherPersonalNumber= '221Л');

-- 16 task 
SELECT * FROM lab11.subject
WHERE SubjectCodeNumber NOT IN (SELECT DISTINCT SubjectCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'М-6');

-- 17 task 
SELECT teacher.* FROM lab11.teacher_subject_group
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE (StudentGroupCodeNumber = '3Г' OR StudentGroupCodeNumber = '8Г') AND Position = 'Доцент'
GROUP BY TeacherPersonalNumber; 

-- 18 task 
SELECT SubjectCodeNumber, TeacherPersonalNumber, StudentGroupCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.specialty_teacher USING(TeacherPersonalNumber)
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE Department = 'ЭВМ' AND SpecialtyName = 'АСОИ' ; 

-- 19 task 
SELECT DISTINCT StudentGroupCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.specialty_teacher USING(TeacherPersonalNumber)
INNER JOIN lab11.student_group_specialty USING(SpecialtyName, StudentGroupCodeNumber); 

-- 20 task 
SELECT DISTINCT TeacherPersonalNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
INNER JOIN lab11.student_group_specialty USING(StudentGroupCodeNumber)
INNER JOIN lab11.specialty_teacher USING(TeacherPersonalNumber, SpecialtyName)
WHERE teacher.Department = 'ЭВМ'; 

-- 21 task 
SELECT DISTINCT student_group_specialty.SpecialtyName FROM lab11.student_group_specialty
INNER JOIN lab11.specialty_teacher USING(SpecialtyName)
INNER JOIN lab11.teacher USING(TeacherPersonalNumber)
WHERE teacher.Department = 'АСУ'; 

-- 22 task
SELECT SubjectCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'АС-8';

-- 23 task-
SELECT DISTINCT StudentGroupCodeNumber FROM lab11.teacher_subject_group
WHERE SubjectCodeNumber IN
(SELECT SubjectCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'АС-8')
GROUP BY StudentGroupCodeNumber
HAVING COUNT(*) = (SELECT COUNT(*) FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'АС-8');


-- 24 task-
SELECT StudentGroupCodeNumber FROM lab11.student_group
WHERE StudentGroupCodeNumber NOT IN (SELECT DISTINCT StudentGroupCodeNumber FROM lab11.teacher_subject_group
WHERE SubjectCodeNumber IN
(SELECT SubjectCodeNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'АС-8'));


-- 25 task
SELECT DISTINCT StudentGroupCodeNumber FROM lab11.teacher_subject_group
WHERE StudentGroupCodeNumber NOT IN
(SELECT StudentGroupCodeNumber FROM lab11.teacher_subject_group
WHERE TeacherPersonalNumber = '430Л');


-- 26 task
SELECT TeacherPersonalNumber FROM lab11.teacher_subject_group
INNER JOIN lab11.student_group USING(StudentGroupCodeNumber)
WHERE student_group.Name = 'Э-15' and SubjectCodeNumber<>'12П';
 
