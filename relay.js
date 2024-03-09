const ws = new WebSocket("wss://willhpayne-pvcc.github.io"); // WebSocket server URI

ws.onopen = function() {
  console.log("WebSocket connection established.");
};

ws.onmessage = function(event) {
  console.log("Received message:", event.data);
  // Here, you would implement logic to forward the message to the appropriate Python peer(s).
  // For simplicity, let's just display the message in the browser console.
};

function sendMessage(message) {
  ws.send(message);
}
