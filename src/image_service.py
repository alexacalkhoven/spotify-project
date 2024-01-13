from openai import OpenAI
from dotenv import load_dotenv
import os

'''
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
'''

load_dotenv()

CLIENT_SECRET = os.getenv('OPENAI_CLIENT_SECRET')
BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'

class ImageService():
    '''
    This class holds functions related to AI image generation

    Member vars
    -----------
    openai : OpenAI client
    '''

    def __init__(self):
        self.openai = OpenAI(api_key=CLIENT_SECRET)

    def generate_image(self):
        '''
        generate AI image given prompts
        '''
        response = self.openai.images.generate(
          model="dall-e-3",
          prompt="a white siamese cat",
          size="1024x1024",
          quality="standard",
          n=1,
        )

        image_url = response.data[0].url
        print(image_url)

def main():
    print("main")
    service = ImageService()
    service.generate_image()

if __name__ == '__main__':
    main()