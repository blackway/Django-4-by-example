// Main JavaScript for Sakila Home Page

document.addEventListener('DOMContentLoaded', function() {
    // Load featured films
    loadFeaturedFilms();

    // Setup search functionality
    setupSearch();
});

// Load featured films on home page
function loadFeaturedFilms() {
    const filmGrid = document.getElementById('featuredFilms');
    if (!filmGrid) return;

    // Display first 6 films as featured
    const featuredFilms = films.slice(0, 6);

    filmGrid.innerHTML = featuredFilms.map(film => createFilmCard(film)).join('');
}

// Create film card HTML
function createFilmCard(film) {
    const initials = film.title.split(' ').map(word => word[0]).join('').substring(0, 2);
    const ratingColor = getRatingColor(film.rating);

    return `
        <div class="film-card" onclick="showFilmDetail(${film.film_id})">
            <div class="film-poster">${initials}</div>
            <div class="film-info">
                <h3 class="film-title">${film.title}</h3>
                <div class="film-meta">
                    ${film.categories.map(cat => `<span class="film-badge">${cat}</span>`).join('')}
                </div>
                <p class="film-description">${film.description}</p>
                <div class="film-footer">
                    <span class="film-price">${formatCurrency(film.rental_rate)}</span>
                    <span class="film-rating" style="background-color: ${ratingColor}">${film.rating}</span>
                </div>
            </div>
        </div>
    `;
}

// Setup search functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');

    if (searchBtn && searchInput) {
        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
}

// Perform search
function performSearch() {
    const searchInput = document.getElementById('searchInput');
    const query = searchInput.value.trim();

    if (query) {
        // Redirect to films page with search query
        window.location.href = `films.html?search=${encodeURIComponent(query)}`;
    }
}

// Show film detail modal (placeholder)
function showFilmDetail(filmId) {
    // This will be implemented on the films page
    window.location.href = `films.html?id=${filmId}`;
}
