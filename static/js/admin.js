async function fetchUsers() {
  const response = await fetch("/admin/users");
  if (!response.ok) {
    return;
  }

  const users = await response.json();
  const tbody = document.querySelector("#users-table tbody");
  tbody.innerHTML = "";

  users.forEach((user) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${user.id}</td>
      <td>${user.email}</td>
      <td>${user.role}</td>
      <td>
        <button onclick="deleteUser(${user.id})" class="button-danger">Deletar</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

async function deleteUser(userId) {
  if (!confirm("Tem certeza que deseja deletar este usuario?")) {
    return;
  }

  const response = await fetch(`/admin/users/${userId}`, { method: "DELETE" });
  if (response.ok) {
    fetchUsers();
    fetchProjects();
    return;
  }

  alert("Erro ao deletar usuario.");
}

async function fetchProjects() {
  const response = await fetch("/admin/projects");
  if (!response.ok) {
    return;
  }

  const projects = await response.json();
  const tbody = document.querySelector("#projects-table tbody");
  tbody.innerHTML = "";

  projects.forEach((project) => {
    const ownerLabel = project.owner
      ? `${project.owner.email} (${project.owner.role})`
      : "Nenhum usuario";

    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${project.id}</td>
      <td>${project.name}</td>
      <td>${ownerLabel}</td>
      <td>
        <button onclick="deleteProject(${project.id})" class="button-danger">Deletar</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

async function deleteProject(projectId) {
  if (!confirm("Tem certeza que deseja deletar este projeto?")) {
    return;
  }

  const response = await fetch(`/admin/projects/${projectId}`, { method: "DELETE" });
  if (response.ok) {
    fetchProjects();
    return;
  }

  alert("Erro ao deletar projeto.");
}

fetchUsers();
fetchProjects();
