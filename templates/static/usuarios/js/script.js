{% comment %} function togglePasswordVisibility() {
    var senhaInput = document.getElementById("senha");
    var icon = document.querySelector(".toggle-password i");

    // Alterna entre o tipo de input 'password' e 'text'
    if (senhaInput.type === "password") {
        senhaInput.type = "text";
        icon.classList.remove("bi-eye");
        icon.classList.add("bi-eye-slash"); // Muda o ícone para o de "olho fechado"
    } else {
        senhaInput.type = "password";
        icon.classList.remove("bi-eye-slash");
        icon.classList.add("bi-eye"); // Muda o ícone para o de "olho aberto"
    }
} {% endcomment %}

