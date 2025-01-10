<template>
    <div class="camera-container">
      <div class="video-container">
        <video id="video" autoplay playsinline></video>
      </div>
      <button id="capture-button" @click="capturePhoto">拍摄</button>
    </div>
  </template>
  
  <script>
  import { saveAs } from 'file-saver';
  
  export default {
    name: 'Camera',
    data() {
      return {
        serverProcess: null,
      };
    },
    mounted() {
      const video = document.getElementById('video');
  
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          video.srcObject = stream;
        })
        .catch(error => {
          console.error('Error accessing the camera:', error);
        });
    },
    methods: {
      capturePhoto() {
        const video = document.getElementById('video');
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        const squareSize = Math.min(video.videoWidth, video.videoHeight);
  
        canvas.width = squareSize;
        canvas.height = squareSize;
  
        context.drawImage(video, 0, 0, squareSize, squareSize, 0, 0, squareSize, squareSize);
  
        // 将图像转换为Blob格式
        canvas.toBlob(blob => {
          // 使用FileSaver.js保存图像
          saveAs(blob, 'captured_image.jpg');
  
          // 关闭摄像头
          const stream = video.srcObject;
          const tracks = stream.getTracks();
          tracks.forEach(track => track.stop());
  
          // 跳转回/flower界面
          this.$router.push('/flower');
        }, 'image/jpeg');
      },
    },
    beforeRouteLeave(to, from, next) {
        const stream = video.srcObject;
          const tracks = stream.getTracks();
          tracks.forEach(track => track.stop());
      next();
    },
  };
  </script>
  
  <style scoped>
  .camera-container {
    background: linear-gradient(to bottom, #4CAF50, #2196F3); /* 从绿色到蓝色的渐变 */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    padding: 0;
  }
  
  .video-container {
    width: 500px;
    height: 500px;
    background-color: #ccc;
    border: 1px solid #000;
    margin-bottom: 20px;
    position: relative;
  }
  
  #video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  #capture-button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  #capture-button:hover {
    background-color: #45a049;
  }
  </style>
  
  
  