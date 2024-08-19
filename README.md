# [MoodAlbum - Paintings derived from emotions.](https://huggingface.co/spaces/DingoBeast/MoodAlbum)

## Project Description

MoodAlbum is a web application designed for visual art therapy, with a strong focus on psychology and enhancing emotional interaction between humans and AI. This unique platform transforms written emotional expressions into AI-generated paintings, creating a bridge between internal feelings and external visual representations. The project is rooted in the understanding that visual representation can often capture emotional nuances that words alone might struggle to convey.

The primary goal of MoodAlbum is to bridge the emotional gap between humans and AI through art. 

A key feature of MoodAlbum is that the generated paintings are derived from actual paintings, art styles, and eras from previous generations. This approach connects users' emotions to the rich art history, reflecting the periods artists went through and the emotional contexts of their times. By doing so, MoodAlbum also places them within the broader context of human emotional expression throughout art history.

Key aspects of MoodAlbum include:

1. **Visual Art Therapy**: Serves as a digital tool for art therapy, allowing users to externalize and process their emotions through AI-generated artwork.

2. **Psychological Focus**: Emphasizes the psychological aspect of emotion recognition and expression, potentially aiding in self-reflection and emotional awareness.

3. **Human-AI Emotional Interaction**: Fosters a unique form of emotional communication between users and AI, where human emotions are interpreted and visually represented by artificial intelligence.

4. **Artistic Emotion Mapping**: Associates detected emotions with various art styles and famous artists, providing an educational component about art history in relation to emotional expression.

## How It Works

1. **Emotional Input**: Users begin by entering a text description of their current emotional state or feelings.

2. **AI Emotion Analysis**: The application uses a RoBERTa-based model (SamLowe/roberta-base-go_emotions) to analyze the text and identify the top 5 emotions present.

3. **Artistic Interpretation**: Each detected emotion is associated with a specific art style and a renowned artist known for that style.

4. **Prompt Creation**: A unique prompt is generated, combining the detected emotions with their corresponding art styles and artists.

5. **Image Generation**: Using the Stable Diffusion v1.5 model, the application creates a custom painting based on the generated prompt.

6. **Visual Feedback**: The resulting AI-generated painting is displayed to the user, along with the detected emotions and the prompt used for creation.

7. **Reflection**: Users can reflect on the generated artwork, considering how it relates to their expressed emotions and potentially gaining new insights into their emotional state.

Through this process, MoodAlbum creates a dynamic and personalized experience that encourages emotional exploration and expression through the medium of AI-generated art, potentially offering new perspectives on one's emotional landscape.

## Availability and Processing Time

MoodAlbum is hosted on Hugging Face Spaces and can be accessed at: [MoodAlbum - Paintings derived from emotions.](https://huggingface.co/spaces/DingoBeast/MoodAlbum)

Please note that due to current hosting constraints, the image generation process is running on CPU. As a result, it may take up to 3.5 minutes to generate an image. We appreciate your patience during this process.
