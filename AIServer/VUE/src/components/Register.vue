<template>
  <div class="register-container">
    <h1>花卉识别系统</h1>
    <form @submit.prevent="register">
      <h2 style="color: #2196F3;">注册</h2>
      <div>
        <label for="username">用户名:</label>
        <input v-model="username" type="text" id="username" required>
      </div>
      <div>
        <label for="password">密码:</label>
        <input v-model="password" type="password" id="password" required>
      </div>
      <button type="submit" style="background-color: #2196F3;">注册</button>
      <p><router-link to="/login">登录</router-link></p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    register() {
      if (this.registerUser(this.username, this.password)) {
        alert('注册成功');
        this.$router.push('/login');
      } else {
        alert('注册失败，请重试');
      }
    },
    registerUser(username, password) {
      // 检查用户名是否已存在，然后将用户名和密码保存到本地存储
      if (!this.checkUsernameExists(username)) {
        localStorage.setItem('registeredUser', JSON.stringify({ username, password }));
        return true;
      }
      return false;
    },
    checkUsernameExists(username) {
      // 检查用户名是否已存在
      const registeredUser = JSON.parse(localStorage.getItem('registeredUser'));
      return registeredUser && registeredUser.username === username;
    }
  }
};
</script>

<style scoped>
.register-container {
  background: linear-gradient(to bottom, #2196F3, #4CAF50); /* 从蓝色到绿色的渐变 */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

h1 {
  text-align: center;
  color: white;
  font-size: 36px; 
  margin-bottom: 20px; 
}

form {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center; 
  gap: 10px;
  width: 300px; 
}

h2 {
  text-align: center;
  margin-bottom: 10px; 
}

label {
  margin-bottom: 5px; 
}

input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button {
  padding: 10px;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  width: 80%; 
}

button:hover {
  background-color: #45a049;
}

p {
  text-align: center;
  color: #4CAF50; 
  margin-top: 10px; 
}
</style>
