document.addEventListener("DOMContentLoaded", function () {
    var textBox = document.getElementById("text-box");

    var welcomeSpeech = [
        "Hi, there 🥳",
        "If you are Huy's Angel",
        "You are at the right place!",
        "I have been waiting for you.",
        "Click the button!",
        "You will enter a digital world created just for you!",
        "What are you waitin for..?",
        "Let's Go!😇",
    ];

    var index = 0;
    var originalWidth = 250;
    var originalHeight = 70;

    setInterval(function () {
        setTimeout(function () {
            // Set the content of the text box
            if (welcomeSpeech[index].length >= 30) {
                // Set the expanded size
                textBox.style.width = originalWidth + 50 + "px";
                textBox.style.height = originalHeight + 50 + "px";
            }

            textBox.textContent = welcomeSpeech[index];

            index++;
        }, 2500);

        textBox.style.width = originalWidth + "px";
        textBox.style.height = originalHeight + "px";
    }, 2500);
});
