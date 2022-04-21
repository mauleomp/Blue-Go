
function login(){
    window.location.href = 'Login.html';
};

function signup(){
    window.location.href = 'SignUp.html';
};

function hover(){

};



// Notification
(async () => {

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
