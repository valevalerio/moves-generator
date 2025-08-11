# Dance Improvisation Generator

A web-based tool for Lindy Hop and Jazz dancers to generate random movement prompts for improvisation practice. Features bilingual support (English/Italian) and multiple categories of dance elements.

## Try It Live

This is a fully functional web application. You can:
- Open `index.html` directly in your browser
- Or deploy it to GitHub Pages for online access

## Features

- **Random prompt generation** combining different dance elements
- **Bilingual interface** - switch between English and Italian
- **Multiple categories**: spatial positions, movement types, audience positioning, beat counts, emotions, and body parts
- **Extensive move database** with 100+ Lindy Hop and Jazz dance moves
- **Clean, responsive design** that works on desktop and mobile

## Using the Application

1. Open the web interface (locally or deployed)
2. Select your preferred language using the dropdown
3. Choose which categories to include in your prompts
4. Click "Generate" to get a random combination
5. Use the generated prompt to inspire your improvisation

## Files Overview

**Web Application:**
- `index.html` - Main application interface
- `script.js` - Core functionality and move database
- `styles.css` - Styling and responsive design

**Python Versions:**
- `app_streamlit.py` - Streamlit web app version
- `improvisation_cli.py` - Command-line interface
- `requirements.txt` - Python dependencies

**Documentation:**
- `GITHUB_PAGES_GUIDE.md` - Complete deployment instructions

## Local Development

### Web Version
Simply open `index.html` in any modern web browser. No server required.

### Python Version
```bash
pip install -r requirements.txt
streamlit run app_streamlit.py
```

### Command Line
```bash
python improvisation_cli.py --interactive
python improvisation_cli.py --language it --categories places emotions
```

## Deployment

Want to host this online? See the complete guide in `GITHUB_PAGES_GUIDE.md` for step-by-step instructions on deploying to GitHub Pages.

## Credits

Based on the original work by [Sergei Kaptelin](https://sergeikaptelin.github.io/improvisation-generator/)
