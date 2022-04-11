
function login(){
    window.location.href = 'Login.html';
};

function signup(){
    window.location.href = 'SignUp.html';
};

function hover(){

};

function button_click() {
// Notification
    (async () => {
        // create and show the notification
        const showNotification = () => {
            // create a new notification
            const notification = new Notification('Blue&GO!', {
                //The body is the text that will go inside the notification
                icon: "{{ url_for('images', filename='logo.png') }}",
                body: 'Thank you for registering for Blue&GO'
            });

            // close the notification after 10 seconds
            setTimeout(() => {
                notification.close();
            }, 10 * 1000);

            // navigate to a URL when clicked
            notification.addEventListener('click', () => {

                window.open('http://127.0.0.1:5000/', '_blank');
            });
        }

        // show an error message
        const showError = () => {
            const error = document.querySelector('.error');
            error.style.display = 'block';
            error.textContent = 'You blocked the notifications';
        }

        // check notification permission
        let granted = false;

        if (Notification.permission === 'granted') {
            granted = true;
        } else if (Notification.permission !== 'denied') {
            let permission = await Notification.requestPermission();
            granted = permission === 'granted' ? true : false;
        }

        // show notification or error
        granted ? showNotification() : showError();

    })();

}

