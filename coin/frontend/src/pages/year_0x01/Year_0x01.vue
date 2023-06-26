<template>
  <CoinBackground>
    <div class="year-id">0x01 / 2022-2023</div>
    <div class="challenge-container">
      <img class="coin" src="img/cwbcbtrvms.gif" alt="Challenge Coin" />
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
    document.title = 'HaB Coin | 0x01';
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/theme.scss";

.year-id {
  font-size: 40px;
  color: $color-grey-1;
  margin-top: 20px;
}
.challenge-container {
  position: absolute;
  height: 100vh;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: center;
}

.coin {
  width: 500px;
  height: 500px;
}
</style>
