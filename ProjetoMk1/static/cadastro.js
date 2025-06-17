document.getElementById("cadastro-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const empresa = document.getElementById("empresa").value;
    const produto = document.getElementById("produto").value;
    const imagem = document.getElementById("imagem").value;
    const descricao = document.getElementById("descricao").value;
  
    const novoProduto = {
      id: Date.now(),
      titulo: produto,
      descricao: `${descricao} (Empresa: ${empresa})`,
      imagem: imagem
    };
  
    const dadosSalvos = JSON.parse(localStorage.getItem("investimentos")) || [];
    dadosSalvos.push(novoProduto);
    localStorage.setItem("investimentos", JSON.stringify(dadosSalvos));
  
    alert("Investimento cadastrado com sucesso!");
    window.location.href = "/";
  });
  
  