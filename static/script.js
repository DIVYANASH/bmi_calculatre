const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const target = parseFloat(counter.dataset.value);

    let current = 0;

    const duration = 1200;
    const startTime = performance.now();

    function updateNumber(time) {

        const progress = Math.min(
            (time - startTime) / duration, 1
        );

        current = target * progress;

        counter.textContent = Number.isInteger(target)
            ? Math.round(current)
            : current.toFixed(2);

        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        }
    }

    requestAnimationFrame(updateNumber);

});


// Animate BMI progress bar

const progressBar = document.getElementById("bmiProgress");

if (progressBar) {

    const bmiElement = document.querySelector(".bmi-box h1");

    const bmi = parseFloat(bmiElement.dataset.value ||
                            bmiElement.textContent);

    const percentage = Math.min((bmi / 40) * 100, 100);

    setTimeout(() => {
        progressBar.style.width = percentage + "%";
    }, 200);

}