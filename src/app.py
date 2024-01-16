from spotify_service import SpotifyService
import matplotlib.pyplot as plt

def main():
    print("main")
    service = SpotifyService()
    response = service.get_n_recent_tracks(30)
    items = response['items']
    track_ids = [track['track']['id'] for track in items]
    danceability = []
    for track_id in track_ids:
        properties = service.get_properties(track_id)
        danceability.append(properties['danceability'])
    print(danceability)
    plt.hist(danceability, bins=10)
    plt.ylabel('Num songs')
    plt.xlabel('Danceability')
    plt.show()

if __name__ == '__main__':
    main()