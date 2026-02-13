// Films Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Get URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');
    const categoryFilter = urlParams.get('category');
    const filmId = urlParams.get('id');

    // Check if showing film detail
    if (filmId) {
        showFilmModal(parseInt(filmId));
    }

    // Set filter values from URL
    if (categoryFilter) {
        document.getElementById('categoryFilter').value = categoryFilter;
    }

    // Load films
    loadFilms();

    // Setup filter event listeners
    setupFilters();

    // Setup modal
    setupModal();
});

let currentPage = 1;
const itemsPerPage = 20;
let filteredFilms = [...films];

// Load films based on filters
function loadFilms() {
    const searchQuery = document.getElementById('searchInput').value.toLowerCase();
    const categoryFilter = document.getElementById('categoryFilter').value;
    const ratingFilter = document.getElementById('ratingFilter').value;
    const sortBy = document.getElementById('sortBy').value;

    // Apply filters
    filteredFilms = films.filter(film => {
        const matchesSearch = !searchQuery ||
            film.title.toLowerCase().includes(searchQuery) ||
            film.description.toLowerCase().includes(searchQuery) ||
            film.actors.some(actor => actor.toLowerCase().includes(searchQuery));

        const matchesCategory = !categoryFilter || film.categories.includes(categoryFilter);
        const matchesRating = !ratingFilter || film.rating === ratingFilter;

        return matchesSearch && matchesCategory && matchesRating;
    });

    // Apply sorting
    filteredFilms.sort((a, b) => {
        switch (sortBy) {
            case 'title':
                return a.title.localeCompare(b.title);
            case 'release_year':
                return b.release_year - a.release_year;
            case 'rental_rate':
                return a.rental_rate - b.rental_rate;
            case 'length':
                return a.length - b.length;
            default:
                return 0;
        }
    });

    // Reset to first page
    currentPage = 1;

    // Update display
    displayFilms();
    updatePagination();
}

// Display films for current page
function displayFilms() {
    const filmGrid = document.getElementById('filmGrid');
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const pageFilms = filteredFilms.slice(start, end);

    filmGrid.innerHTML = pageFilms.map(film => createFilmCard(film)).join('');

    // Update results count
    const resultsCount = document.getElementById('resultsCount');
    const totalResults = filteredFilms.length;
    const showingStart = start + 1;
    const showingEnd = Math.min(end, totalResults);
    resultsCount.textContent = `Showing ${showingStart}-${showingEnd} of ${totalResults} films`;
}

// Update pagination
function updatePagination() {
    const totalPages = Math.ceil(filteredFilms.length / itemsPerPage);
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const paginationNumbers = document.getElementById('paginationNumbers');

    // Enable/disable prev/next buttons
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage === totalPages || totalPages === 0;

    // Generate page numbers
    let numbersHTML = '';
    const maxVisible = 5;
    let startPage = Math.max(1, currentPage - Math.floor(maxVisible / 2));
    let endPage = Math.min(totalPages, startPage + maxVisible - 1);

    if (endPage - startPage < maxVisible - 1) {
        startPage = Math.max(1, endPage - maxVisible + 1);
    }

    for (let i = startPage; i <= endPage; i++) {
        const isActive = i === currentPage ? 'active' : '';
        numbersHTML += `<button class="pagination-number ${isActive}" onclick="goToPage(${i})">${i}</button>`;
    }

    paginationNumbers.innerHTML = numbersHTML;
}

// Go to specific page
function goToPage(page) {
    currentPage = page;
    displayFilms();
    updatePagination();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Setup filter event listeners
function setupFilters() {
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const ratingFilter = document.getElementById('ratingFilter');
    const sortBy = document.getElementById('sortBy');
    const searchBtn = document.getElementById('searchBtn');

    searchBtn.addEventListener('click', loadFilms);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            loadFilms();
        }
    });

    categoryFilter.addEventListener('change', loadFilms);
    ratingFilter.addEventListener('change', loadFilms);
    sortBy.addEventListener('change', loadFilms);

    // Pagination buttons
    document.getElementById('prevBtn').addEventListener('click', function() {
        if (currentPage > 1) {
            goToPage(currentPage - 1);
        }
    });

    document.getElementById('nextBtn').addEventListener('click', function() {
        const totalPages = Math.ceil(filteredFilms.length / itemsPerPage);
        if (currentPage < totalPages) {
            goToPage(currentPage + 1);
        }
    });
}

// Setup modal functionality
function setupModal() {
    const modal = document.getElementById('filmModal');
    const closeBtn = modal.querySelector('.close');

    closeBtn.addEventListener('click', function() {
        modal.classList.remove('show');
    });

    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
        }
    });
}

// Show film detail modal
function showFilmModal(filmId) {
    const film = films.find(f => f.film_id === filmId);
    if (!film) return;

    const modal = document.getElementById('filmModal');
    const modalContent = document.getElementById('filmModalContent');

    const initials = film.title.split(' ').map(word => word[0]).join('').substring(0, 2);
    const ratingColor = getRatingColor(film.rating);

    modalContent.innerHTML = `
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="
                width: 200px;
                height: 200px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: inline-flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 5rem;
                border-radius: 1rem;
                margin-bottom: 1rem;
            ">${initials}</div>
            <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">${film.title}</h2>
            <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
                ${film.categories.map(cat => `<span class="film-badge">${cat}</span>`).join('')}
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
            <div>
                <strong>Release Year:</strong> ${film.release_year}
            </div>
            <div>
                <strong>Language:</strong> ${film.language}
            </div>
            <div>
                <strong>Duration:</strong> ${formatDuration(film.length)}
            </div>
            <div>
                <strong>Rating:</strong>
                <span class="film-rating" style="background-color: ${ratingColor}; margin-left: 0.5rem;">${film.rating}</span>
            </div>
            <div>
                <strong>Rental Duration:</strong> ${film.rental_duration} days
            </div>
            <div>
                <strong>Rental Rate:</strong> <span style="color: var(--primary-color); font-weight: 700;">${formatCurrency(film.rental_rate)}</span>
            </div>
        </div>

        <div style="margin-bottom: 2rem;">
            <h3 style="margin-bottom: 0.5rem;">Description</h3>
            <p style="color: var(--text-secondary); line-height: 1.8;">${film.description}</p>
        </div>

        <div style="margin-bottom: 2rem;">
            <h3 style="margin-bottom: 0.5rem;">Cast</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                ${film.actors.map(actor => `<span class="film-badge">${actor}</span>`).join('')}
            </div>
        </div>

        <div style="text-align: center;">
            <button style="
                padding: 0.75rem 2rem;
                background-color: var(--primary-color);
                color: white;
                border: none;
                border-radius: 0.5rem;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
            " onmouseover="this.style.backgroundColor='var(--primary-hover)'" onmouseout="this.style.backgroundColor='var(--primary-color)'">
                Rent Now
            </button>
        </div>
    `;

    modal.classList.add('show');
}

// Reuse createFilmCard from main.js
function createFilmCard(film) {
    const initials = film.title.split(' ').map(word => word[0]).join('').substring(0, 2);
    const ratingColor = getRatingColor(film.rating);

    return `
        <div class="film-card" onclick="showFilmModal(${film.film_id})">
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
