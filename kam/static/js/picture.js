function checkCameraSupport() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                const videoElement = document.getElementById('camera-stream');
                videoElement.srcObject = stream;
            })
            .catch(function(error) {
                console.error("Error accessing the camera", error);
            });
    } else {
        alert("Camera API not supported by this browser.");
    }
}

function captureImageAndSubmit() {
    const canvas = document.getElementById('image-capture');
    const context = canvas.getContext('2d');
    const video = document.getElementById('camera-stream');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageDataUrl = canvas.toDataURL('image/png');
    const imageInput = document.getElementById('id_image');
    imageInput.value = imageDataUrl;

    document.getElementById('picture-form').submit();
}

document.addEventListener("DOMContentLoaded", function() {
    // Check if the camera is supported
    checkCameraSupport();

    // Capture image and submit form
    document.getElementById('capture-button').addEventListener('click', function() {
        captureImageAndSubmit();
    });
});