<template>
  <div class='app-pane'>
    <HelpModal></HelpModal>
    <ControlColumn :chats="chats"/>
    <ChatPane :passedChats="chats"/>
  </div>
</template>

<script>
import HelpModal from '@/components/HelpModal.vue';
import ControlColumn from '@/components/ControlColumn.vue';
import ChatPane from '@/components/ChatPane.vue';

export default {
  name: 'dvGPT',
  components: {
    HelpModal,
    ControlColumn,
    ChatPane,
  },
  data() {
    return {
      chats: [],
    };
  },
};
</script>

<style lang='scss'>
body {
  margin: 0;
}
.app-pane {
  display: flex;
  flex-direction: row;

  height: 100vh;
  width: 100vw;

  overflow: hidden;
}

* {
  font-family:Verdana, Geneva, Tahoma, sans-serif;
}
</style>
