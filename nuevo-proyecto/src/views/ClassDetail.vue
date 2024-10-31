<template>
    <div v-if="classItem">
      <h1>{{ classItem.name }}</h1>
      <p>{{ classItem.description }}</p>
      <p><strong>Schedule:</strong> {{ classItem.schedule }}</p>
      <router-link to="/classes">
        <button>Volver a Clases</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import classesData from '../data/classes.json';
  
  export default {
    name: 'ClassDetail',
    data() {
      return {
        classItem: null,
      };
    },
    created() {
      const classId = parseInt(this.$route.params.id);
      this.classItem = classesData.find(item => item.id === classId);
    },
  };
  </script>
  
  <style scoped>
  /* Puedes agregar estilos específicos para la vista de detalle aquí */
  </style>
  