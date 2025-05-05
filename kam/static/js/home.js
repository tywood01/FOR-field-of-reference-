function installPrompt() {
    // Check if the browser supports service workers and show the install prompt
    if ("serviceWorker" in navigator) {
        navigator.serviceWorker
        .register("/serviceworker.js", { scope: "/" })
        .then((registration) => {
            registration.unregister().then((boolean) => {
            });
        })
        .catch((error) => {
            
        });
        // Befor install prompt start
        window.addEventListener('beforeinstallprompt', event => {
        event.preventDefault();
        var installDiv = document.getElementById('divInstallApp');
        installDiv.innerHTML = '<button id="installApp" class="btn btn-outline-secondary ms-1">Install App</button>';
        installDiv.addEventListener('click', () => {
            event.prompt();
            installDiv.innerHTML = ""
        });
        });
        // Before install prompt end
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Check if service worker is supported
    installPrompt();
});