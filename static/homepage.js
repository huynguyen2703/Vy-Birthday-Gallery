document.addEventListener("DOMContentLoaded", function () {
    let wishes = [
        "Hi Babi",
        "It's been 365 days growing with you",
        "You have grown up a lot",
        "Have become more beautiful than ever",
        "You have done so many amazing things",
        "I am very proud of you, babii",
        "I know, we have argued a lot",
        "And overcome a lot",
        "And I admire all of your effort in our love",
        "Today, you have grown a bit more",
        "Future coming closer a bit more",
        "But, I will be there for the high and low",
        "Yesterday, Today, and Tomorrow",
        "I was, I am, and I will",
        "Be there for you. ❤️",
        "I love you so much ❤️",
        "Happy Birthday and enjoy these moments, my babi 😇",
    ];

    let index = 0;

    function updateText() {
        if (index < wishes.length) {
            document.getElementById("birthday-text").innerHTML =
                "<span>" + wishes[index] + "</span>";
            index++;
            setTimeout(updateText, 10000);
        }
    }

    updateText();
});

let redirectUrl = "/Vy-Story.com";
if (redirectUrl) {
    setTimeout(function () {
        window.location.href = redirectUrl;
    }, 240000);
}
