import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="LabelBoxMini",
    page_icon="🧊",
    layout="wide")

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roboflow Clone</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            overflow: hidden;
            padding: 0;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #fff;
            padding: 10px 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .logo {
            font-size: 24px;
            color: #6a0dad;
            font-weight: bold;
        }

        .navbar ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
        }

        .navbar ul li {
            margin: 0 15px;
        }

        .navbar ul li a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            cursor: pointer;
        }

        .sign-in-btn {
            background-color: #6a0dad;
            color: #fff;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
        }

        main {
            text-align: center;
            padding: 50px 20px;
        }

        main h2 {
            font-size: 36px;
            margin-bottom: 20px;
        }

        main p {
            font-size: 18px;
            margin-bottom: 30px;
        }

        .btn-group button {
            padding: 10px 20px;
            margin: 0 10px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        .primary-btn {
            background-color: #6a0dad;
            color: white;
        }

        .secondary-btn {
            background-color: white;
            color: #6a0dad;
            border: 1px solid #6a0dad;
        }

        .image-container {
            position: relative;
            width: 60%;
            margin: 30px auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }

        .image-container img {
            width: 100%;
            border-radius: 10px;
            transition: transform 0.3s ease;
        }

        .image-container img:hover {
            transform: scale(1.05);
        }

        .overlay-buttons,
        .button-group {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
        }

        .overlay-buttons button,
        .button-group button {
            background-color: #6a0dad;
            color: white;
            border: none;
            padding: 8px 16px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            border-radius: 5px;
            transition: all 0.3s ease;
            opacity: 0.9;
        }

        .button-group button {
            background-color: #fff;
            color: #6a0dad;
            border: 1px solid #6a0dad;
        }

        .button-group button:hover,
        .overlay-buttons button:hover {
            opacity: 1;
            background-color: #6a0dad;
            color: white;
        }

        /* New sections styling */
        .section {
            padding: 50px 20px;
            text-align: center;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }

        .features, .testimonials {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 30px;
            margin-top: 30px;
        }

        .feature, .testimonial {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .feature h3, .testimonial h3 {
            color: #6a0dad;
        }

        .testimonial p {
            font-style: italic;
            color: #777;
        }

        .testimonial img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            margin-bottom: 10px;
        }

        footer {
            background-color: #6a0dad;
            color: white;
            padding: 20px;
            text-align: center;
        }

        footer a {
            color: white;
            text-decoration: none;
        }

    </style>
</head>
<body>
    <header class="navbar">
        <h1 class="logo">LabelBox</h1>
        <nav>
            <ul>
                <li><a href="#section1">Products</a></li>
                <li><a href="#section2">Solutions</a></li>
                <li><a href="#section3">Developers</a></li>
                <li><a href="#section4">Pricing</a></li>
                <li><a href="#section5">Docs</a></li>
                <li><a href="#section6">Blog</a></li>
            </ul>
        </nav>
        <button class="sign-in-btn">Sign In</button>
    </header>
    <main>
        <h2>Everything you need to build and deploy computer vision applications.</h2>
        <p>Used by over 1 million engineers to create datasets, train models, and deploy to production.</p>
        <div class="btn-group">
            <button class="primary-btn" onclick="showAlert('Get Started Clicked')">Get Started</button>
            <button class="secondary-btn" onclick="showAlert('Request a Demo Clicked')">Request a Demo</button>
        </div>
        <div class="image-container">
            <img id="mainImage" src="https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/22606/images/b80886-de54-602b-81d2-f0425b17e04_shutterstock_668209624-1.jpeg" alt="Placeholder Image">
            <div class="button-group">
                <button onclick="changeImage('https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/22606/images/1446e76-f181-6047-4e73-8d8ba3c6a50e_object_detection_1.webp')">Detection</button>
                <button onclick="changeImage('https://user-images.githubusercontent.com/62513924/196107891-bb8124de-99c6-4039-b556-2ade403bd985.png')">Tracking</button>
                <button onclick="changeImage('https://user-images.githubusercontent.com/62513924/196107891-bb8124de-99c6-4039-b556-2ade403bd985.png')">Counting</button>
                <button onclick="changeImage('https://user-images.githubusercontent.com/62513924/196107891-bb8124de-99c6-4039-b556-2ade403bd985.png')">Analysis</button>
            </div>
        </div>
    </main>

    <!-- Features Section -->
    <div id="section1" class="section">
        <h2>Our Features</h2>
        <div class="features">
            <div class="feature">
                <h3>Fast Training</h3>
                <p>Speed up your model training with optimized tools that reduce processing time.</p>
            </div>
            <div class="feature">
                <h3>Seamless Integration</h3>
                <p>Easily integrate our platform with your existing tools and workflows.</p>
            </div>
            <div class="feature">
                <h3>Scalable Models</h3>
                <p>Build and deploy models that can scale to meet your needs, no matter the size.</p>
            </div>
        </div>
    </div>

    <!-- Testimonials Section -->
    <div id="section2" class="section">
        <h2>What Our Users Say</h2>
        <div class="testimonials">
            <div class="testimonial">
                <img src="https://randomuser.me/api/portraits/men/10.jpg" alt="User 1">
                <h3>John Doe</h3>
                <p>"This platform has revolutionized how we build and deploy AI models. Highly recommend!"</p>
            </div>
            <div class="testimonial">
                <img src="https://randomuser.me/api/portraits/women/10.jpg" alt="User 2">
                <h3>Jane Smith</h3>
                <p>"I love the intuitive UI and powerful features. It makes our work so much easier."</p>
            </div>
            <div class="testimonial">
                <img src="https://randomuser.me/api/portraits/men/20.jpg" alt="User 3">
                <h3>Sarah Lee</h3>
                <p>"Great support and a fast way to get models into production. Truly a game-changer."</p>
            </div>
        </div>
    </div>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 LabelBox. All rights reserved. <br>
        <a href="#section1">Privacy Policy</a> | <a href="#section2">Terms of Service</a></p>
    </footer>

    <script>
        function showAlert(message) {
            alert(message);
        }

        function changeImage(imageUrl) {
            document.getElementById('mainImage').src = imageUrl;
        }

        // Detect when the sections come into view
        function fadeInOnScroll() {
            const sections = document.querySelectorAll('.section');
            sections.forEach(section => {
                const rect = section.getBoundingClientRect();
                if (rect.top <= window.innerHeight * 0.8) {
                    section.style.opacity = 1;
                }
            });
        }

        window.addEventListener('scroll', fadeInOnScroll);
        fadeInOnScroll();  // Initial check

        document.querySelectorAll('.navbar ul li a').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = e.target.getAttribute('href').substring(1);
                document.getElementById(targetId)?.scrollIntoView({ behavior: 'smooth' });
            });
        });
    </script>
</body>
</html>

""",height=1700,scrolling=True)