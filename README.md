# Dance Improvisation Generator

A dance improvisation tool for Lindy Hop and Jazz dancers. Generate random movement prompts to inspire your practice sessions. Available in English and Italian.

## Live Demo

Try it online: [GitHub Pages Version](https://yourusername.github.io/) *(replace with your actual GitHub Pages URL)*

## Getting Started

### Web Version (Recommended)
The easiest way to use this tool is through the web interface - no installation required. Just visit the link above.

### Local Streamlit App
If you prefer to run it locally:
```bash
pip install streamlit
streamlit run app_streamlit.py
```
Then open `http://localhost:8501` in your browser.

### Command Line Interface
For command line usage:
```bash
python improvisation_cli.py --interactive
python improvisation_cli.py --language it --categories places emotions
```

## Project Structure

### Web Version
- `index.html` - Main web page
- `styles.css` - Styling  
- `script.js` - JavaScript functionality
- `GITHUB_PAGES_GUIDE.md` - Deployment guide

### Python Version
- `app_streamlit.py` - Streamlit web app
- `improvisation_cli.py` - Command line tool
- `requirements.txt` - Dependencies

## What It Does

This tool helps dancers practice improvisation by generating random combinations of:
- Spatial positions and movements
- Audience positioning
- Beat counts and timing
- Emotional expressions
- Body part focus

The database includes over 100 moves from Lindy Hop and Jazz dance styles.

## Usage

### Web Interface
1. Choose your language (English or Italian)
2. Select which categories to include in your prompt
3. Click generate to get a random combination
4. Use the prompt to inspire your movement

### Python Version
Install Python 3.7+ and the requirements, then run the Streamlit app. The interface works the same way as the web version.

## Deployment

To deploy your own copy on GitHub Pages, see the guide in `GITHUB_PAGES_GUIDE.md`.

Quick steps:
1. Fork this repository
2. Rename it to `yourusername.github.io`
3. Enable GitHub Pages in settings
4. Access at `https://yourusername.github.io/`

## Credits

Based on the original work by [Sergei Kaptelin](https://sergeikaptelin.github.io/improvisation-generator/)

Based on the original work by [Sergei Kaptelin](https://sergeikaptelin.github.io/improvisation-generator/)
