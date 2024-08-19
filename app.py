# import streamlit as st
# from transformers import pipeline
# from diffusers import StableDiffusionPipeline
# import torch

# # Check for GPU availability
# device = "cuda" if torch.cuda.is_available() else "cpu"
# if device == "cpu" and torch.backends.mps.is_available():
#     device = "mps"

# # Load sentiment analysis model
# @st.cache_resource
# def load_sentiment_analyzer():
#     return pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=5, device=device)

# # Load text-to-image model
# @st.cache_resource
# def load_text2img():
#     model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
#     if device == "mps":
#         model = model.to(device)
#     else:
#         model = model.to(device)
#     return model

# sentiment_analyzer = load_sentiment_analyzer()
# text2img = load_text2img()

# def analyze_sentiment(text):
#     results = sentiment_analyzer(text)
#     emotions = [(result['label'], result['score']) for result in results[0]]
#     return emotions
#     #return [(result['label'], result['score']) for result in results]

# def generate_prompt(emotions):
#     era_styles = {
#         "joy": ("Impressionist", "Claude Monet"),
#         "sadness": ("Romantic", "Caspar David Friedrich"),
#         "anger": ("Expressionist", "Edvard Munch"),
#         "fear": ("Surrealist", "Salvador Dali"),
#         "disgust": ("Abstract", "Jackson Pollock"),
#         "surprise": ("Pop Art", "Andy Warhol"),
#         "neutral": ("Minimalist", "Piet Mondrian"),
#         "love": ("Renaissance", "Sandro Botticelli"),
#         "admiration": ("Baroque", "Rembrandt"),
#         "approval": ("Neoclassical", "Jacques-Louis David"),
#         "caring": ("Pre-Raphaelite", "John Everett Millais"),
#         "excitement": ("Fauvism", "Henri Matisse"),
#         "gratitude": ("Rococo", "Jean-Honoré Fragonard"),
#         "pride": ("Art Nouveau", "Gustav Klimt"),
#         "relief": ("Pointillism", "Georges Seurat"),
#         "remorse": ("Symbolism", "Odilon Redon"),
#         "confusion": ("Cubism", "Pablo Picasso"),
#         "curiosity": ("Futurism", "Umberto Boccioni"),
#         "desire": ("Art Deco", "Tamara de Lempicka"),
#         "disapproval": ("Dada", "Marcel Duchamp"),
#         "embarrassment": ("Naive Art", "Henri Rousseau"),
#         "nervousness": ("Constructivism", "Vladimir Tatlin"),
#         "optimism": ("De Stijl", "Theo van Doesburg"),
#         "realization": ("Bauhaus", "Wassily Kandinsky"),
#         "amusement": ("Suprematism", "Kazimir Malevich"),
#         "annoyed": ("Social Realism", "Diego Rivera"),
#         "disappointment": ("Color Field", "Mark Rothko"),
#         "grief": ("Neo-Expressionism", "Jean-Michel Basquiat")
#     }
    
#     prompt_parts = []
#     for emotion, _ in emotions:
#         style, artist = era_styles.get(emotion, ("Contemporary", "Various"))
#         prompt_parts.append(f"a {style} painting in the style of {artist} depicting {emotion}")
    
#     return "Create a multi-style artwork combining " + ", ".join(prompt_parts)

# def generate_image(prompt):
#     image = text2img(prompt, num_inference_steps=50).images[0]
#     return image

# def main():
#     st.title("MoodAlbum - Visualise your feelings.")

#     user_text = st.text_area("How are you feeling? Describe your emotions:")

#     if st.button("Generate Painting"):
#         if user_text:
#             with st.spinner("Analyzing emotions..."):
#                 emotions = analyze_sentiment(user_text)
            
#             st.write("Detected emotions:")
#             for emotion, score in emotions:
#                 st.write(f"- {emotion}: {score:.2f}")
            
#             prompt = generate_prompt(emotions)
#             st.write("Generated prompt:")
#             st.write(prompt)
            
#             with st.spinner("Generating painting... This may take a while."):
#                 image = generate_image(prompt)
            
#             st.image(image, caption="Your feelings coming to life!", use_column_width=True)
#         else:
#             st.warning("Please enter some text describing your emotions.")

# if __name__ == "__main__":
#     main()





import streamlit as st
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch

# Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"

# Set appropriate dtype based on device
torch_dtype = torch.float16 if device == "cuda" else torch.float32

# Load sentiment analysis model
@st.cache_resource
def load_sentiment_analyzer():
    return pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=5, device=device)

# Load text-to-image model
@st.cache_resource
def load_text2img():
    model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch_dtype)
    model = model.to(device)
    return model

sentiment_analyzer = load_sentiment_analyzer()
text2img = load_text2img()

def analyze_sentiment(text):
     results = sentiment_analyzer(text)
     emotions = [(result['label'], result['score']) for result in results[0]]
     return emotions

def generate_prompt(emotions):
    era_styles = {
        "joy": ("Impressionist", "Claude Monet"),
        "sadness": ("Romantic", "Caspar David Friedrich"),
        "anger": ("Expressionist", "Edvard Munch"),
        "fear": ("Surrealist", "Salvador Dali"),
        "disgust": ("Abstract", "Jackson Pollock"),
        "surprise": ("Pop Art", "Andy Warhol"),
        "neutral": ("Minimalist", "Piet Mondrian"),
        "love": ("Renaissance", "Sandro Botticelli"),
        "admiration": ("Baroque", "Rembrandt"),
        "approval": ("Neoclassical", "Jacques-Louis David"),
        "caring": ("Pre-Raphaelite", "John Everett Millais"),
        "excitement": ("Fauvism", "Henri Matisse"),
        "gratitude": ("Rococo", "Jean-Honoré Fragonard"),
        "pride": ("Art Nouveau", "Gustav Klimt"),
        "relief": ("Pointillism", "Georges Seurat"),
        "remorse": ("Symbolism", "Odilon Redon"),
        "confusion": ("Cubism", "Pablo Picasso"),
        "curiosity": ("Futurism", "Umberto Boccioni"),
        "desire": ("Art Deco", "Tamara de Lempicka"),
        "disapproval": ("Dada", "Marcel Duchamp"),
        "embarrassment": ("Naive Art", "Henri Rousseau"),
        "nervousness": ("Constructivism", "Vladimir Tatlin"),
        "optimism": ("De Stijl", "Theo van Doesburg"),
        "realization": ("Bauhaus", "Wassily Kandinsky"),
        "amusement": ("Suprematism", "Kazimir Malevich"),
        "annoyed": ("Social Realism", "Diego Rivera"),
        "disappointment": ("Color Field", "Mark Rothko"),
        "grief": ("Neo-Expressionism", "Jean-Michel Basquiat")
    }
    
    prompt_parts = []
     for emotion, _ in emotions:
         style, artist = era_styles.get(emotion, ("Contemporary", "Various"))
         prompt_parts.append(f"a {style} painting in the style of {artist} depicting {emotion}")
    
     return "Create a multi-style artwork combining " + ", ".join(prompt_parts)

def generate_image(prompt):
    image = text2img(prompt, num_inference_steps=50).images[0]
    return image

def main():
    st.title("Emotion to Painting Generator")

    user_text = st.text_area("How are you feeling? Describe your emotions:")

    if st.button("Generate Painting"):
        if user_text:
            with st.spinner("Analyzing emotions..."):
                emotions = analyze_sentiment(user_text)
            
            st.write("Detected emotions:")
            for emotion, score in emotions:
                st.write(f"- {emotion}")
            
            prompt = generate_prompt(emotions)
            st.write("Generated prompt:")
            st.write(prompt)
            
            with st.spinner("Generating painting... This may take a while."):
                image = generate_image(prompt)
            
            st.image(image, caption="Generated Emotion Painting", use_column_width=True)
        else:
            st.warning("Please enter some text describing your emotions.")

if __name__ == "__main__":
    main()
