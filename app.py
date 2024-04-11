import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from textblob import TextBlob

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """**You are a YouTube video summarizer.** You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 1500 words.The Summary Should Be As detailed As Possible  . Please provide the summary of the text given here:  """


# Function to extract transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e


# Function to generate summary based on prompt using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt, max_length):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    summary = response.text

    # Split the summary into words and limit the length
    words = summary.split()
    if len(words) > max_length:
        summary = ' '.join(words[:max_length])

    return summary


# Function to analyze sentiment of text
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score == 0:
        return "Neutral"
    else:
        return "Negative"


# Streamlit app
st.set_page_config(page_title="YouTube  Summarizer and Sentiment Analyzer", page_icon=":clapper:", layout="wide")

st.title("🎥 YouTube Sentiment Analyzer")

st.sidebar.header("Options")
youtube_link = st.sidebar.text_input("Enter YouTube Video Link:")
action = st.sidebar.selectbox("Select Action:", ["Choose", "Get Detailed Summary", "Analyze Sentiment"])

if action == "Get Detailed Summary":
    max_length = st.sidebar.slider("Select Maximum Summary Length (words)", min_value=50, max_value=1500, value=400)

if st.sidebar.button("🚀 Perform Action"):
    if action == "Get Detailed Summary":
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt, max_length)
            st.markdown("## Detailed Summary:")
            st.write(summary)

    elif action == "Analyze Sentiment":
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            sentiment = analyze_sentiment(transcript_text)
            st.markdown("## Sentiment Analysis:")
            st.write(f"The sentiment of the video is: {sentiment}")

# Show YouTube video thumbnail if link provided
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
else:
    # Stretched GIF
    st.markdown('<div style="font-family:Arial; text-align:center;"><iframe allow="fullscreen" frameBorder="0" height="400" src="https://giphy.com/embed/SNHd3FpcOrPHoBHtLD/video" width="800"></iframe></div>', unsafe_allow_html=True)

# Footer
footer_with_image_light_blue = """
<style>
.footer {
    background-color: #E0F2F1;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    animation: fadeIn 1s;
}
.footer img {
    max-width: 100%;
    border-radius: 10px;
    margin-top: 10px;
}
.footer .line {
    height: 1px;
    background-color: #B2DFDB;
    margin: 10px 0;
}
.footer .connect-text {
    color: #004D40;
    font-weight: bold;
    margin-bottom: 10px;
}
.footer a {
    margin: 0 10px;
}
.footer .powered-by {
    color: #004D40;
    font-size: 14px;
    margin-top: 10px;
}
.bright-text {
    color: #004D40;
}
/* Add Animation */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.chat-message {
    animation: fadeIn 0.5s ease-out;
}
</style>
<div class="footer">
    <div class="line"></div>
    <div class="connect-text">Connect with me at</div>
    <a href="https://github.com/FasilHameed" target="_blank"><img src="https://img.icons8.com/plasticine/30/000000/github.png" alt="GitHub"></a>
    <a href="https://www.linkedin.com/in/faisal--hameed/" target="_blank"><img src="https://img.icons8.com/plasticine/30/000000/linkedin.png" alt="LinkedIn"></a>
    <a href="tel:+917006862681"><img src="https://img.icons8.com/plasticine/30/000000/phone.png" alt="Phone"></a>
    <a href="mailto:faisalhameed763@gmail.com"><img src="https://img.icons8.com/plasticine/30/000000/gmail.png" alt="Gmail"></a>
    <div class="line"></div>
    <div class="powered-by">Powered By <img src="https://img.icons8.com/clouds/30/000000/gemini.png" alt="Gemini"> Gemini 💫 and Streamlit 🚀</div>
</div>
"""

# Render Footer
st.markdown(footer_with_image_light_blue, unsafe_allow_html=True)