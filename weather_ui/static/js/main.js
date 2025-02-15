document.addEventListener('DOMContentLoaded', function() {
    // Dark/Light mode toggle
    const modeToggle = document.querySelector('.switch');
    const body = document.body;

    modeToggle.addEventListener('click', function() {
        body.classList.toggle('light-mode');
        const icon = this.querySelector('i');
        if (icon.classList.contains('fa-moon')) {
            icon.classList.replace('fa-moon', 'fa-sun');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
        }
    });

    // Current time update
    function updateTime() {
        const timeElement = document.querySelector('.time');
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        timeElement.textContent = `${hours}:${minutes}`;
    }

    setInterval(updateTime, 1000);
    updateTime();
});
