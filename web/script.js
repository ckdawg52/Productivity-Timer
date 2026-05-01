document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('timer-form');
    const status = document.getElementById('status');
    const progressBar = document.getElementById('progress-bar');
    const timeRemaining = document.getElementById('time-remaining');
    const animationArea = document.getElementById('animation-area');
    const bellSound = document.getElementById('bell-sound');

    let totalTime, intervalTime, remainingTotal, intervalTimer, countdownTimer;

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        totalTime = parseInt(document.getElementById('total-time').value) * 60; // seconds
        intervalTime = parseInt(document.getElementById('interval-time').value) * 60; // seconds
        remainingTotal = totalTime;

        status.textContent = 'Starting...';
        startCountdown(); // Mimic your 3-2-1 countdown
    });

    function startCountdown() {
        let count = 3;
        animationArea.textContent = count;
        animationArea.classList.add('slide-animation');
        countdownTimer = setInterval(() => {
            count--;
            if (count > 0) {
                animationArea.textContent = count;
            } else {
                clearInterval(countdownTimer);
                animationArea.textContent = '';
                animationArea.classList.remove('slide-animation');
                startInterval();
            }
        }, 1000);
    }

    function startInterval() {
        let remainingInterval = intervalTime;
        updateProgress(remainingInterval);
        intervalTimer = setInterval(() => {
            remainingInterval--;
            remainingTotal--;
            updateProgress(remainingInterval);

            if (remainingInterval <= 0) {
                clearInterval(intervalTimer);
                bellSound.play();
                showAnimation('FOCUS!', 'wave-animation'); // Reminder alert

                if (remainingTotal > 0) {
                    setTimeout(startInterval, 2000); // Short pause before next interval
                } else {
                    showAnimation('FINISHED!', 'slide-animation');
                    status.textContent = 'Session Complete!';
                }
            }
        }, 1000);
    }

    function updateProgress(remaining) {
        const progress = ((intervalTime - remaining) / intervalTime) * 100;
        progressBar.value = progress;
        timeRemaining.textContent = `Time left in interval: ${formatTime(remaining)}`;
        status.textContent = `Total time left: ${formatTime(remainingTotal)}`;
    }

    function formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    function showAnimation(text, animationClass) {
        animationArea.textContent = text;
        animationArea.classList.add(animationClass);
        setTimeout(() => {
            animationArea.textContent = '';
            animationArea.classList.remove(animationClass);
        }, 3000); // Show for 3 seconds
    }
});
