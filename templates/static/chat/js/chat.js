function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var chatContainer = document.getElementById("chatContainer");

    if (messageInput.value !== "") {
        var newMessage = document.createElement("div");
        newMessage.className = "message";
        newMessage.textContent = messageInput.value;

        chatContainer.appendChild(newMessage);
        messageInput.value = "";
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
}