<h1><strong>Xolve - Math Problem Solver</strong></h1>

<p>Welcome to <strong>Xolve</strong>, an innovative solution that uses gesture recognition to solve math problems drawn on the screen. Draw a math problem using your finger, and Xolve will recognize the gesture, process the math problem, and provide a step-by-step solution!</p>

<hr>

<h2><strong>Features</strong></h2>
<ul>
    <li><strong>Gesture Recognition</strong>: Uses computer vision to track hand gestures and draw on the screen.</li>
    <li><strong>AI-Powered Math Solver</strong>: The <strong>Gemini API</strong> is used to solve the math problem step-by-step.</li>
    <li><strong>Streamlit Web App</strong>: Interactive web interface to display and interact with the solution.</li>
    <li><strong>Real-Time Camera Feed</strong>: Webcam feed is used to capture hand movements.</li>
</ul>

<hr>

<h2><strong>Technologies Used</strong></h2>
<ul>
    <li><strong>Python</strong>: The main programming language for development.</li>
    <li><strong>OpenCV</strong>: For real-time hand tracking and drawing on the screen.</li>
    <li><strong>Streamlit</strong>: Used to build the interactive web app.</li>
    <li><strong>cvzone</strong>: For easy implementation of hand tracking and gesture recognition.</li>
    <li><strong>Gemini API</strong>: For generating step-by-step solutions to math problems.</li>
    <li><strong>PIL (Python Imaging Library)</strong>: For image processing.</li>
    <li><strong>dotenv</strong>: To securely manage environment variables like API keys.</li>
</ul>

<p><strong>Credits</strong>: A special thanks to <a href="https://github.com/cvzone/cvzone" target="_blank">cvzone</a> for providing an easy-to-use library for hand tracking and gesture recognition.</p>

<hr>

<h2><strong>Setup Instructions</strong></h2>

<h3><strong>1. Clone the Repository</strong></h3>
<p>First, clone the repository to your local machine:</p>
<pre><code>git clone https://github.com/prvnX/Xolve.git
cd Xolve</code></pre>

<h3><strong>2. Create a Virtual Environment</strong></h3>
<p>Create and activate a virtual environment to isolate the project dependencies:</p>
<pre><code>python -m venv venv</code></pre>

<p>Windows:</p>
<pre><code>.\venv\Scripts\activate</code></pre>

<p>macOS/Linux:</p>
<pre><code>source venv/bin/activate</code></pre>

<h3><strong>3. Install Dependencies</strong></h3>
<p>Install the required dependencies from the <code>requirements.txt</code> file:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3><strong>4. Setup API Key</strong></h3>
<p>This project requires access to the <strong>Gemini API</strong> to generate solutions. You need to set up your API key.</p>

<ol>
    <li>Create a <code>.env</code> file in the project root directory.</li>
    <li>Add your <strong>Gemini API key</strong> to the <code>.env</code> file:
        <pre><code>GEMINI_API_KEY=your_api_key_here</code></pre>
    </li>
</ol>

<h3><strong>5. Run the Application</strong></h3>
<p>After setting up everything, you can start the application using <strong>Streamlit</strong>:</p>
<pre><code>streamlit run app.py</code></pre>
<p>This will launch a local web app where you can interact with the math problem solver.</p>

<hr>

<h2><strong>How to Use</strong></h2>

<ol>
    <li><strong>Run the app</strong> and grant access to your camera.</li>
    <li><strong>Draw a math problem</strong> on the screen using your finger. The system will track your hand movements and interpret the drawing.</li>
    <li>Once the math problem is recognized, Xolve will solve it and provide the answer along with a detailed explanation.</li>
    <li>Use the <strong>"Run" checkbox</strong> to toggle the drawing and processing functionality.</li>
</ol>

<hr>

<h2><strong>Contributing</strong></h2>
<p>Contributions are welcome! If you'd like to contribute to the project, feel free to fork the repository, create a branch, and submit a pull request with your changes.</p>

<h3><strong>Steps to Contribute:</strong></h3>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature-name</code>).</li>
    <li>Make your changes.</li>
    <li>Commit your changes (<code>git commit -m 'Add new feature'</code>).</li>
    <li>Push to your forked repository (<code>git push origin feature-name</code>).</li>
    <li>Open a pull request.</li>
</ol>

<h2><strong>Social Links</strong></h2>
<ul>
    <li><a href="https://github.com/prvnX" target="_blank">GitHub</a></li>
    <li><a href="https://www.linkedin.com/in/praveen-kahatapitiya-560708171/" target="_blank">LinkedIn</a></li>
    <li><a href="https://web.facebook.com/praveenmadushan.kahatapitiya" target="_blank">Facebook</a></li>
</ul>

<hr>

<h3><strong>Made with ❤️ by prvnX</strong></h3>
