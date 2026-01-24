import streamlit as st
import pandas as pd

from Raw_logic import cleartext
from translation import translate_text
from text_to_speech import text_to_speech



st.set_page_config(
    page_title="Verbaitm – Clear Text Simplification",
    page_icon="📄",
    layout="wide"
)


if "df" not in st.session_state:
    st.session_state.df = None

if "simplified_text" not in st.session_state:
    st.session_state.simplified_text = ""


st.title("📄 Verbaitm")
st.caption("Deterministic, LLM-free document simplification")


st.subheader("Enter text to simplify")

input_text = st.text_area(
    "Paste text here:",
    height=220
)


if st.button("Simplify Text"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Simplifying..."):
            results = cleartext(input_text)
            df = pd.DataFrame(results)

            st.session_state.df = df
            st.session_state.simplified_text = "\n".join(df["simple"].tolist())

        st.success("Text simplified!")


if st.session_state.df is not None:
    st.subheader("Results")

    for idx, row in st.session_state.df.iterrows():
        with st.expander(f"Sentence {idx + 1}", expanded=True):
            st.markdown("**Original**")
            st.write(row["original"])

            st.markdown("**Simplified**")
            st.success(row["simple"])

            st.markdown("**Explanation**")
            st.info(row["explanation"])


    st.subheader("Download")

    st.download_button(
        "📥 Download simplified text",
        st.session_state.simplified_text,
        file_name="cleartext_simplified.txt",
        mime="text/plain"
    )


    st.subheader("Translate & Audio")

    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "Spanish": "es"
    }

    selected_lang = st.selectbox(
        "Select language:",
        list(lang_map.keys())
    )

    if st.button("Translate & Generate Audio"):
        with st.spinner("Translating & generating audio..."):
            translated = translate_text(
                st.session_state.simplified_text,
                lang_map[selected_lang]
            )

            if translated.strip():
                st.markdown("**Translated Text**")
                st.write(translated)

                audio_path = text_to_speech(
                    translated,
                    lang_map[selected_lang]
                )

                if audio_path:
                    st.audio(audio_path)
                else:
                    st.error("Audio generation failed.")
            else:
                st.error("Translation failed.")


st.markdown("---")
st.caption("ClearText • Reliability over automation")

