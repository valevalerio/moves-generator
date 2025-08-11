import streamlit as st
import random

# Data - Dance moves and categories
MOVES = [
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
]

# Multilingual data
CATEGORIES = {
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
}

TITLES = {
    "en": {
        "title": "Improvisation Generator",
        "subtitle": "Generate random combinations for dance improvisation",
        "language": "Language",
        "categories": "Categories to include:",
        "generate": "🎲 Generate Random Improvisation",
        "result": "Your Improvisation:",
        "moves": "Moves",
        "places": "Space Position", 
        "moving": "Movement",
        "positions": "Audience Position",
        "counts": "Counts",
        "emotions": "Emotions",
        "organs": "Body Parts"
    },
    "it": {
        "title": "Generatore di Improvvisazione",
        "subtitle": "Genera combinazioni casuali per l'improvvisazione di danza",
        "language": "Lingua",
        "categories": "Categorie da includere:",
        "generate": "🎲 Genera Improvvisazione Casuale",
        "result": "La Tua Improvvisazione:",
        "moves": "Movimenti",
        "places": "Posizione nello Spazio",
        "moving": "Movimento",
        "positions": "Posizione verso il Pubblico",
        "counts": "Conteggi",
        "emotions": "Emozioni",
        "organs": "Parti del Corpo"
    }
}

def generate_improvisation(language, selected_categories):
    """Generate random improvisation based on selected categories"""
    categories = CATEGORIES[language]
    
    result = {
        "moves": random.sample(MOVES, 4)  # Always include 4 moves
    }
    
    for category in selected_categories:
        if category in categories:
            if category == "moving":
                result[category] = random.sample(categories[category], 2)
            else:
                result[category] = random.sample(categories[category], 1)
    
    return result

def main():
    # Page config
    st.set_page_config(
        page_title="Improvisation Generator",
        page_icon="💃", # or better the dancer emoji: 💃
        layout="wide"
    )
    
    # Language selection
    col1, col2 = st.columns([3, 1])
    with col2:
        language = st.selectbox("🌐", ["en", "it"], format_func=lambda x: "English" if x == "en" else "Italiano")
    
    # Get translations
    t = TITLES[language]
    categories = CATEGORIES[language]
    
    # Title
    st.title(t["title"])
    st.markdown(f"*{t['subtitle']}*")
    st.markdown("---")
    
    # Sidebar for category selection
    with st.sidebar:
        st.header(t["categories"])
        
        selected_categories = []
        category_keys = ["places", "moving", "positions", "counts", "emotions", "organs"]
        
        for key in category_keys:
            if st.checkbox(t[key], value=True, key=key):
                selected_categories.append(key)
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button(t["generate"], type="primary", use_container_width=True):
            if selected_categories:
                # Generate improvisation
                result = generate_improvisation(language, selected_categories)
                
                # Display results
                st.markdown(f"## {t['result']}")
                
                # Always show moves first
                st.markdown(f"### 🕺 {t['moves']}")
                for i, move in enumerate(result["moves"], 1):
                    st.markdown(f"{i}. **{move}**")
                
                # Show other selected categories
                for category in selected_categories:
                    if category in result:
                        st.markdown(f"### {t[category]}")
                        for item in result[category]:
                            st.markdown(f"• {item}")
            else:
                st.warning("Please select at least one category!" if language == "en" else "Seleziona almeno una categoria!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "🎭 Dance Improvisation Generator | "
        "Built with Streamlit & Python ❤️"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
