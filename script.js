// Dance Improvisation Generator JavaScript

// Data - Dance moves and categories (converted from Python)
const MOVES = [
    "Apple Jack", "Around the World", "Bee's Knees", "Ball Change", "Birds", 
    "Black Bottom", "Boogie Back", "Boogie Forward", "Boogie Drop", "Box Step",
    "Boogie Step", "Brake a Leg", "Breeze Knees", "Bunny Hop", "Cake Walk",
    "Camel Walk", "Charleston 20th", "Chase", "Chase more", "Corkscrew",
    "Crawls", "Crazy Legs (Rebel Legs, Rubber Legs)", "Cross Kicks (Run on the Log)",
    "Crossover", "Cow tail (Cartwheel)", "Duck Walk", "Drunken Sailor",
    "Eagle Slide", "Fall of the Log", "Fish Tail", "Flying Charleston",
    "Gaze Afar", "Golubec", "Grapevine", "Halliluya", "Half Break",
    "Hangman", "Happy Feet", "Helicopter Kicks (Hop Around)", "Heels",
    "Heels Click", "Hips Grinding", "Hitch Hiker", "Hot Potatoes",
    "Inside the Leg", "Itches", "Jig Walks", "Jumps", "Jump Kick Slide (from Big Apple)",
    "Jump Charleston (Jam Charleston)", "Jump Toe", "Jump Toe Kick Step",
    "Kicks", "Knee Slaps", "Knee Rocks", "Lockstep front (Cross Turn)",
    "Lockstep Back", "London Bridge", "Lowdown (Funky Butt)", "Mambo Step",
    "Messaround", "Moonslide", "Opposites", "Over the Top (Ankle Step)",
    "Paddle Turn", "Pecking (Pecks)", "Pimp Walk", "Pivots (Pivot Step, Strutting with inside Turn)",
    "Poni Walk", "Pushes", "Ride the Pony", "Rocks (Halliluya Rocks, Saxophone)",
    "Ronds", "Run run", "Rusty Dusty", "Sailor Kicks", "Savoy Kicks",
    "Scarecrow", "Scissors", "Shim Sham Break", "Shim Sham Step (Big Apple Stomp)",
    "Skating", "Shish-ka-boom-ba", "Shish-ka-boom-ba II (step hop step clap clap clap)",
    "Shoe Shine", "Shorty George", "Shorty George one leg", "Skips",
    "Slides", "Slip Slop", "Snake Hips (Mooche)", "Shimmy", "Spank the Baby",
    "Stomps", "Stomp Off", "Suzie Q", "Squat Charleston", "Sweep Charleston",
    "Tabby the Cat", "Tackie Annie", "Tic Tocs", "Tracking", "Travelling Charleston",
    "Trip over", "Triple Steps", "Turkey Trots", "Twists"
];

// Multilingual data
const CATEGORIES = {
    "en": {
        "places": ["High", "Low", "Wide", "Collected", "Bouncy", "Smooth"],
        "moving": ["Forward-backward", "Right-left", "In place", "Rotating", "Circle", "Diagonal", "Zigzag", "Triangle", "Square"],
        "positions": ["Front facing", "Profile", "Diagonal", "Back", "Constantly changing"],
        "counts": ["8", "4", "2", "1", "3", "5", "7", "6"],
        "emotions": ["Joy", "Playfulness", "Fatigue", "Seduction", "Ecstasy", "Fear", "Uncertainty"],
        "organs": ["Head", "Arms", "Wrists", "Shoulders", "Hips", "Feet", "Torso"]
    },
    "it": {
        "places": ["Alto", "Basso", "Largo", "Raccolto", "Rimbalzante", "Fluido"],
        "moving": ["Avanti-indietro", "Destra-sinistra", "Sul posto", "Ruotando", "Cerchio", "Diagonale", "Zigzag", "Triangolo", "Quadrato"],
        "positions": ["Frontale", "Profilo", "Diagonale", "Schiena", "Cambia continuamente"],
        "counts": ["8", "4", "2", "1", "3", "5", "7", "6"],
        "emotions": ["Gioia", "Giocosità", "Stanchezza", "Seduzione", "Estasi", "Paura", "Incertezza"],
        "organs": ["Testa", "Braccia", "Polsi", "Spalle", "Fianchi", "Piedi", "Busto"]
    }
};

const TITLES = {
    "en": {
        "title": "🎭 Improvisation Generator",
        "subtitle": "Generate random combinations for dance improvisation",
        "language": "Language",
        "categories": "Categories to include:",
        "generate": "🎲 Generate Random Improvisation",
        "result": "Your Improvisation:",
        "moves": "🕺 Moves",
        "places": "Space Position", 
        "moving": "Movement",
        "positions": "Audience Position",
        "counts": "Counts",
        "emotions": "Emotions",
        "organs": "Body Parts",
        "warning": "Please select at least one category!"
    },
    "it": {
        "title": "🎭 Generatore di Improvvisazione",
        "subtitle": "Genera combinazioni casuali per l'improvvisazione di danza",
        "language": "Lingua",
        "categories": "Categorie da includere:",
        "generate": "🎲 Genera Improvvisazione Casuale",
        "result": "La Tua Improvvisazione:",
        "moves": "🕺 Movimenti",
        "places": "Posizione nello Spazio",
        "moving": "Movimento",
        "positions": "Posizione verso il Pubblico",
        "counts": "Conteggi",
        "emotions": "Emozioni",
        "organs": "Parti del Corpo",
        "warning": "Seleziona almeno una categoria!"
    }
};

// Current language
let currentLanguage = 'en';

// Utility functions
function getRandomSample(array, count) {
    const shuffled = [...array].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}

function generateImprovisation(language, selectedCategories) {
    const categories = CATEGORIES[language];
    
    const result = {
        moves: getRandomSample(MOVES, 4) // Always include 4 moves
    };
    
    selectedCategories.forEach(category => {
        if (categories[category]) {
            if (category === 'moving') {
                result[category] = getRandomSample(categories[category], 2);
            } else {
                result[category] = getRandomSample(categories[category], 1);
            }
        }
    });
    
    return result;
}

function updateLanguage(language) {
    currentLanguage = language;
    const titles = TITLES[language];
    
    // Update page title and subtitle
    document.getElementById('main-title').textContent = titles.title;
    document.getElementById('subtitle').textContent = titles.subtitle;
    
    // Update categories title
    document.getElementById('categories-title').textContent = titles.categories;
    
    // Update category labels
    document.getElementById('places-label').textContent = titles.places;
    document.getElementById('moving-label').textContent = titles.moving;
    document.getElementById('positions-label').textContent = titles.positions;
    document.getElementById('counts-label').textContent = titles.counts;
    document.getElementById('emotions-label').textContent = titles.emotions;
    document.getElementById('organs-label').textContent = titles.organs;
    
    // Update generate button
    document.getElementById('generate-btn').textContent = titles.generate;
    
    // Update results title if visible
    const resultsTitle = document.getElementById('results-title');
    if (resultsTitle) {
        resultsTitle.textContent = titles.result;
    }
    
    // Update warning text
    document.getElementById('warning').textContent = titles.warning;
    
    // Clear results when language changes
    document.getElementById('results').style.display = 'none';
}

function displayResults(result, language) {
    const titles = TITLES[language];
    const resultsDiv = document.getElementById('results');
    const resultsContent = document.getElementById('results-content');
    const placeholderDiv = document.getElementById('placeholder');
    
    // Hide placeholder and show results
    if (placeholderDiv) placeholderDiv.style.display = 'none';
    
    // Clear previous results
    resultsContent.innerHTML = '';
    
    // Create moves section (first column)
    const movesDiv = document.createElement('div');
    movesDiv.className = 'moves-category';
    movesDiv.innerHTML = `
        <h3>${titles.moves}</h3>
        <ul class="result-list moves-list">
            ${result.moves.map(move => `<li><strong>${move}</strong></li>`).join('')}
        </ul>
    `;
    resultsContent.appendChild(movesDiv);
    
    // Create traits grid (columns 2 and 3)
    const traitsGrid = document.createElement('div');
    traitsGrid.className = 'traits-grid';
    
    // Show other categories in traits grid
    const categoryOrder = ['places', 'moving', 'positions', 'counts', 'emotions', 'organs'];
    
    categoryOrder.forEach(category => {
        if (result[category]) {
            const categoryDiv = document.createElement('div');
            categoryDiv.className = 'result-category';
            categoryDiv.innerHTML = `
                <h3>${titles[category]}</h3>
                <ul class="result-list">
                    ${result[category].map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
            traitsGrid.appendChild(categoryDiv);
        }
    });
    
    resultsContent.appendChild(traitsGrid);
    
    // Show results
    resultsDiv.style.display = 'block';
}

function getSelectedCategories() {
    const categories = ['places', 'moving', 'positions', 'counts', 'emotions', 'organs'];
    return categories.filter(category => {
        const checkbox = document.getElementById(category);
        return checkbox && checkbox.checked;
    });
}

function showWarning() {
    const warningDiv = document.getElementById('warning');
    const placeholderDiv = document.getElementById('placeholder');
    const resultsDiv = document.getElementById('results');
    
    // Hide results and placeholder, show warning
    if (placeholderDiv) placeholderDiv.style.display = 'none';
    resultsDiv.style.display = 'none';
    warningDiv.style.display = 'block';
    
    // Hide warning after 3 seconds and show placeholder
    setTimeout(() => {
        warningDiv.style.display = 'none';
        if (placeholderDiv) placeholderDiv.style.display = 'flex';
    }, 3000);
}

function hideWarning() {
    document.getElementById('warning').style.display = 'none';
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Language selector
    const languageSelect = document.getElementById('language-select');
    languageSelect.addEventListener('change', function() {
        updateLanguage(this.value);
    });
    
    // Generate button
    const generateBtn = document.getElementById('generate-btn');
    generateBtn.addEventListener('click', function() {
        const selectedCategories = getSelectedCategories();
        
        if (selectedCategories.length === 0) {
            showWarning();
            document.getElementById('results').style.display = 'none';
            return;
        }
        
        hideWarning();
        const result = generateImprovisation(currentLanguage, selectedCategories);
        displayResults(result, currentLanguage);
    });
    
    // Initialize with default language
    updateLanguage('en');
});

// Add some visual feedback for button clicks
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    
    generateBtn.addEventListener('click', function() {
        // Add loading effect
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
    });
});
