# Color Detection from Images

This project is a simple utility tool that detects the name and RGB value of any color in an uploaded image.

# Features
- Upload any image (JPG/PNG).
- Click anywhere on the image to detect the color.
- Display the closest color name and its RGB values.
- View the color visually with a filled reference box.

# Technologies Used
- Python
- Streamlit
- OpenCV
- Pandas

# How to Run
1. Clone this repository.
2. Install dependencies:
pip install -r requirements.txt
3. Run the app:
streamlit run app.py
# Note
Streamlit's image click detection is limited in the browser. For pixel-perfect interaction, run locally with OpenCV GUI support.

# License
MIT License
