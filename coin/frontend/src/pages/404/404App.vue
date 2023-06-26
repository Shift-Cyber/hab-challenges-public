<template>
  <CoinBackground>
    <div class="container-404gif">
      <img class="image-404gif" src="/img/404.gif" alt="404 Not Found" />
    </div>
  </CoinBackground>
</template>

<script>
import CoinBackground from '@/components/base/CoinBackground.vue';

export default {
  components: {
    CoinBackground,
  },
  created() {
    document.title = 'HaB Coin | 404';
  },
};
</script>

<style lang="scss" scoped>
.container-404gif {
  left: 0;
  top: 0;
  position: absolute;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}
.image-404gif {
  font-size: 36px;
  color: white;
  text-align: center;
  margin-top: 20px;

  width: 300px;
}
</style>
