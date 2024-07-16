import streamlit as st

def main():
    st.set_page_config(
        page_title="Portfolio", page_icon=":briefcase:", layout="wide"
    )

    st.markdown(
        """
        <style>
            body {
                color: #f0f8ff; /* AliceWhite */
                background-color: #000000; /* Black */
            }
            .header {
                background-color: #FFA500; /* Orange */
                padding: 20px 10%;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo {
                color: #f0f8ff; /* AliceWhite */
                font-size: 24px;
                font-weight: bold;
                text-decoration: none;
            }
            .navbar a {
                color: #f0f8ff; /* AliceWhite */
                font-size: 18px;
                font-weight: bold;
                text-decoration: none;
                margin-left: 20px;
                padding-bottom: 5px;
                border-bottom: 2px solid transparent;
                transition: border-bottom-color 0.3s;
            }
            .navbar a:hover {
                border-bottom-color: #FFA500; /* Orange */
            }
            .section {
                padding: 50px 10%;
                background-color: #000000; /* Black */
            }
            .section h2 {
                color: #FFA500; /* Orange */
                font-size: 36px;
                margin-bottom: 30px;
            }
            .section p, .section ul {
                color: #f0f8ff; /* AliceWhite */
                font-size: 20px;
                line-height: 1.5;
            }
            .contact {
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin-top: 50px;
            }
            .contact a {
                color: #FFA500; /* Orange */
                font-size: 20px;
                text-decoration: none;
            }
            .contact a:hover {
                color: #ffd700; /* Gold */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <header class="header">
            <a href="#home" class="logo">Portfolio</a>
            <nav class="navbar">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#certifications">Certifications</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </nav>
        </header>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="home" class="section">
            <div class="home-content">
                <h3>Hello, It's Me</h3>
                <h1>Kishan Kumar S</h1>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="about" class="section">
            <h2>About</h2>
            <p>Aspiring Data Learning Scientist. Passionate about leveraging the power of data to drive meaningful insights
            and innovations. Proficient in Python, C, C++, Java, with a strong foundation in data science principles.
            Currently honing skills in machine learning algorithms, I am on a journey to contribute to cutting-edge
            advancements in artificial intelligence. Excited about the intersection of technology and problem-solving, I
            thrive on challenges that require creative solutions.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="skills" class="section">
            <h2>Skills</h2>
            <ul>
                <li>Data Analysis</li>
                <li>Prompt Engineering</li>
                <li>Data Visualization</li>
                <li>Machine Learning</li>
                <li>Programming</li>
                <li>Problem Solving</li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="certifications" class="section">
            <h2>Certifications</h2>
            <ul>
                <li>Python for Data Science - IBM</li>
                <li>Data Analysis Using Python - IBM</li>
                <li>Data Science Foundations - Level 1 - IBM</li>
                <li>Predictions: Regression for Car Mileage and Diamond Price - IBM</li>
                <li>Customer Clustering With KMeans to Boost Business Strategy - IBM</li>
                <li>Data Visualization Using Python - IBM</li>
                <li>Applied Data Science with Python - Level 2 - IBM</li>
                <li>Prompt Engineering for Everyone - IBM</li>
                <li>Machine Learning with Python - IBM</li>
                <li>Data Privacy Fundamentals - IBM</li>
                <li>Data Science Methodologies - IBM</li>
                <li>Python (Basic) - HackerRank</li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="projects" class="section">
            <h2>Projects</h2>
            <ul>
                <li>Emotion Detection - <a href="https://github.com/Kishankumar1328/Emotion-detection" style="color: #FFA500;" target="_blank">link</a></li>
                <li>Sentiment Analysis - <a href="https://github.com/Kishankumar1328/sentiment_analysis-with-gradio" style="color: #FFA500;" target="_blank">link</a></li>
                <li>Lung Cancer Analysis - <a href="https://github.com/Kishankumar1328/lung_cancer_analysis" style="color: #FFA500;" target="_blank">link</a></li>
                <li>Semiconductor stock Dashboard - <a href="https://github.com/Kishankumar1328/SEMICONDUCTOR-STOCK-DASHBOARD" style="color: #FFA500;" target="_blank">link</a></li>
                <li>Stock Prediction - <a href="https://github.com/Kishankumar1328/Stock-prediction" style="color: #FFA500;" target="_blank">link</a></li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="contact" class="section">
            <h2>Contact</h2>
            <div class="contact">
                <a href="https://github.com/Kishankumar1328" style="color: #FFA500;" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/kishan-kumar-037175259/" style="color: #FFA500;" target="_blank">LinkedIn</a>
                <a href="mailto:krss132005@gmail.com" style="color: #FFA500;" target="_blank">Email</a>
                <a href="https://discord.com/invite/tenacious_quail_34080" style="color: #FFA500;" target="_blank">Discord</a>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
