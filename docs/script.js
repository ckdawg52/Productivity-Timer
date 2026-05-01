document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('timer-form');
    const status = document.getElementById('status');
    const progressBar = document.getElementById('progress-bar');
    const timeRemaining = document.getElementById('time-remaining');
    const animationArea = document.getElementById('animation-area');
    const bellSound = document.getElementById('bell-sound');

    let totalTime, intervalTime, startTime, intervalStartTime, intervalTimer, countdownTimer;
    let isTabActive = true; // Track tab visibility

    bellSound.volume = 1; // Default volume

    // Listen for tab visibility changes to correct timer
    document.addEventListener('visibilitychange', () => {
        isTabActive = !document.hidden;
        if (isTabActive && intervalStartTime) {
            correctTimer(); // Adjust for any lost time when tab becomes active
        }
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        totalTime = parseInt(document.getElementById('total-time').value) * 60 * 1000; // milliseconds
        intervalTime = parseInt(document.getElementById('interval-time').value) * 60 * 1000; // milliseconds
        startTime = performance.now(); // High-precision start time
        intervalStartTime = startTime;

        status.textContent = 'Starting...';
        startCountdown();
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
        updateProgress();
        intervalTimer = setInterval(() => {
            if (isTabActive) {
                updateProgress();
                if (getElapsedInterval() >= intervalTime) {
                    clearInterval(intervalTimer);
                    triggerAlert('FOCUS!'); // Reminder alert

                    if (getElapsedTotal() < totalTime) {
                        intervalStartTime = performance.now(); // Reset for next interval
                        setTimeout(startInterval, 2000);
                    } else {
                        triggerAlert('FINISHED!');
                        status.textContent = 'Session Complete!';
                    }
                }
            }
        }, 1000); // Check every second when active
    }

    // Get precise elapsed time for interval and total
    function getElapsedInterval() {
        return performance.now() - intervalStartTime;
    }

    function getElapsedTotal() {
        return performance.now() - startTime;
    }

    // Correct timer if tab was inactive
    function correctTimer() {
        const elapsedInterval = getElapsedInterval();
        if (elapsedInterval >= intervalTime) {
            triggerAlert('FOCUS!'); // Fire any missed alerts
            intervalStartTime = performance.now() - (elapsedInterval - intervalTime); // Adjust start time
            if (getElapsedTotal() >= totalTime) {
                triggerAlert('FINISHED!');
                clearInterval(intervalTimer);
            }
        }
        updateProgress();
    }

    function updateProgress() {
        let elapsedInterval = getElapsedInterval();
        let elapsedTotal = getElapsedTotal();

        // Cap elapsed times to prevent negative remaining values
        elapsedInterval = Math.min(elapsedInterval, intervalTime);
        elapsedTotal = Math.min(elapsedTotal, totalTime);

        const remainingInterval = intervalTime - elapsedInterval;
        const remainingTotal = totalTime - elapsedTotal;

        const progress = (elapsedInterval / intervalTime) * 100;
        progressBar.value = progress;
        timeRemaining.textContent = `Time left in interval: ${formatTime(remainingInterval / 1000)}`;
        status.textContent = `Total time left: ${formatTime(remainingTotal / 1000)}`;
    }

    function formatTime(seconds) {
        seconds = Math.max(0, Math.floor(seconds)); // Prevent negative
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
        }, 3000);
    }

    function playSound() {
        bellSound.play().catch(error => console.error('Audio playback failed:', error));
    }

    // Centralized alert trigger (sound + animation)
    function triggerAlert(text) {
        playSound();
        showAnimation(text, text === 'FOCUS!' ? 'wave-animation' : 'slide-animation');
    }
});

