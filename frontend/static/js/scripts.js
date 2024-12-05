// Wait for the DOM to load before running the scripts
document.addEventListener('DOMContentLoaded', function() {
    
    // ----- LOGIN FORM VALIDATION ----- //
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission for validation
            
            const username = document.getElementById('username');
            const password = document.getElementById('password');
            let valid = true;

            // Reset previous error messages
            resetLoginErrors();

            // Username validation
            if (username.value.trim() === '') {
                valid = false;
                showError(username, 'Please enter your username');
            }

            // Password validation
            if (password.value.trim() === '') {
                valid = false;
                showError(password, 'Please enter your password');
            } else if (password.value.length < 6) {
                valid = false;
                showError(password, 'Password must be at least 6 characters');
            }

            if (valid) {
                loginForm.submit(); // Submit the form if everything is valid
            }
        });
    }

    function showError(inputElement, message) {
        const errorMessage = document.createElement('span');
        errorMessage.classList.add('error-message');
        errorMessage.textContent = message;
        inputElement.parentElement.appendChild(errorMessage);
    }

    function resetLoginErrors() {
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.remove());
    }

    // ----- MESSAGING INTERFACE ----- //
    const messageForm = document.getElementById('message-form');
    
    if (messageForm) {
        messageForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const messageInput = document.getElementById('message-input');
            const messagesContainer = document.getElementById('messages-container');
            const messageContent = messageInput.value.trim();
            
            if (messageContent !== '') {
                // Create new message element
                const newMessage = document.createElement('div');
                newMessage.classList.add('message');
                newMessage.innerHTML = `
                    <div class="sender">Parent</div>
                    <div class="message-content">${messageContent}</div>
                `;
                messagesContainer.appendChild(newMessage);

                // Scroll to the bottom of the message container
                messagesContainer.scrollTop = messagesContainer.scrollHeight;

                // Clear the input field after sending
                messageInput.value = '';
            }
        });
    }

    // ----- SCHEDULING MEETING FORM ----- //
    const scheduleForm = document.getElementById('schedule-form');
    
    if (scheduleForm) {
        scheduleForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const meetingDate = document.getElementById('meeting-date');
            const meetingTime = document.getElementById('meeting-time');
            const parentName = document.getElementById('parent-name');
            const meetingContainer = document.getElementById('scheduled-meetings-container');

            if (meetingDate.value !== '' && meetingTime.value !== '' && parentName.value !== '') {
                // Create new meeting entry
                const newMeeting = document.createElement('div');
                newMeeting.classList.add('meeting');
                newMeeting.innerHTML = `
                    <div class="meeting-details">
                        <p><strong>Parent:</strong> ${parentName.value}</p>
                        <p><strong>Date:</strong> ${meetingDate.value}</p>
                        <p><strong>Time:</strong> ${meetingTime.value}</p>
                    </div>
                `;
                meetingContainer.appendChild(newMeeting);

                // Reset form fields after submission
                scheduleForm.reset();
            } else {
                alert('Please fill out all the fields before submitting.');
            }
        });
    }

    // ----- DASHBOARD CARDS - INTERACTIVE CARD (example for messages) ----- //
    const messageCard = document.getElementById('message-card');
    
    if (messageCard) {
        messageCard.addEventListener('click', function() {
            window.location.href = '/messaging'; // Navigate to the messaging page
        });
    }

    // ----- MOBILE NAVIGATION TOGGLE ----- //
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // ----- HIGHLIGHT ACTIVE NAV ITEM ----- //
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(item => item.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // ----- RESPONSIVE FORM STYLES ----- //
    const formElements = document.querySelectorAll('form input, form select');
    
    formElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.classList.add('focused');
        });
        element.addEventListener('blur', function() {
            this.classList.remove('focused');
        });
    });

});

// ----- Utility Functions ----- //

function toggleLoading(isLoading) {
    const loadingSpinner = document.getElementById('loading-spinner');
    if (isLoading) {
        loadingSpinner.style.display = 'block';
    } else {
        loadingSpinner.style.display = 'none';
    }
}
