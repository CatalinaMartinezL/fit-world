<template>
  <div class="home">
    <h1>Welcome to Fit World!</h1>
    <p>Your journey to fitness starts here. Discover our wide range of classes and sign up!</p>
    <img src="../assets/gimnasio.jpg" alt="Fit World Gym" class="gym-image" />
    
    <router-link :to="{ name: 'classes' }">
      <button class="classes-button">Clases Disponibles</button>
    </router-link>

    <button class="add-class-button" @click="askPassword">Agregar Clase</button>

    <div class="about-contact-buttons">
      <router-link to="/about">
        <button class="about-button">About Us</button>
      </router-link>
      <router-link to="/contact">
        <button class="contact-button">Contact Us</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    askPassword() {
      const password = prompt("Ingrese la contraseña de 4 dígitos:");
      if (password === "2004") { // Cambia a la contraseña "2004"
        this.$router.push('/add_class'); // Redirige al formulario si la contraseña es correcta
      } else {
        alert("Contraseña incorrecta. Acceso denegado.");
      }
    }
  }
}
</script>

<style scoped>
.home {
  text-align: center;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: #f1f1f1;
  border-radius: 8px; /* Añadir borde redondeado a la sección */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Sombra para darle profundidad */
}
.gym-image {
  width: 80%;
  margin-top: 20px;
  border-radius: 8px;
}
.classes-button,
.add-class-button,
.about-button,
.contact-button {
  margin: 10px;
  padding: 12px 24px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s; /* Efecto de transición */
}
.classes-button:hover,
.add-class-button:hover,
.about-button:hover,
.contact-button:hover {
  background-color: #45a049;
}
</style>
