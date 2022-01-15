export function humanReadableNumber(num) {
    if(num > 1000) {
        return (num/1000).toFixed(1) + 'K';
    } else {
        return num.toString();
    }
}

export function humanReadableElapsedHMS(elapsedSeconds) {
    if(elapsedSeconds < 0) { return '-' + humanReadableElapsedHMS(-elapsedSeconds); }

    let remainingSeconds = elapsedSeconds;

    const hours = Math.floor(remainingSeconds / 3600).toString();
    remainingSeconds -= hours * 3600;

    const minutes = Math.floor(remainingSeconds / 60).toString();
    remainingSeconds -= minutes * 60;

    const seconds = remainingSeconds.toString();

    return `${hours.padStart(2, '0')}:${minutes.padStart(2, '0')}:${seconds.padStart(2, '0')}`;
}