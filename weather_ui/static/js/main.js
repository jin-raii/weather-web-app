document.addEventListener('DOMContentLoaded', function() {
    // Dark mode toggle
    const modeToggle = document.querySelector('.mode-toggle');
    const body = document.body;

    modeToggle.addEventListener('click', () => {
        body.classList.toggle('light-mode');
        const icon = modeToggle.querySelector('i');
        if (body.classList.contains('light-mode')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });

    // Search functionality
    const searchInput = document.querySelector('.search-bar input');
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            // for the searched city
            console.log('Searching for:', this.value);
        }
    });

    // Current location button
    // const locationBtn = document.querySelector('.location-btn');
    // locationBtn.addEventListener('click', () => {
    //     if (navigator.geolocation) {
    //         navigator.geolocation.getCurrentPosition(position => {
    //             const { latitude, longitude } = position.coords;
    //             // Here you would make an API call using these coordinates
    //             console.log('Location:', latitude, longitude);
    //         }, error => {
    //             console.error('Error getting location:', error);
    //         });
    //     }
    // });

    // Update time
    function updateTime() {
        const timeElement = document.querySelector('.time');
        const dateElement = document.querySelector('.date');
        const now = new Date();
        
        timeElement.textContent = now.toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit', 
            hour12: false 
        });
        
        dateElement.textContent = now.toLocaleDateString('en-US', { 
            weekday: 'long', 
            day: 'numeric', 
            month: 'short' 
        });
    }

    updateTime();
    setInterval(updateTime, 60000); // Update every minute
    
});



