# YouTube Summarizer and Sentiment Analyzer

## Introduction

This is a Streamlit web application for summarizing the content of YouTube videos and analyzing their sentiment. The application extracts the transcript of the provided YouTube video, generates a detailed summary, and analyzes the sentiment of the content. It utilizes the Google Gemini Pro API for content generation and the TextBlob library for sentiment analysis.

## Features

- Extracts transcript from YouTube videos
- Generates detailed summaries within a specified word limit
- Analyzes sentiment (Positive, Neutral, Negative) of the video content
- Provides an option to input YouTube video link and select actions from the sidebar

## Usage

1. Clone the repository:

```bash
git clone https://github.com/FasilHameed/YouTube-Summarizer-and-Sentiment-Analyzer.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Google API key by creating a `.env` file in the project directory and adding your API key:

```dotenv
GOOGLE_API_KEY=your_google_api_key
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

5. Enter the YouTube video link and select the desired action from the sidebar.

## Dependencies

- Streamlit
- dotenv
- google.generativeai
- textblob
- youtube_transcript_api

## Acknowledgments

- This project utilizes the Google Gemini Pro API for content generation.
- Sentiment analysis is performed using the TextBlob library.


## Demo

![web app link](https://huggingface.co/spaces/lisaf/Youtube-Vedio-Summarizer-and-sentiment-analyzer)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Connect with me at**

[GitHub](https://github.com/FasilHameed) | [LinkedIn](https://www.linkedin.com/in/faisal--hameed/) | Phone: +917006862681 | Email: faisalhameed763@gmail.com

Powered By Gemini 💫 and Streamlit 🚀
