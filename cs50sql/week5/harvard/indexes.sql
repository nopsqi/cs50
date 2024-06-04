CREATE INDEX "search_enrollments" ON enrollments(student_id, course_id);
CREATE INDEX "search_courses" ON courses(department, number, semester, title);
CREATE INDEX "search_satisfies_by_course_id" ON satisfies(course_id);
