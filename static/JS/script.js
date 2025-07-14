document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.card');
    
    // Hover animasi tambahan (glow effect)
    cards.forEach(card => {
        card.addEventListener('mouseover', () => {
            card.style.boxShadow = '0 0 20px #00e1ff';
        });
        card.addEventListener('mouseout', () => {
            card.style.boxShadow = '0 4px 8px rgba(0,0,0,0.3)';
        });
    });

    // Optional: Animasi Fade In Page
    document.body.style.opacity = 0;
    document.body.style.transition = "opacity 0.7s ease-in";
    setTimeout(() => {
        document.body.style.opacity = 1;
    }, 100);
});

document.addEventListener("DOMContentLoaded", () => {
    // Fade effect untuk konten
    document.querySelectorAll('.card, .table-container').forEach(el => {
        el.style.opacity = 0;
        el.style.transition = 'opacity 1s ease';
        setTimeout(() => el.style.opacity = 1, 200);
    });
});

// Di script.js atau langsung dalam <script> tag di index.html
Chart.defaults.responsive = true;
Chart.defaults.maintainAspectRatio = false;