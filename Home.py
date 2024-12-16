import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="AQI Project", 
    page_icon="🌍", 
    layout="centered"
)

# Add a project title with emoji
st.title("🌍 Air Quality Index (AQI) Project")

# Add a subtitle or tagline
st.subheader("A Comprehensive Analysis of Air Quality Data Across Regions")

# Add an image or GIF for visual appeal
st.image(
    "https://www.environment.sa.gov.au/files/sharedassets/images/air_quality.jpg", 
    caption="Understanding the air we breathe.",
    use_column_width=True
)

# Add a brief description about the project
st.write("""
The **Air Quality Index (AQI)** Project is an interactive web application that provides insights into air quality 
levels across various regions. This app allows users to:
- Explore AQI data through charts and tables.
- Analyze trends and patterns in air quality.
- Predict AQI levels using machine learning models.

Built using **Streamlit**, this app ensures a user-friendly and visually engaging experience.
""")

# Add a call-to-action button
if st.button("Get Started 🚀"):
    st.write("Use the **sidebar** to navigate to different sections of the app!")

# Optional: Add additional visual elements like expander or metrics
with st.expander("Learn More About AQI"):
    st.write("""
    The Air Quality Index is a metric used globally to measure air pollution levels. 
    Understanding AQI helps in addressing environmental concerns and promoting better health practices.
    """)

# Add footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit | [GitHub Repository](https://github.com/your-repo-link)")
