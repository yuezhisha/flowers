<template>
    <div class="login-container">
      <h1>花卉识别系统</h1>
      <form @submit.prevent="login">
        <h2>登录</h2>
        <div>
          <label for="username">用户名:</label>
          <input v-model="username" type="text" id="username" required>
        </div>
        <div>
          <label for="password">密码:</label>
          <input v-model="password" type="password" id="password" required>
        </div>
        <button type="submit">登录</button>
        <p><router-link to="/register">注册</router-link></p>
      </form>
      <div v-if="showPopup" class="popup">
        <p>登录成功，还剩{{ countdown }}秒自动跳转</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        showPopup: false, 
        countdown: 5 // 倒计时初始值
      };
    },
    methods: {
      login() {
        if (this.checkCredentials(this.username, this.password)) {
          this.showPopup = true; // 显示弹窗
          this.startCountdown(); // 开始倒计时
        } else {
          alert('用户名或密码错误');
        }
      },
      checkCredentials(username, password) {
        // 从本地存储中获取注册数据并进行比较
        const registeredUser = JSON.parse(localStorage.getItem('registeredUser'));
        return registeredUser && registeredUser.username === username && registeredUser.password === password;
      },
      startCountdown() {
        // 使用 setInterval 每秒更新倒计时
        const timer = setInterval(() => {
          this.countdown--;
          if (this.countdown <= 0) {
            clearInterval(timer); // 清除定时器
            this.showPopup = false; // 隐藏弹窗
            this.$router.push('/flower'); // 跳转到花卉识别系统页面
          }
        }, 1000);
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    background: linear-gradient(to bottom, #4CAF50, #2196F3); /* 从绿色到蓝色的渐变 */
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
    color: #4CAF50; 
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
    background-color: #4CAF50;
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
  
  /* 弹窗*/
  .popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 9999;
  }
  </style>
  
  
  