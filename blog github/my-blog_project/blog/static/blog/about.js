document.addEventListener("DOMContentLoaded", function () {
    const dynamicWord = document.getElementById("dynamic-word");
    const words = ["Me", "Cloud", "DevOps"];
    let index = 0;

    setInterval(() => {
        // Kelimeyi değiştir
        index = (index + 1) % words.length;
        dynamicWord.textContent = words[index];

        // Animasyon sınıfını ekle ve sonra kaldır
        dynamicWord.classList.remove("robotic-animation");
        void dynamicWord.offsetWidth; // Tarayıcıyı yeniden çizdirerek animasyonu resetler
        dynamicWord.classList.add("robotic-animation");
    }, 3000); // Her 3 saniyede bir değiştir
});