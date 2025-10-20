var luEl = document.getElementById('last-updated');
var luText = luEl.innerHTML;
var now = new Date();
var last_updated = new Date(luText);
var hours_ago = Math.round((now - last_updated) / 3.6e6);
var updatedText = hours_ago + ' hour' + ((hours_ago === 1) ? '' : 's') + ' ago';
luEl.innerHTML = updatedText;
