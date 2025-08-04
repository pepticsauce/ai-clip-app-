import streamlit as st
import shutil
from ai_clipper import download_video, transcribe_video, extract_highlights, create_clips

st.set_page_config(page_title="AI TikTok Clipper")

st.title("🎬 AI TikTok Clipper")
st.write("Paste a YouTube or Twitch link and get 50 TikTok‑ready clips (8–27 sec each).")

url = st.text_input("Enter Video URL")
if st.button("Generate AI Clips") and url:
    with st.spinner("Working..."):
        try:
            video_path = "downloaded_video.mp4"
            clip_folder = "clips"

            download_video(url, video_path)
            transcript = transcribe_video(video_path)
            highlights = extract_highlights(transcript, 8, 27,
                                            ["kill", "funny", "insane", "crazy", "clutch", "no way", "help", "wow"],
                                            50)
            create_clips(video_path, highlights, clip_folder)

            shutil.make_archive("ai_clips", 'zip', clip_folder)
            with open("ai_clips.zip", "rb") as f:
                st.download_button("📥 Download All Clips", f, file_name="ai_clips.zip")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
