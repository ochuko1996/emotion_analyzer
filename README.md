# Repository for final project
Here's a comprehensive README for your Emotion Analyzer project:

---

# Emotion Analyzer

Emotion Analyzer is a web application that detects emotions from a given text input using IBM Watson's Emotion Analysis API. This application is built with Flask and leverages a custom emotion detection function to analyze text and return the detected emotions along with the dominant emotion.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/ochuko1996/sentiment_analyzer.git
cd sentiment_analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Ensure you have the necessary environment variables set up for accessing IBM Watson's Emotion Analysis API. Create a `.env` file in the root directory and add the following:

```
WATSON_EMOTION_API_URL=<your_watson_emotion_api_url>
WATSON_EMOTION_API_KEY=<your_watson_emotion_api_key>
```

Replace `<your_watson_emotion_api_url>` and `<your_watson_emotion_api_key>` with your actual API URL and API key.

## Usage

### Run the Application

```bash
python server.py
```

The application will start on `http://0.0.0.0:5000`.

### Access the Application

Open your web browser and navigate to `http://0.0.0.0:5000`. You will see the home page where you can input text to analyze its emotions.

## Endpoints

### Home

- **URL:** `/`
- **Method:** `GET`
- **Description:** Renders the home page with a form to input text for emotion analysis.

### Emotion Detector

- **URL:** `/emotionDetector`
- **Method:** `GET`
- **Parameters:**
  - `textToAnalyze` (string): The text to analyze for emotions.
- **Description:** Receives the text input from the home page, analyzes it using the emotion detection function, and returns the detected emotions along with the dominant emotion.

Example response:

```
For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.
```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to contribute to the project.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Ochuko Samuel George

---

Feel free to customize this README further to better fit your project's specifics and personal preferences.