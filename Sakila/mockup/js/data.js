// Mock Data for Sakila Movie Rental System

// Films Data
const films = [
    {
        film_id: 1,
        title: "Academy Dinosaur",
        description: "A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies",
        release_year: 2006,
        language: "English",
        rental_duration: 6,
        rental_rate: 0.99,
        length: 86,
        replacement_cost: 20.99,
        rating: "PG",
        categories: ["Documentary"],
        actors: ["PENELOPE GUINESS", "WARREN NOLTE", "OPRAH KILMER"]
    },
    {
        film_id: 2,
        title: "Ace Goldfinger",
        description: "A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China",
        release_year: 2006,
        language: "English",
        rental_duration: 3,
        rental_rate: 4.99,
        length: 48,
        replacement_cost: 12.99,
        rating: "G",
        categories: ["Action"],
        actors: ["BOB FAWCETT", "MINNIE KALLOCH", "SEAN WILLIAMS"]
    },
    {
        film_id: 3,
        title: "Adaptation Holes",
        description: "A Astounding Reflection of a Lumberjack And a Car who must Battle a Feminist in A MySQL Shop",
        release_year: 2006,
        language: "English",
        rental_duration: 7,
        rental_rate: 2.99,
        length: 50,
        replacement_cost: 18.99,
        rating: "NC-17",
        categories: ["Documentary"],
        actors: ["NICK WAHLBERG", "MARY KEITEL", "JON DEPP"]
    },
    {
        film_id: 4,
        title: "Affair Prejudice",
        description: "A Fanciful Documentary of a Frisbee And a Lumberjack who must Chase a Monkey in A Shark Tank",
        release_year: 2006,
        language: "English",
        rental_duration: 5,
        rental_rate: 2.99,
        length: 117,
        replacement_cost: 26.99,
        rating: "G",
        categories: ["Horror"],
        actors: ["JAYNE NOLTE", "OZZIE OSBOURNE", "ELVIS KALLOCH"]
    },
    {
        film_id: 5,
        title: "African Egg",
        description: "A Fast-Paced Documentary of a Pastry Chef And a Dentist who must Pursue a Forensic Psychologist in The Gulf of Mexico",
        release_year: 2006,
        language: "English",
        rental_duration: 6,
        rental_rate: 2.99,
        length: 130,
        replacement_cost: 22.99,
        rating: "PG",
        categories: ["Action"],
        actors: ["GARY PHOENIX", "JODIE DEGENERES", "BURT TEMPLE"]
    },
    {
        film_id: 6,
        title: "Agent Truman",
        description: "A Intense Panorama of a Robot And a Astronaut who must Battle a Student in A Jet Engine",
        release_year: 2006,
        language: "English",
        rental_duration: 3,
        rental_rate: 2.99,
        length: 179,
        replacement_cost: 17.99,
        rating: "PG-13",
        categories: ["Action", "Sci-Fi"],
        actors: ["KIRK JOVOVICH", "DAN HARRIS", "KELSEY HOUSTON"]
    },
    {
        film_id: 7,
        title: "Airplane Sierra",
        description: "A Touching Saga of a Hunter And a Butler who must Discover a Butler in A Jet Engine",
        release_year: 2006,
        language: "English",
        rental_duration: 6,
        rental_rate: 4.99,
        length: 62,
        replacement_cost: 28.99,
        rating: "PG-13",
        categories: ["Comedy"],
        actors: ["RIPLEY CRAWFORD", "LAURENCE BULLOCK", "PENELOPE PINKETT"]
    },
    {
        film_id: 8,
        title: "Airport Pollock",
        description: "A Epic Drama of a Student And a Secret Agent who must Meet a Cat in A MySQL Shop",
        release_year: 2006,
        language: "English",
        rental_duration: 6,
        rental_rate: 4.99,
        length: 54,
        replacement_cost: 15.99,
        rating: "R",
        categories: ["Action", "Drama"],
        actors: ["AL PACINO", "ANGELINA JOLIE", "NICK DEPP"]
    },
    {
        film_id: 9,
        title: "Aladdin Calendar",
        description: "A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China",
        release_year: 2006,
        language: "English",
        rental_duration: 6,
        rental_rate: 2.99,
        length: 63,
        replacement_cost: 24.99,
        rating: "NC-17",
        categories: ["Animation", "Comedy"],
        actors: ["CAMERON STREEP", "KEVIN GARLAND", "CARY MCCONAUGHEY"]
    },
    {
        film_id: 10,
        title: "Alamo Fever",
        description: "A Emotional Drama of a Student And a Secret Agent who must Challenge a Teacher in The Outback",
        release_year: 2006,
        language: "English",
        rental_duration: 5,
        rental_rate: 2.99,
        length: 124,
        replacement_cost: 14.99,
        rating: "PG",
        categories: ["Drama"],
        actors: ["MATTHEW CARREY", "SANDRA KILMER", "WOODY HOFFMAN"]
    }
];

// Categories Data
const categories = [
    "Action",
    "Animation",
    "Comedy",
    "Documentary",
    "Drama",
    "Horror",
    "Sci-Fi",
    "Thriller",
    "Western",
    "Family"
];

// Actors Data
const actors = [
    { actor_id: 1, first_name: "PENELOPE", last_name: "GUINESS", film_count: 19 },
    { actor_id: 2, first_name: "NICK", last_name: "WAHLBERG", film_count: 25 },
    { actor_id: 3, first_name: "ED", last_name: "CHASE", film_count: 26 },
    { actor_id: 4, first_name: "JENNIFER", last_name: "DAVIS", film_count: 22 },
    { actor_id: 5, first_name: "JOHNNY", last_name: "LOLLOBRIGIDA", film_count: 20 },
    { actor_id: 6, first_name: "BETTE", last_name: "NICHOLSON", film_count: 23 },
    { actor_id: 7, first_name: "GRACE", last_name: "MOSTEL", film_count: 24 },
    { actor_id: 8, first_name: "MATTHEW", last_name: "JOHANSSON", film_count: 21 },
    { actor_id: 9, first_name: "JOE", last_name: "SWANK", film_count: 27 },
    { actor_id: 10, first_name: "CHRISTIAN", last_name: "GABLE", film_count: 25 }
];

// Customers Data
const customers = [
    {
        customer_id: 1,
        first_name: "MARY",
        last_name: "SMITH",
        email: "mary.smith@sakilacustomer.org",
        active: true,
        rentals: 32
    },
    {
        customer_id: 2,
        first_name: "PATRICIA",
        last_name: "JOHNSON",
        email: "patricia.johnson@sakilacustomer.org",
        active: true,
        rentals: 27
    },
    {
        customer_id: 3,
        first_name: "LINDA",
        last_name: "WILLIAMS",
        email: "linda.williams@sakilacustomer.org",
        active: true,
        rentals: 21
    },
    {
        customer_id: 4,
        first_name: "BARBARA",
        last_name: "JONES",
        email: "barbara.jones@sakilacustomer.org",
        active: false,
        rentals: 15
    },
    {
        customer_id: 5,
        first_name: "ELIZABETH",
        last_name: "BROWN",
        email: "elizabeth.brown@sakilacustomer.org",
        active: true,
        rentals: 29
    }
];

// Stores Data
const stores = [
    {
        store_id: 1,
        address: "47 MySakila Drive",
        city: "Lethbridge",
        country: "Canada",
        manager: "Mike Hillyer"
    },
    {
        store_id: 2,
        address: "28 MySQL Boulevard",
        city: "Woodridge",
        country: "Australia",
        manager: "Jon Stephens"
    }
];

// Rating colors
const ratingColors = {
    "G": "#10b981",
    "PG": "#3b82f6",
    "PG-13": "#f59e0b",
    "R": "#ef4444",
    "NC-17": "#7c3aed"
};

// Helper function to get rating color
function getRatingColor(rating) {
    return ratingColors[rating] || "#64748b";
}

// Helper function to format currency
function formatCurrency(amount) {
    return "$" + amount.toFixed(2);
}

// Helper function to format duration
function formatDuration(minutes) {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
}
