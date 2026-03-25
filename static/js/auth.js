function setupAuthForm(formId, endpoint, successRedirect, extraData = {}) {
  const form = document.getElementById(formId);
  const message = document.getElementById("message");

  if (!form) {
    return;
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {
      ...Object.fromEntries(formData),
      ...extraData
    };

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (response.ok) {
        window.location.href = successRedirect;
        return;
      }

      if (message) {
        message.innerText = result.message || "Nao foi possivel concluir a acao.";
      }
    } catch (error) {
      if (message) {
        message.innerText = "Erro de conexao. Tente novamente.";
      }
      console.error(error);
    }
  });
}

document.querySelectorAll("[data-auth-endpoint]").forEach((form) => {
  const extraData = {};
  const extraRole = form.dataset.authRole;

  if (extraRole) {
    extraData.role = extraRole;
  }

  setupAuthForm(
    form.id,
    form.dataset.authEndpoint,
    form.dataset.authRedirect,
    extraData
  );
});
