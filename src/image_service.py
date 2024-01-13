import os

from dotenv import load_dotenv

load_dotenv()

# CLIENT_SECRET = os.getenv('OPENAI_CLIENT_SECRET')
# BASE_URL = 'https://api.spotify.com/v1/'
# AUTH_URL = 'https://accounts.spotify.com/api/token'

class ImageService():
    '''
    This class holds functions related to AI image generation

    Member vars
    -----------
    '''

    def __init__(self):
        '''
        '''

    def generate_image(self):
        '''
        generate AI image given prompts
        '''

def main():
    print("main")
    service = ImageService()
    service.generate_image()

if __name__ == '__main__':
    main()