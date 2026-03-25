const commentsList = document.getElementById("comments-list");
const commentMessage = document.getElementById("comment-message");
const favoriteButton = document.getElementById("favorite-btn");
const favoriteMessage = document.getElementById("message");
const projectId = document.body.dataset.projectId;

if (favoriteButton && projectId) {
  favoriteButton.addEventListener("click", async () => {
    try {
      const response = await fetch(`/favorites/${projectId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" }
      });

      if (!response.ok) {
        throw new Error("Erro na requisicao");
      }

      const data = await response.json();
      favoriteMessage.classList.add("success");
      favoriteMessage.innerText = data.message || "Projeto favoritado!";
    } catch (error) {
      favoriteMessage.classList.remove("success");
      favoriteMessage.innerText = "Erro ao favoritar.";
      console.error(error);
    }
  });
}

async function loadComments() {
  if (!commentsList || !projectId) {
    return;
  }

  try {
    const response = await fetch(`/comments/${projectId}`);
    if (!response.ok) {
      throw new Error("Erro ao carregar comentarios");
    }

    const comments = await response.json();
    commentsList.innerHTML = "";

    if (comments.length === 0) {
      commentsList.innerHTML = '<div class="comment-card"><p class="muted-text">Nenhum comentario ainda.</p></div>';
      return;
    }

    comments.forEach((comment) => {
      const div = document.createElement("div");
      div.className = "comment-card";
      div.innerHTML = `
        <div class="comment-top">
          <img src="https://ui-avatars.com/api/?name=${encodeURIComponent(comment.username)}&background=1976d2&color=fff&size=32" alt="Avatar" class="avatar-sm">
          <strong>${comment.username}</strong>
          <span class="comment-date">${comment.created_at}</span>
        </div>
        <div class="comment-body">${comment.content}</div>
      `;
      commentsList.appendChild(div);
    });
  } catch (error) {
    commentsList.innerHTML = '<div class="comment-card"><p class="message">Erro ao carregar comentarios.</p></div>';
    console.error(error);
  }
}

const commentForm = document.getElementById("comment-form");
if (commentForm && projectId) {
  commentForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const content = document.getElementById("comment-content").value.trim();
    if (!content) {
      return;
    }

    try {
      const response = await fetch(`/comments/${projectId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
      });

      if (!response.ok) {
        throw new Error("Erro ao enviar comentario");
      }

      const data = await response.json();
      commentMessage.classList.add("success");
      commentMessage.innerText = data.message || "Comentado com sucesso!";
      document.getElementById("comment-content").value = "";
      await loadComments();
    } catch (error) {
      commentMessage.classList.remove("success");
      commentMessage.innerText = "Erro ao enviar comentario.";
      console.error(error);
    }
  });
}

loadComments();
