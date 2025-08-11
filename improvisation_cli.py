#!/usr/bin/env python3
"""
Command-line version of the Improvisation Generator
Simple Python script that can be run without web interface
"""

import random
import argparse

# Same data as web versions
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
        "title": "🎭 DANCE IMPROVISATION GENERATOR",
        "moves": "🕺 MOVES",
        "places": "📍 SPACE POSITION", 
        "moving": "🏃 MOVEMENT",
        "positions": "👀 AUDIENCE POSITION",
        "counts": "🔢 COUNTS",
        "emotions": "😊 EMOTIONS",
        "organs": "🫀 BODY PARTS"
    },
    "it": {
        "title": "🎭 GENERATORE DI IMPROVVISAZIONE DANZA",
        "moves": "🕺 MOVIMENTI",
        "places": "📍 POSIZIONE NELLO SPAZIO",
        "moving": "🏃 MOVIMENTO",
        "positions": "👀 POSIZIONE VERSO IL PUBBLICO",
        "counts": "🔢 CONTEGGI",
        "emotions": "😊 EMOZIONI",
        "organs": "🫀 PARTI DEL CORPO"
    }
}

def generate_improvisation(language='en', include_categories=None):
    """
    Generate a random improvisation
    
    Args:
        language (str): 'en' or 'it'
        include_categories (list): List of categories to include
    
    Returns:
        dict: Generated improvisation
    """
    if include_categories is None:
        include_categories = ["places", "moving", "positions", "counts", "emotions", "organs"]
    
    categories = CATEGORIES[language]
    result = {
        "moves": random.sample(MOVES, 4)  # Always include 4 moves
    }
    
    for category in include_categories:
        if category in categories:
            if category == "moving":
                result[category] = random.sample(categories[category], 2)
            else:
                result[category] = random.sample(categories[category], 1)
    
    return result

def print_improvisation(result, language='en'):
    """Pretty print the improvisation result"""
    titles = TITLES[language]
    
    print("\n" + "="*50)
    print(titles["title"])
    print("="*50)
    
    # Always print moves first
    print(f"\n{titles['moves']}")
    for i, move in enumerate(result["moves"], 1):
        print(f"  {i}. {move}")
    
    # Print other categories
    category_order = ["places", "moving", "positions", "counts", "emotions", "organs"]
    for category in category_order:
        if category in result:
            print(f"\n{titles[category]}")
            for item in result[category]:
                print(f"  • {item}")
    
    print("\n" + "="*50)

def interactive_mode():
    """Interactive command-line interface"""
    print("🎭 Welcome to the Dance Improvisation Generator!")
    
    # Choose language
    while True:
        lang = input("\nChoose language (en/it): ").lower().strip()
        if lang in ['en', 'it']:
            break
        print("Please enter 'en' for English or 'it' for Italian")
    
    # Choose categories
    categories = CATEGORIES[lang]
    available_categories = list(categories.keys())
    
    print(f"\nAvailable categories:")
    for i, cat in enumerate(available_categories, 1):
        print(f"  {i}. {TITLES[lang][cat]}")
    
    print(f"\nSelect categories (1-{len(available_categories)}, separated by commas)")
    print("Or press Enter for all categories:")
    
    selection = input().strip()
    
    if not selection:
        selected_categories = available_categories
    else:
        try:
            indices = [int(x.strip()) - 1 for x in selection.split(',')]
            selected_categories = [available_categories[i] for i in indices if 0 <= i < len(available_categories)]
        except (ValueError, IndexError):
            print("Invalid selection, using all categories")
            selected_categories = available_categories
    
    # Generate and display
    result = generate_improvisation(lang, selected_categories)
    print_improvisation(result, lang)
    
    # Ask for another
    again = input("\nGenerate another? (y/n): ").lower().strip()
    if again.startswith('y'):
        interactive_mode()

def main():
    parser = argparse.ArgumentParser(description='Dance Improvisation Generator')
    parser.add_argument('--language', '-l', choices=['en', 'it'], default='en',
                        help='Language (en for English, it for Italian)')
    parser.add_argument('--categories', '-c', nargs='+', 
                        choices=['places', 'moving', 'positions', 'counts', 'emotions', 'organs'],
                        help='Categories to include')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Run in interactive mode')
    parser.add_argument('--count', '-n', type=int, default=1,
                        help='Number of improvisations to generate')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    else:
        for i in range(args.count):
            if args.count > 1:
                print(f"\n--- Improvisation #{i+1} ---")
            
            result = generate_improvisation(args.language, args.categories)
            print_improvisation(result, args.language)

if __name__ == "__main__":
    main()
