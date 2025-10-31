function updateClock() {
    const now = new Date();
    // Use .toLocaleTimeString() for a clean, localized time format
    const timeString = now.toLocaleTimeString(); 
    
    // Find the clock element and update its content
    document.getElementById('clock').textContent = timeString;
}

// Run the function immediately, then run it every 1000 milliseconds (1 second)
updateClock(); 
setInterval(updateClock, 1000);
