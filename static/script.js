// async function sendMessage() {
//     const input = document.getElementById("user-input");
//     const message = input.value.trim();
//     if (!message) return;

//     const chatBox = document.getElementById("chat-box");
//     chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
//     input.value = "";

//     const response = await fetch('/chat', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({ message: message })
//     });

//     const data = await response.json();
//     chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
//     chatBox.scrollTop = chatBox.scrollHeight;
// }




// DOM Elements
// DOM Elements
// DOM Elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const typingIndicator = document.getElementById('typing-indicator');
const modeToggle = document.getElementById('mode-toggle');

// Enable send button on input
userInput.addEventListener('input', () => {
  sendBtn.disabled = userInput.value.trim() === '';
});

userInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  const mode = modeToggle.value;

  addMessage(message, 'user');
  userInput.value = '';
  sendBtn.disabled = true;
  showTypingIndicator();

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, mode })
    });

    const data = await response.json();

    setTimeout(() => {
      addMessage(data.reply, 'bot');
      hideTypingIndicator();
    }, 500);

  } catch (err) {
    addMessage("⚠️ Something went wrong!", 'bot');
    hideTypingIndicator();
  }
}

function addMessage(text, sender) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}-message`;

  const avatar = document.createElement('div');
  avatar.className = 'message-avatar';
  avatar.textContent = sender === 'user' ? '👤' : '🛡️';

  const content = document.createElement('div');
  content.className = 'message-content';
  const para = document.createElement('p');

  // Render markdown using marked (for bot messages)
  if (sender === 'bot') {
    para.innerHTML = marked.parse(text);
  } else {
    para.textContent = text;
  }

  content.appendChild(para);
  msgDiv.appendChild(avatar);
  msgDiv.appendChild(content);
  chatBox.appendChild(msgDiv);

  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
  typingIndicator.classList.add('show');
}

function hideTypingIndicator() {
  typingIndicator.classList.remove('show');
}

function quickMessage(msg) {
  userInput.value = msg;
  sendBtn.disabled = false;
  sendMessage();
}

function clearChat() {
  chatBox.innerHTML = `
    <div class="message bot-message">
      <div class="message-avatar">🛡️</div>
      <div class="message-content">
        <p>Hello! I'm your Insurance Assistant.</p>
        <p>Select a mode and type your query to begin.</p>
        <div class="quick-actions">
          <button class="quick-btn" onclick="quickMessage('Suggest a good policy for a 30-year-old')">🎯 Recommend Policy</button>
          <button class="quick-btn" onclick="quickMessage('Create a policy for a home insurance')">📝 Generate Document</button>
        </div>
      </div>
    </div>
  `;
}
