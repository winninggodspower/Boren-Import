/*
Variables
currentUserEmail, isUserStaff, staticUrl, csrfToken
are being set from django templates
*/

document.addEventListener('DOMContentLoaded', function() {
    // Handle opening and closing chat rooms
    document.querySelectorAll('[data-accordion-target]').forEach(button => {
        button.addEventListener('click', function() {
            const chatContainerId = this.getAttribute('data-accordion-target');
            const chatContainer = document.querySelector(chatContainerId);
            
            if (chatContainer.classList.contains('hidden') && !chatContainer.dataset.hasFetched) {
                const chatId = chatContainerId.split('-').pop();
                
                console.log('is fetching');
                
                // Fetch messages
                fetch(`/service_enquiry/fetch_messages/${chatId}/`)
                    .then(response => response.json())
                    .then(data => {
                        const messages = data.messages;
                        const chatBox = chatContainer.querySelector('.overflow-y-auto');
                        chatBox.innerHTML = '';
                        
                        messages.forEach(msg => {
                            addChatBuble(msg, chatBox);
                        });

                        chatContainer.classList.remove('hidden');
                    });

                console.log('is streaming');
                
                // Set up EventSource for real-time updates
                const eventSource = new EventSource(`/service_enquiry/stream_messages/${chatId}/`);
                eventSource.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    const chatBox = chatContainer.querySelector('.overflow-y-auto');
                    addChatBuble(data, chatBox);
                };

                chatContainer.dataset.hasFetched = true;

            } 
        });
    });

    // Handle sending messages
    const chatForms = document.querySelectorAll('[id^="chat-form-"]');
    chatForms.forEach(chatForm => {

        chatForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const chatId = chatForm.id.replace('chat-form-', '');
            const messageInput = document.getElementById(`message-input-${chatId}`);
            const content = messageInput.value.trim();

            if (content.trim()) {
                fetch(`/service_enquiry/send_message/${chatId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ content })
                }).then(response => {
                    if (response.status === 204) {
                        messageInput.value = '';
                    }
                });
            }
        });
    });
});



function addChatBuble(msg, chatBox) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('flex', 'items-start', 'gap-3');

    let isUserMessage = msg.sender === currentUserEmail || (msg.sender_is_staff && isUserStaff)
    
    
    if (isUserMessage) {
        messageDiv.classList.add('justify-end');
    }

    let avatar = `
        <span class="relative flex shrink-0 overflow-hidden rounded-full w-8 h-8">
            <img class="aspect-square h-full w-full" alt="User Avatar" src="${staticUrl}assets/placeholder-user.jpg" />
        </span>`;

    let messageContent = `
        <div class="${isUserMessage ? 'bg-primary text-white' : 'bg-muted'} px-3 py-2 rounded-lg max-w-[70%]">
            <p>${msg.content}</p>
        </div>`;

    if (isUserMessage) {
        messageDiv.innerHTML = `${messageContent}${avatar}`;
    } else {
        messageDiv.innerHTML = `${avatar}${messageContent}`;
    }
    
    chatBox.appendChild(messageDiv);
}