import tweepy
import re
import matplotlib.pyplot as plt
from collections import Counter

todos_los_hashtags = []

# 💡 Reemplaza estas claves con las que obtendrás de tu cuenta de desarrollador
API_KEY = "TU_API_KEY"
API_SECRET = "TU_API_SECRET"
ACCESS_TOKEN = "TU_ACCESS_TOKEN"
ACCESS_SECRET = "TU_ACCESS_SECRET"

#  Autenticación con la API de Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

usuario = input("Ingresa el nombre de usuario de Twitter (sin @): ")

#  Obtener los últimos 20 tuits
try:
    tweets = api.user_timeline(screen_name=usuario, count=20, tweet_mode="extended")
    
    print(f"\nÚltimos 20 tuits de @{usuario}:\n")
    for i, tweet in enumerate(tweets, start=1):
        print(f"{i}. {tweet.full_text}\n")
        #
        hashtags = re.findall(r"#\w+", tweet.full_text)
        todos_los_hashtags.extend(hashtags)

    contador = Counter(todos_los_hashtags)

    print("\n📊 Hashtags más usados en los últimos 20 tuits:\n")

    if contador:
        for tag, cantidad in contador.most_common():
            print(f"{tag}: {cantidad} vez/veces")
    else: 
        print("No se encontraron hashtags en los tuits.")

except tweepy.TweepError as e:
    print(f"❌ Error al acceder a la cuenta de Twitter: {e}")


# Graficando los hashtag obtenidos  
top_hashtags = contador.most_common(10) 

if top_hashtags: 
    etiquetas = [tag for tag, _ in top_hashtags ]
    cantidades = [cantidad for _, cantidad in top_hashtags]

    # Grafico de barras 
    plt.figure(figsize=(10, 6))
    plt.barh(etiquetas, cantidades, color='red')
    plt.xlabel("cantidad de veces")
    plt.title("Top 10 hashtags mas usados")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


