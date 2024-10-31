<template>
  <div class="classes-view">
    <h1>Available Classes</h1>
    <div class="class-list">
      <div v-if="classes.length === 0">
        <p>No hay clases disponibles en este momento.</p>
      </div>
      <div v-for="classItem in classes" :key="classItem.id" class="class-card">
        <h3>{{ classItem.name }}</h3>
        <p>{{ classItem.description }}</p>
        <p><strong>Horario:</strong> {{ classItem.schedule }}</p>
        <router-link :to="{ name: 'classDetail', params: { id: classItem.id } }">
          <button class="details-button">View Details</button>
        </router-link>
      </div>
    </div>

    <div class="action-buttons">
      <router-link to="/password_check"> <!-- Cambié la redirección aquí -->
        <button class="add-class-button">Add New Class</button>
      </router-link>
      <router-link :to="{ name: 'signup' }">
        <button class="signup-button">Sign Up Now</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      classes: []
    };
  },
  mounted() {
    this.fetchClasses();
  },
  methods: {
    async fetchClasses() {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/classes');
        if (!response.ok) throw new Error('Failed to fetch classes');
        this.classes = await response.json();
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.classes-view {
  text-align: center;
  background-color: #f9f9f9;
  padding: 20px;
}
.class-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.class-card {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 10px;
  width: 250px;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
.action-buttons {
  margin-top: 20px; /* Espacio antes de los botones de acción */
}
.add-class-button,
.signup-button {
  padding: 12px 24px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px; /* Espacio entre botones */
}
.add-class-button:hover,
.signup-button:hover {
  background-color: #45a049;
}
.details-button {
  margin-top: 10px;
  padding: 10px;
  background-color: #008CBA;
  color: white;
  border: none;
  border-radius: 5px;
}
.details-button:hover {
  background-color: #007B9A;
}
</style>
