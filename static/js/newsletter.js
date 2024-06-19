
document.getElementById('newsletter-form').addEventListener('submit', function (event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('/newsletter/subscribe', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token for POST requests
        }
    })
        .then(response => {
            return response.json();
        })
        .then(data => {
            let errorText =document.getElementById('error-message');
            if (data.success) {
                errorText.innerText = data.success;
                errorText.style.color = 'green'
            } else {
                errorText = data.error;
                errorText.style.color = 'rgb(185,28,28)'
            }
        })
        .catch(error => {
            console.log('Error:', error);
            alert('There was an error subscribing. Please try again later.');
        });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}