<template>
  <div class="outer-chat-pane">
    <div class="inner-chat-pane">
      <div v-if="chats.length == 0" class="intro-window" id="flag{the_DOM_is_like_">
        dvGPT
        <div class="tag">It's a dumpster fire.</div>
      </div>
      <div v-else class="chats" id="crazy_virtual_maaaan}" >
        <div v-for="chat in chats" :key="chat"
        :class="['chat',( Object.keys(chat)[0] === 'server' ) ? 'server': 'client']">
          <div class="chat-content">{{ Object.values(chat)[0] }}</div>
        </div>
      </div>
    </div>
    <div class="chat-management">
      <div class="disclaimer" id="disclaimer"></div>
      <input class="text-input-box" id="message-input"
        placeholder="Send a message..."
        v-on:keydown.enter="onEnter()"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatPane',
  props: {},
  data() {
    return {
      connection: null,
      chats: [],
    };
  },
  mounted() {
    console.log('Connecting to websocket server...');
    // eslint-disable-next-line no-undef
    this.connection = io(this.deriveWsURL());

    this.connection.on('connect', () => {
      this.connection.emit('message', { data: 'I\'m connected!' });
      console.log('Connected to websocket server...');
    });

    this.connection.on('disconnect', () => {
      console.log('Disconnected from the websocket server...');
    });

    this.connection.on('message_event', (message) => this.receiveMessage(message));

    axios.get('footer?message=default')
      .then((response) => {
        document.getElementById('disclaimer').innerHTML = response.data;
      });
  },
  methods: {
    deriveWsURL() {
      if (window.location.protocol === 'https:') {
        return `wss://${window.location.host}/`;
      }
      return `ws://${window.location.host}/`;
    },
    onEnter() {
      const messageValue = document.getElementById('message-input').value;
      if (messageValue !== '') {
        document.getElementById('message-input').value = '';
        this.sendMessage(messageValue);
      }
    },
    // eslint-disable-next-line object-shorthand
    sendMessage: function (message) {
      this.connection.emit('message_event', { data: message });
      this.chats.push({ client: message });
      console.log(this.chats);
    },
    // eslint-disable-next-line object-shorthand
    receiveMessage: function (message) {
      console.log('got message from server', message);
      this.chats.push({ server: message });
    },
  },
};
</script>

<style scoped lang="scss">
@import "../scss/theme.scss";
.outer-chat-pane {
  background-color: $color-chatpane;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: baseline;
  align-items: center;
}

.chat-management {
  width: 800px;
  display: flex;
  align-items: center;
  flex-direction: column-reverse;
}

.inner-chat-pane {
  display: flex;
  flex-direction: column-reverse;
  align-items: center;

  max-width: 800px;
  width: 100%;
  flex-grow: 1;
  overflow: auto;
}

.disclaimer {
  color: grey;
  font-size: 12px;
  margin: 20px;
  text-align: center;
  font-weight: 400;
  max-width: 670px;
}

.text-input-box {
  all:unset;
  max-width: 100%;
  height: 50px;
  min-height: 50px;
  background-color: #4d4e5c6c;
  border-radius: 5px;

  font-size: 16px;
  color: white;
  padding: 0 20px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.164);

  margin-top: 20px;
  width: 800px;
}

.intro-window {
  color: white;
  text-align: center;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  font-size: 50px;
}

.tag {
  font-size: 17px;
}

.chats {
  display: flex;
  flex-direction: column;

  width: 100%;
}

.chat {
  display: flex;
  border-top: 2px solid rgba(128, 128, 128, 0.1);

  color: white;
  line-height: 40px;
}

.server {
  justify-content: left;
}

.client {
  justify-content: right;
}

.chat-content {
  display: block;
}
</style>
