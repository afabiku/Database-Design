-- Departments
INSERT INTO department (DepartmentName) VALUES
('Engineering'), ('Sales'), ('HR'), ('IT Support');

-- Shifts
INSERT INTO shift (Name, start_time, end_time, DaysWorked) VALUES
('Morning Shift', '08:00:00', '16:00:00', 'Mon-Fri'),
('Night Shift', '22:00:00', '06:00:00', 'Sun-Thu'),
('Weekend Shift', '10:00:00', '18:00:00', 'Sat-Sun');

-- Certifications
INSERT INTO certification (CertificationName, Description) VALUES
('First Aid', 'Certified in basic first aid procedures'),
('Forklift Operation', 'Qualified to operate warehouse forklifts'),
('Cybersecurity Basics', 'Completed basic cybersecurity training');

-- Employees
INSERT INTO employee (FirstName, LastName, StartDate, Salary, Status, YearsAtCompany, Strikes, PTOUsed, PTORemaining, HoursWorked, DepartmentID, ShiftID)
VALUES
('Alice', 'Anderson', '2020-01-15', 75000, 'Full-Time', 4, 0, 10, 80, 160.00, 1, 1),
('Bob', 'Brown', '2022-06-01', 55000, 'Part-Time', 2, 1, 4, 36, 60.00, 2, 3),
('Charlie', 'Clark', '2023-03-22', 60000, 'Full-Time', 1, 0, 0, 40, 80.00, 4, 2);

-- Disciplinary Actions
INSERT INTO disciplinaryAction (EmployeeID, ActionType, ActionDate, Description)
VALUES
(2, 'Late Arrival', '2023-08-14', 'Arrived 30 minutes late without notice'),
(2, 'Missed Shift', '2023-09-10', 'Missed weekend shift without informing');

-- Employee Certifications
INSERT INTO employeeCertification (EmployeeID, CertificationID, DateObtained)
VALUES
(1, 1, '2020-02-01'),
(1, 3, '2021-11-15'),
(2, 2, '2022-07-10'),
(3, 3, '2023-04-05');
