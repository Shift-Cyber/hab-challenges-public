<template>
  <div class="nav-item-container" @click="navToChallenge()">
    <div class="season">{{ season }}</div>
    <div class="year">{{ year }}</div>
    <div class="space"></div>
    <div class="category">{{ category }}</div>
    <div class="space"></div>
    <div class="difficulty-container">
      <div class="difficulty-indicator" :class="{'active': difficulty >= 1}" ></div>
      <div class="difficulty-indicator" :class="{'active': difficulty >= 2}" ></div>
      <div class="difficulty-indicator" :class="{'active': difficulty >= 3}" ></div>
      <div class="difficulty-indicator" :class="{'active': difficulty >= 4}" ></div>
      <div class="difficulty-indicator" :class="{'active': difficulty >= 5}"
        style="margin-right: 10px;"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CoreBackground',
  components: {},
  props: {
    year: String,
    season: String,
    category: String,
    difficulty: Number,
    navURL: String,
  },
  methods: {
    navToChallenge() {
      window.location.href = this.navURL;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/theme.scss";

.nav-item-container {
  height: 50px;
  width: 700px;

  background: $color-blue-4;
  border-radius: 5px;
  border: 2px solid $color-blue-3;

  display: flex;
  flex-direction: row;
}

.nav-item-container:hover {
  filter: brightness(120%);
  cursor: pointer;
}

.year {
  font-size: 20px;
  line-height: 50px;
}

.season {
  font-size: 20px;
  line-height: 50px;
  font-weight: 700;

  margin: 0 20px;
}

.category {
  font-size: 20px;
  line-height: 50px;

  margin: 0 20px;
}

.difficulty-container {
  height: 100%;
  display: flex;
  flex-direction: row;

  align-items: center;
}

.difficulty-indicator {
  height: 30px;
  width: 30px;

  background-color: $color-blue-2;
  margin: auto;

  border-radius: 5px;
  margin: 5px;

  &.active {
    background-color: $color-blue-1;
  }
}
</style>
