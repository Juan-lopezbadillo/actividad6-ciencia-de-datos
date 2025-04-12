import tweepy
import re
import matplotlib.pyplot as plt
from collections import Counter

todos_los_hashtags = []

# 💡 Claves de la API (solo necesitas el Bearer Token para lectura en v2)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAG1I0gEAAAAAH8e6Pol6LhVxszzta%2FYOu%2F8muiE%3DVKIDLue3dAfwwognmYAUBUznGqKoD6tSPJ7abJ2QASrp0Fpdg4"

# Autenticación con API v2
try:
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    print("✅ Conexión exitosa con la API v2 de Twitter")
except Exception as e:
    print("❌ Error al conectar:", e)
    exit()

usuario = input("Ingresa el nombre de usuario de Twitter (sin @): ")

# Obtener el ID del usuario a partir del nombre
try:
    user = client.get_user(username=usuario)
    user_id = user.data.id
except Exception as e:
    print(f"❌ No se pudo obtener el ID del usuario: {e}")
    exit()

# Obtener los últimos 20 tuits del usuario
try:
    response = client.get_users_tweets(
        id=user_id,
        max_results=20,
        tweet_fields=["text", "entities"]
    )

    tweets = response.data

    if not tweets:
        print("⚠ No se encontraron tuits para este usuario.")
        exit()

    print(f"\nÚltimos 20 tuits de @{usuario}:\n")
    for i, tweet in enumerate(tweets, start=1):
        print(f"{i}. {tweet.text}\n")
        hashtags = re.findall(r"#\w+", tweet.text)
        todos_los_hashtags.extend(hashtags)

    if todos_los_hashtags:
        contador = Counter(todos_los_hashtags)
        print("\n📊 Hashtags más usados en los últimos 20 tuits:\n")
        for tag, cantidad in contador.most_common():
            print(f"{tag}: {cantidad} vez/veces")
    else:
        print("⚠ No se encontraron hashtags en los tuits.")

except tweepy.TweepyException as e:
    print(f"❌ Error al acceder a los tuits del usuario: {e}")
    exit()

# Graficar hashtags si hay datos
if todos_los_hashtags:
    top_hashtags = contador.most_common(10)

    etiquetas = [tag for tag, _ in top_hashtags]
    cantidades = [cantidad for _, cantidad in top_hashtags]

    plt.figure(figsize=(10, 6))
    plt.barh(etiquetas, cantidades, color='blue')
    plt.xlabel("Cantidad de veces")
    plt.title("Top 10 hashtags más usados")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
else:
    print("⚠ No se pueden mostrar gráficos ya que no se encontraron hashtags. ⚠")
