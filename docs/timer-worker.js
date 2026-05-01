let intervalTime, totalTime, intervalStartTime, startTime;
let timerInterval;

self.onmessage = (event) => {
    if (event.data.action === 'start') {
        intervalTime = event.data.intervalTime;
        totalTime = event.data.totalTime;
        startTime = performance.now();
        intervalStartTime = startTime;

        timerInterval = setInterval(() => {
            const elapsedInterval = performance.now() - intervalStartTime;
            const elapsedTotal = performance.now() - startTime;

            self.postMessage({
                type: 'update',
                remainingInterval: intervalTime - elapsedInterval,
                remainingTotal: totalTime - elapsedTotal
            });

            if (elapsedInterval >= intervalTime) {
                self.postMessage({ type: 'alert', text: 'FOCUS!' });
                intervalStartTime = performance.now(); // Reset for next interval

                if (elapsedTotal >= totalTime) {
                    self.postMessage({ type: 'alert', text: 'FINISHED!' });
                    clearInterval(timerInterval);
                }
            }
        }, 1000); // Accurate even in background
    } else if (event.data.action === 'stop') {
        clearInterval(timerInterval);
    }
};
