async function loadCourses() {
  const res = await fetch("config/courses.json");
  const courses = await res.json();

  const container = document.getElementById("trackers");

  courses.forEach(course => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <h3>${course.name}</h3>
      <a href="courses/${course.id}/index.html">Open</a>
    `;

    container.appendChild(card);
  });
}
loadCourses();
