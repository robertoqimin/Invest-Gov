function setupProjectForm(formId, options = {}) {
  const form = document.getElementById(formId);

  if (!form) {
    return;
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {
      title: document.getElementById("empresa").value,
      description: document.getElementById("descricao").value,
      category: document.getElementById("produto").value,
      location: document.getElementById("imagem").value
    };

    try {
      const response = await fetch("/projects/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (!response.ok) {
        alert(result.error || "Erro ao cadastrar projeto");
        return;
      }

      alert(options.successMessage || "Projeto cadastrado com sucesso!");
      form.reset();

      if (options.redirectToProject && result.id) {
        window.location.href = `/projects/${result.id}`;
      }
    } catch (error) {
      alert("Erro ao cadastrar projeto");
      console.error(error);
    }
  });
}

document.querySelectorAll("[data-project-form]").forEach((form) => {
  setupProjectForm(form.id, {
    redirectToProject: form.dataset.redirectToProject === "true"
  });
});
