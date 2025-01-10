// 假设你的CSRF令牌存储在名为'csrftoken'的cookie中
// 注意：这取决于你的后端如何设置和命名CSRF令牌cookie

// 创建一个Axios实例
import axios from "axios";

const axiosInstance = axios.create({
    // Axios配置...
    baseURL: 'http://localhost:8000/model/',
    // 其他配置...
});
// 添加请求拦截器
axiosInstance.interceptors.request.use(function (config) {
    // 从cookie中获取CSRF令牌
    // 注意：这里需要一个函数来读取cookie，因为Axios本身不提供此功能
    // 你可能需要使用第三方库（如js-cookie）或自己编写函数来读取cookie
    const csrftoken = getCsrfToken('csrftoken'); // 假设getCookie是一个读取cookie的函数

    // 如果存在CSRF令牌，则将其添加到请求头中
    if (csrftoken) {
      
        config.headers['X-CSRFToken'] = csrftoken;
    }else{
      console.log(document.cookie)
    }
    // 发送请求
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});
// 示例函数来读取cookie（简单实现，可能不适用于所有情况）
function getCsrfToken() {
    const cookies = document.cookie.split(';');
    console.log(document.cookie)
    for (let cookie of cookies) {
      const trimmed = cookie.trim();
      if (trimmed.startsWith('csrftoken=')) {
        return trimmed.substring('csrftoken='.length);
      }
    }
    return null; // 未找到时返回 null
  }
  

// 现在你可以使用axiosInstance来发送请求，并且它会自动包含X-CSRFToken请求头（如果CSRF令牌存在的话）
export default axiosInstance;