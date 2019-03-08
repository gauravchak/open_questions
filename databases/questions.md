1. Write an SQL query to get a list of tenant who are renting more than one apartment
```SQL
/*
Get tenantIDs that are associated with more than one aptid
join with Tenants and select TenantName
*/
SELECT TenantName 
FROM Tenants INNER JOIN 
    (SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING COUNT(APTID) > 1) T ON Tenants.TenantID = T.TenantID
```

2. Get a list of all buildings and the number of open requests, i.e. requests where status = "Open"

```SQL
SELECT BuildingName, ISNULL(Count, 0) as 'Count'
FROM Buildings 
LEFT JOIN
  (SELECT BuildindID, Count(*) as 'Count'
  FROM Requests INNER JOIN 
  Apartments ON Apartments.AptID = Requests.AptID
  WHERE Requests.Status = "Open"
  GROUP BY Apartments.BuildingID) B 
ON Buildings.BuildingID = B.BuildingID
```

3. Close all requests of apartments in Building # 11
```SQL
UPDATE Requests
SET STATUS = 'Closed'
WHERE AptID in (SELECT AptID in Apartments WHERE BuildingID = 11)
```

7. Design grade database and return SQL query to select top 10% by GPA
```SQL
/*
Tables are

Students: StudentID: int, SName: varchar(100), Address: varchar(500)
Courses: CourseID:int , InstructorID:int, CName: varchar(100)
Enrollments: StudentID: int, CourseID: int, Grade: float, term: int
*/
SELECT TOP 10 PERCENT AVG(Enrollments.Grade) AS GPA, Enrollments.StudentID FROM Enrollments 
GROUP BY Enrollments.StudentID
ORDER BY AVG(Enrollments.Grade)

/* This returns top 10 percent not the people with the GPA in the top 10 percent.
*/
/*Define variable @gpacutoff */
DECLARE @gpacutoff float;
SET @gpacutoff = (SELECT MIN(gpa) as 'MinGPA' FROM (
    SELECT TOP 10 PERCENT AVG(Enrollments.Grade) as 'gpa' FROM Enrollments
    GROUP BY Enrollments.StudentID
    ORDER BY gpa DESC) GpaTable
);
/* Select students with GPA more than cutoff */
SELECT StudentName, 'gpa' 
FROM Students INNER JOIN (
    SELECT Enrollments.StudentID, AVG(Enrollments.Grade) as 'gpa' FROM Enrollments GROUP BY Enrollments.StudentID HAVING AVG(Enrollments.Grade) >= @gpacutoff) GpaStuds ON GpaStuds.StudentID = Students.StudentID ;
```