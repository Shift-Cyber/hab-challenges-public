<template>
  <div class="coin-background">
    <div class="content"><slot></slot></div>
    <div class="space"></div>
    <div class="footer">© Shift Cyber {{ new Date().getFullYear() }}</div>
  </div>
</template>

<script>
export default {
  name: 'CoreBackground',
  components: {},
};
</script>

<style lang="scss">
@import "@/scss/theme.scss";

@font-face {
  font-family: 'cairo';
  src: url('../../../fonts/cairo.ttf');
}

* { font-family: 'cairo'; }

body {
  margin: 0;
  background-color: $color-background;
}

.space {
  flex-grow: 1;
}

.coin-background {
  height: 100vh;
  width: 100vw;

  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
  width: min(700px, 95%);
  display:flex;
  flex-direction: column;
  align-items: center;
  overflow: clip;
}

.footer {
  color: $color-grey-2;
  margin-bottom: 10px;
}
</style>
