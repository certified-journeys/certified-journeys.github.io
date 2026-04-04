function getAllCourses() {
  return JSON.parse(localStorage.getItem("courses")) || {};
}
