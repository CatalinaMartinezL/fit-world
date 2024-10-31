<template>
    <div class="add-class-view">
      <h1>Add New Class</h1>
      <form @submit.prevent="submitClass">
        <label for="name">Class Name:</label>
        <input type="text" v-model="classData.name" required />
  
        <label for="description">Description:</label>
        <input type="text" v-model="classData.description" required />
  
        <label for="schedule">Schedule:</label>
        <input type="text" v-model="classData.schedule" required />
  
        <button type="submit">Add Class</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        classData: {
          name: '',
          description: '',
          schedule: '',
          signupCount: 0
        }
      };
    },
    methods: {
      async submitClass() {
        try {
          const response = await fetch('http://127.0.0.1:5000/api/classes', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.classData)
          });
  
          if (!response.ok) throw new Error('Failed to add class');
  
          const newClass = await response.json();
          console.log('Class added:', newClass);
          this.$router.push({ name: 'classes' }); // Redirect to ClassesView after adding
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .add-class-view {
    text-align: center;
    padding: 20px;
  }
  </style>
  