<template>
    <div class="password-check">
      <h2>Ingrese la Contraseña</h2>
      <input type="password" v-model="inputPassword" placeholder="Contraseña de 4 dígitos" />
      <button @click="checkPassword">Enviar</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        inputPassword: '',
        errorMessage: ''
      };
    },
    methods: {
      checkPassword() {
        if (this.inputPassword === '2004') {
          this.$router.push({ name: 'add_class' });
        } else {
          this.errorMessage = 'Contraseña incorrecta. Inténtalo de nuevo.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .password-check {
    text-align: center;
    margin-top: 50px;
  }
  .error {
    color: red;
  }
  </style>
  