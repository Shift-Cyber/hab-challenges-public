<template>
  <div class="modal" id="helpModal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Get Assistance</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div>
          <label for="username" style="margin-right:10px;">URL to Visit:</label>
          <input type="text" id="url" name="url" required>
        </div>
        <div>
          <label for="password" style="margin-right:10px;">Message:</label>
          <input type="text" id="message" name="message" required>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"
          @click="postMessage()">Submit</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelpModal',
  methods: {
    postMessage() {
      axios.post('/help_forum', {
        url: document.getElementById('url').value,
        message: document.getElementById('message').value,
      });
    },
  },
};
</script>
