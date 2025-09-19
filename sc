 <h1>Buscador MP3</h1>
  <button onclick="buscar()">Buscar</button>
  <pre id="resultado"></pre>

  <script>
    async function buscar() {
      let resultado = await window.pywebview.api.searchMP3();
      document.getElementById("resultado").innerText = resultado.join("\n");
    }
  </script>