<template>
  <div class="control-column">
    <div class="new-chat-button chat">
      <div class="chat-icon">
        <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
      </div>New chat</div>
    <div class="chats-list" style="overflow: auto;">
      <div class="chat" v-for="chat in chats" :key="chat">
        <div class="chat-icon"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0
         0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em"
         width="1em" xmlns="http://www.w3.org/2000/svg">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1
         2 2z"></path></svg></div>{{chat}}</div>
    </div>
    <div class="control">
      <div class="control-item">
        <div class="control-item-icon">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
          xmlns="http://www.w3.org/2000/svg"><polyline points="3 6 5 6 21 6"></polyline><path
          d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
          <line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line>
          </svg>
        </div>Clear conversations</div>
      <div class="control-item">
        <div class="control-item-icon">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
          xmlns="http://www.w3.org/2000/svg"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2">
          </path><circle cx="12" cy="7" r="4"></circle></svg>
        </div>Upgrade to Plus<div class="space"></div><span class="new-icon">NEW</span></div>
      <div class="control-item">
        <div class="control-item-icon">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
          xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="3"></circle><path d="M19.4
           15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65
           0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0
           0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65
           1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65
           0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83
           0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2
           2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0
           1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2
           0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        </div>Settings</div>
      <div class="control-item" @click="openHelpModal()">
        <div class="control-item-icon">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
          xmlns="http://www.w3.org/2000/svg"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2
          2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14"
          x2="21" y2="3"></line></svg>
        </div>Get help</div>
      <div class="control-item">
        <div class="control-item-icon">
          <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
          stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em"
          xmlns="http://www.w3.org/2000/svg"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4">
          </path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9"
          y2="12"></line></svg>
        </div>Log out</div>
    </div>
    <Button id="modal-trigger" class="btn btn-primary" data-toggle="modal"
    data-target="#helpModal" style="display:none;"
    ><i class="fa-solid fa-circle-plus"></i></Button>
  </div>
</template>

<script>
export default {
  name: 'ControlColumn',
  props: {
    chats: Array,
  },
  methods: {
    openHelpModal() {
      document.getElementById('modal-trigger').click();
    },
  },
};
</script>

<style scoped lang="scss">
@import "../scss/theme.scss";

.control-column {
  background-color: $color-controlcolumn;
  width: 250px;

  display: flex;
  flex-direction: column;
}

.chat-list {
  flex-grow: 1;
}

.new-icon {
  background-color: #FAE69E;
  border-radius: 5px;
  padding: 2px 5px;
  color: black;
  height: 20px;
  line-height: 20px;
}

.new-chat-button {
  border: 1px solid grey;
}

.chat {
  color: white;
  font-size: 14px;
  display: block;
  overflow: clip;
  min-height: 30px;
  max-height: 30px;
  line-height: 30px;

  margin: 5px;
  padding: 10px;
  margin-right: 10px;

  border-radius: 5px;
  white-space: nowrap;

  display:flex;
  flex-direction: row;
  align-items: center;
  justify-content: baseline;
}

.chat-icon {
  margin-right: 10px;
  margin-top: 2px;
}

.chat:hover {
  background-color: rgba(53, 52, 64, 0.6);
  cursor: pointer;
}

.control {
  color: white;
  border-top: 1px solid rgb(70, 70, 70);

  font-size: 14px;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Sans Unicode', sans-serif;
}

.control-item {
  height: 49px;
  line-height: 49px;

  display:flex;
  flex-direction: row;
  align-items: center;

  border-radius: 5px;
  margin: 5px;
  padding: 0 10px;
}

.control-item:hover {
  background-color: rgba(53, 52, 64, 0.6);
  cursor: pointer;
}

.control-item-icon {
  margin-right: 10px;
}

.space { flex-grow: 1; }
</style>
