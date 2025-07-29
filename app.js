// 🧩 Autocompletado desde palabras.txt
fetch("palabras.txt")
  .then(res => res.text())
  .then(texto => {
    const lista = document.getElementById("listaPalabras");
    const lineas = texto.split("\n");

    lineas.forEach(palabra => {
      palabra = palabra.trim();
      if (palabra) {
        const option = document.createElement("option");
        option.value = palabra;
        lista.appendChild(option);
      }
    });
  })
  .catch(err => {
    console.error("Error al cargar palabras.txt:", err);
    const fallback = document.createElement("div");
    fallback.classList.add("chat-message", "system");
    fallback.textContent = "⚠️ No se pudo cargar el buscador.";
    document.getElementById("chatWindow").appendChild(fallback);
  });

// 🧠 Consulta desde glosario_senado.json (lista de objetos enriquecidos)
fetch("glosario_senado.json")
  .then(res => res.json())
  .then(glosario => {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("userInput");
    const chatWindow = document.getElementById("chatWindow");

    if (!form || !input || !chatWindow) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const palabraIngresada = input.value.trim().toLowerCase();
      if (!palabraIngresada) return;

      // 💬 Mostrar palabra ingresada
      const userMsg = document.createElement("div");
      userMsg.classList.add("chat-message", "user");
      userMsg.textContent = palabraIngresada;
      chatWindow.appendChild(userMsg);

      // 🔍 Buscar entrada en el glosario
      const entrada = glosario.find(
        item => item.palabra.toLowerCase() === palabraIngresada
      );

      if (entrada) {
        // 📘 Bloque de descripción
        const descripcionMsg = document.createElement("div");
        descripcionMsg.classList.add("chat-message", "system");
        descripcionMsg.textContent = `🧭 ${entrada.descripcion}`;
        chatWindow.appendChild(descripcionMsg);

        // ✋ Bloque de seña
        const señaMsg = document.createElement("div");
        señaMsg.classList.add("chat-message", "system");
        señaMsg.textContent = `✋ ${entrada.seña}`;
        chatWindow.appendChild(señaMsg);
      } else {
        const errorMsg = document.createElement("div");
        errorMsg.classList.add("chat-message", "system");
        errorMsg.textContent = "❌ Palabra no encontrada en el glosario.";
        chatWindow.appendChild(errorMsg);
      }

      chatWindow.scrollTop = chatWindow.scrollHeight;
      input.value = "";
    });
  })
  .catch(err => {
    console.error("Error al cargar glosario_senado.json:", err);
    const fallback = document.createElement("div");
    fallback.classList.add("chat-message", "system");
    fallback.textContent = "⚠️ No se pudo cargar el glosario institucional.";
    document.getElementById("chatWindow").appendChild(fallback);
  });