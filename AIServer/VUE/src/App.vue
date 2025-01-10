<template>
  <div id="app">
    <transition name="slide-left" mode="out-in">
      <router-view v-if="$route.meta.animation === 'slide-left'"></router-view>
    </transition>
    <transition name="slide-right" mode="out-in">
      <router-view v-if="$route.meta.animation === 'slide-right'"></router-view>
    </transition>
  </div>
</template>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

/*左右不分滑动动画*/
.slide-left-enter-active,
.slide-left-leave-active,
.slide-right-enter-active,
.slide-right-leave-active {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: transform 2s ease;
}

.slide-left-enter-from {
  transform: translateX(-100%);
}

.slide-left-leave-to {
  transform: translateX(-100%);
}

.slide-right-enter-from {
  transform: translateX(100%);
}

.slide-right-leave-to {
  transform: translateX(100%);
}
</style>