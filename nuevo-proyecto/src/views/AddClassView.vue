<template>
    <div>
      <h2>Agregar Clase</h2>
      <form @submit.prevent="submitForm">
        <label for="name">Nombre:</label>
        <input type="text" v-model="newClass.name" required />
  
        <label for="description">Descripción:</label>
        <input type="text" v-model="newClass.description" required />
  
        <label for="schedule">Horario:</label>
        <input type="text" v-model="newClass.schedule" required />
  
        <label for="image">Imagen (ruta):</label>
        <input type="text" v-model="newClass.image" required />
  
        <button type="submit">Agregar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newClass: {
          name: '',
          description: '',
          schedule: '',
          image: '',
        }
      };
    },
    methods: {
      async submitForm() {
        const response = await fetch('/api/classes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newClass),
        });
  
        if (response.ok) {
          alert("Clase agregada exitosamente");
          this.$router.push('/classes'); // Redirige a la vista de clases
        } else {
          alert("Error al agregar la clase");
        }
      }
    }
  }
  </script>
  