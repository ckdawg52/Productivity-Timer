document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('timer-form');
    const status = document.getElementById('status');
    const progressBar = document.getElementById('progress-bar');
    const timeRemaining = document.getElementById('time-remaining');
    const animationArea = document.getElementById('animation-area');
    const bellSound = document.getElementById('bell-sound');

    let worker; // Web Worker instance
    let totalTime, intervalTime, countdownTimer;

    bellSound.volume = 1; // Default volume

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        totalTime = parseInt(document.getElementById('total-time').value) * 60 * 1000; // ms
        intervalTime = parseInt(document.getElementById('interval-time').value) * 60 * 1000; // ms

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
                startWorker();
            }
        }, 1000);
    }

    function startWorker() {
        if (window.Worker) {
            worker = new Worker('timer-worker.js'); // Assumes file is in root; adjust path if needed

            worker.onmessage = (event) => {
                if (event.data.type === 'update') {
                    updateProgress(event.data.remainingInterval, event.data.remainingTotal);
                } else if (event.data.type === 'alert') {
                    triggerAlert(event.data.text);
                }
            };

            worker.postMessage({
                action: 'start',
                intervalTime: intervalTime,
                totalTime: totalTime
            });
        } else {
            console.error('Web Workers not supported in this browser.');
            // Fallback: Use original throttled timer if needed
        }
    }

    function updateProgress(remainingInterval, remainingTotal) {
        remainingInterval = Math.max(0, remainingInterval);
        remainingTotal = Math.max(0, remainingTotal);

        const progress = ((intervalTime - remainingInterval) / intervalTime) * 100;
        progressBar.value = progress;
        timeRemaining.textContent = `Time left in interval: ${formatTime(remainingInterval / 1000)}`;
        status.textContent = `Total time left: ${formatTime(remainingTotal / 1000)}`;
    }

    function formatTime(seconds) {
        seconds = Math.max(0, Math.floor(seconds));
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

    function triggerAlert(text) {
        playSound(); // Plays custom sound if tab is active
        showAnimation(text, text === 'FOCUS!' ? 'wave-animation' : 'slide-animation');
        sendNotification(text); // Background-capable alert
        if (text === 'FINISHED!') status.textContent = 'Session Complete!';
    }

    // New: Send desktop notification (works in background)
    function sendNotification(text) {
        if (Notification.permission === 'granted') {
            new Notification('Productivity Timer', {
                body: text,
                icon: 'icon.png' // Optional: Upload an icon.png to your repo and reference it
            });
        } else if (Notification.permission !== 'denied') {
            Notification.requestPermission().then(permission => {
                if (permission === 'granted') {
                    new Notification('Productivity Timer', { body: text });
                }
            });
        }
    }
});

