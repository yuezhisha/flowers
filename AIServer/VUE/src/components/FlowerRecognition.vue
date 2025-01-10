<template>
  <div class="flower-recognition">
    <Modal :isVisible="showModal" @update:isVisible="showModal = $event">
      <h2>未知花卉</h2>
      <p>请重新拍照</p>
    </Modal>
    <Modal :isVisible="cc" @update:isVisible="cc = $event">
      <h2>数据获取方式已切换</h2>
      <p>请重新提交</p>
    </Modal>
    <video autoplay loop muted playsinline class="video-background">
      <source src="@/assets/1.mp4" type="video/mp4">
      您的浏览器不支持视频标签。
    </video>
    <div class="rectangle">
      <h1 class="title">欢迎来到花卉识别系统</h1>
      <div class="component-container">
        <div class="component">
          <h2 class="component-title">摄像头模块</h2>
          <div class="square-container">
            <div class="square"  v-if="careamra==false">
              <v-text @click="startCamera">开摄像头</v-text>
              <img :src="photo" v-if='photo' style="width: 80%;"/>
              <Blank style="height: 300px;" v-else></Blank>
            </div>
            <div v-if="careamra">
            <video ref="video" class = "squire" autoplay playsinline style="width: 80%;"></video>
            <canvas ref="canvas" style="display:none;"></canvas>
            </div>
          </div>
          <button @click="takePhoto">拍照</button>
          <button @click="uploadPhoto">识别</button>
        </div>
        <div class="component">
          <div class="text-box1">
            <h2 class="component-title">花卉名称</h2>
            <p class="text-content" >{{ flowerName }}</p>
          </div>
          <div class="text-box2">
            <h2 class="component-title">详细信息</h2>
            <p class="text-content">{{ description }}</p>
          </div>
          <button @click="update">切换数据获取方式</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { KeepAlive } from 'vue';
import axios from '../http/http';
import Modal from './Modal.vue';
import mqtt from 'mqtt';
export default {
  components: {
    Modal,
  },
  data() {
    return {
       flowerName: '',
      description: '',
      careamra: false,
      stream:null,
      photo:null,
      showModal: false,
      change:false,
      cc : false,
      client: null,
    };
  },
  created(){
    this.connect()
  },
  mounted(){
    axios.get()
    axios({
      method:'get',
      url:'/csrf'
  }).then(res=>{console.log(res);axios.defaults.headers['X-CSRFToken'] = res.data["csrftoken"];})
    this.client.on('message', this.onMessage);
  },
beforeDestroy() {
    this.client.removeListener('message', this.onMessage);
    this.client.end();
},
  methods: {
    update(){
      this.cc = true;
      this.change = !this.change;
    },
    takePhoto() {
      const canvas = this.$refs.canvas;
      const video = this.$refs.video;
      const context = canvas.getContext('2d');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      // 将画布内容转为 Base64 数据
      this.photo = canvas.toDataURL('image/png');
      this.stopCamera()
      this.careamra = false
    },
    async uploadPhoto() {
      if (!this.photo) return;

      // 转换 Base64 为 Blob 格式
      const blob = this.base64ToBlob(this.photo);

      const formData = new FormData();
      formData.append('image', blob, 'photo.png'); // 文件名可自定义

      try {
        setTimeout(() => {
          axios({
            method:"post",
            url: '/picture',
            data: formData
          }).then(res=>{
            if(this.change == false){
                if(res.data.error){
                  this.showModal=true
                }else{
                  this.flowerName = res.data.name;
                  this.description = res.data.description;
                }
            }else{

            }
          })
          })
      } catch (error) {
        console.error('上传过程中出现错误:', error);
      }
    },
    connect(){
      const options={
        clientId: 'mqttjs_' + Math.random().toString(16).substr(2, 8),
        KeepAlive: 60,
      }
      this.client = mqtt.connect('mqtt://172.18.0.2:1883', options);
      this.client.on('connect', () => {
        const topics = ['flowers/name', 'flowers/category', 'flowers/description'];
        this.subscribe(topics,(err)=>{
          if (err) {
          console.error('订阅失败：', err);
        } else {
          console.log('已订阅多个主题');
        }
        }); // 订阅主题
      });
    },
    onMessage(topic, payload) {
      const message = payload.toString();
      switch (topic){
        case "flowers/name" :
          this.name = message
        case 'flowers/description':
          this.description = message
      }
    },
    base64ToBlob(base64) {
      const byteString = atob(base64.split(',')[1]);
      const mimeString = base64.split(',')[0].split(':')[1].split(';')[0];
      const ab = new ArrayBuffer(byteString.length);
      const ia = new Uint8Array(ab);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      return new Blob([ab], { type: mimeString });
    },
    async startCamera() {
      this.careamra=true;
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.$refs.video.srcObject = this.stream;
      } catch (error) {
        console.error('无法打开摄像头', error);
      }
    },
    stopCamera() {
      if (this.stream) {
        // 停止所有轨道
        this.stream.getTracks().forEach(track => track.stop());
        this.stream = null;
      }
      // 清理 video 元素
      this.$refs.video.srcObject = null;
    },
  },
};
</script>

<style scoped>
.flower-recognition {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column; 
}

.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.rectangle {
  position: relative;
  width: 80%;
  min-height: 100vh;
  background-color: rgba(255, 255, 255, 0.3);
  display: flex;
  justify-content: center;
  align-items: center; 
  flex-direction: column; 
  padding-top: 20px; 
  min-width: 320px; 
  min-height: 100vh; 
}

.title {
  color: black;
  font-size: 2em; 
  font-weight: bold; 
  font-style: italic; 
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px; 
}

.component-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 100%;
}

.component {
  border: 1px solid black;
  padding: 10px;
  margin-bottom: 20px;
  box-sizing: border-box;
  width: 48%; 
}
#video {
    width: 100ch;
    height: 100ch;
    object-fit: cover;
  }
.component-title {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 10px;
}

.square-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.square {
  display: flex;
  width: 80%;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  margin-bottom: 10px;
  flex-direction: column; 
}

button {
  width: 50%;
  margin-bottom: 10px;
  padding: 5px;
}

.text-box1 {
  border: 1px solid black;
  padding: 10px;
  margin-bottom: 10px;
  box-sizing: border-box;
  width: 100%;
  height: 20%;
  max-height: 100px;
  overflow-y: auto; /* 垂直方向超出部分显示滚动条 */
}

.text-box2 {
  border: 1px solid black;
  padding: 10px;
  margin-bottom: 10px;
  box-sizing: border-box;
  width: 100%;
  height: 80%;
  max-height: 800px; 
  overflow-y: auto; 
}


@media (max-width: 768px) {
  .component {
    width: 100%; /* 在小屏幕上，组件占满宽度，变为纵向排列 */
  }
}
</style>
