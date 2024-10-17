import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = 
                os.environ['OPENAI_API_KEY'])

def identify_animal(image):
  response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Identify the animal in this image. If there are multiple animals, list them all."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": image,
                      },
                  },
              ],
          }
      ],
      max_tokens=300,
  )
  return response.choices[0].message.content

def get_animal_info(animal):
  response = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content": "You are a knowledgeable assistant providing information about animals."},
          {"role": "user", "content": f"Provide brief insights about {animal}, including habitat, diet, and interesting facts."}
      ],
      max_tokens=300,
  )
  return response.choices[0].message.content

st.title("PetPedia: Smart Identification and Care Companion")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image", use_column_width=True)

  if st.button("Identify Animal"):
      with st.spinner("Identifying animal..."):
          # Convert image to bytes
          img_byte_arr = io.BytesIO()
          image.save(img_byte_arr, format='PNG')
          img_byte_arr = img_byte_arr.getvalue()

          # Encode image to base64
          import base64
          base64_image = base64.b64encode(img_byte_arr).decode('utf-8')

          # Identify animal
          animal = identify_animal(f"data:image/png;base64,{base64_image}")
          st.write(f"Identified animal(s): {animal}")

          # Get animal information
          info = get_animal_info(animal)
          st.write("Animal Information:")
          st.write(info)

st.sidebar.title("About")
st.sidebar.info("PetPedia is a smart companion for identifying animals and learning about their care. Upload an image to get started!")