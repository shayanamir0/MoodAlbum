# [MoodAlbum - Paintings derived from emotions.](https://huggingface.co/spaces/DingoBeast/MoodAlbum)

## Project Description

MoodAlbum is a unique platform transforms written emotional expressions into AI-generated paintings, creating a bridge between internal feelings and external visual representations. The project is rooted in the understanding that visual representation can often capture emotional nuances that words alone might struggle to convey.

The primary goal of MoodAlbum is to bridge the emotional gap between humans and AI through art.

Find the full report [HERE].(https://github.com/shayanamir0/MoodAlbum/blob/main/Project%20Report%20MoodAlbum.pdf)

## How It Works

1. **Emotional Input**: Users begin by entering a text description of their current emotional state or feelings.

2. **AI Emotion Analysis**: The application uses a RoBERTa-based model to analyze the text and identify the top 5 emotions present.

3. **Artistic Interpretation**: Each detected emotion is associated with a specific art style and a renowned artist known for that style.

4. **Prompt Creation**: A unique prompt is generated, combining the detected emotions with their corresponding art styles and artists.

5. **Image Generation**: Using the Stable Diffusion v1.5 model, the application creates a custom painting based on the generated prompt.

6. **Visual Feedback**: The resulting AI-generated painting is displayed to the user, along with the detected emotions used for creation.

7. **Reflection**: Users can reflect on the generated artwork, considering how it relates to their expressed emotions and potentially gaining new insights into their emotional state.

## Availability and Processing Time

MoodAlbum is hosted on Hugging Face Spaces and can be accessed at: [MoodAlbum - Paintings derived from emotions.](https://huggingface.co/spaces/DingoBeast/MoodAlbum)

Please note that due to current hosting constraints, the image generation process is running on CPU. As a result, it may take up to 3.5 minutes to generate an image. We appreciate your patience during this process.
