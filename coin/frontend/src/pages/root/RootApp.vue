<template>
  <CoinBackground>
    <div>
      <a class="banner" href="https://www.hackabit.com"><img src="img/banner.png" alt="banner" /></a>
      <div class="sub-title">Putting the in challenge in coin since 2023!</div>
    </div>

    <div class="description">Hack a Bit provides students with hardcore technical cyber
      education and an introduction to what could be a lucrative and fulfilling career. Staff
      in the program provide education through a variety of technical challenges. Each year
      participating students receive a challenge coin in their merch pack. This challenge
      coin links them to a challenge here on this website to continue their learning. You
      can find an overview of all the challenges since HaB's inception below.</div>
    <div class="description">For all of these challenges there is only one flag and
      there is no submission link, it is simply for fun. Good luck! Please reach
      out in the Discord for support.</div>

    <div class="challenge-nav-details">
      <div class="year">Year</div>
      <div class="season">Season</div>
      <div class="space"></div>
      <div class="category">Category</div>
      <div class="space"></div>
      <div class="difficulty">Difficulty</div>
    </div>
    <div class="yearly-challenge-navigation">
      <ChallengeNavItem :year="'2022-2023'" :season="'0x01'" :difficulty=1
      :category="'Steganography'" :navURL="'/ucfkohzrtj'" ></ChallengeNavItem>
    </div>
  </CoinBackground>
</template>

<script>
import CoinBackground from '@/components/base/CoinBackground.vue';
import ChallengeNavItem from '@/components/root/ChallengeNavItem.vue';

export default {
  components: {
    CoinBackground,
    ChallengeNavItem,
  },
  created() {
    document.title = 'HaB Coin';
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/theme.scss";

.banner {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;

  img {
    height: 100px;
  }
}

.sub-title {
  color: $color-yellow-1;
  text-align: center;
  margin: 20px;
}

.challenge-nav-details {
  width: min(700px, 95%);
  display: flex;
  flex-direction: row;

  color: $color-white-1;
  text-align: center;
  margin-bottom: 5px;

  .year { width: 43px; margin: 0 20px; }
  .season { width: 98px; }
  .difficulty { width: 205px; }
}

.description {
  width: min(500px, 95%);
  text-align: justify;
  color: $color-grey-1;
  font-size: 14px;
  margin-bottom: 20px;
}

.yearly-challenge-navigation {
  width: 100%;
  display: flex;
  flex-direction: column;

  align-items: center;
  color: $color-grey-2;
}

@media screen and ( max-width: 700px ) {
  .challenge-nav-details {
    display: none;
  }
  .yearly-challenge-navigation {
    display: none;
  }
}

</style>
