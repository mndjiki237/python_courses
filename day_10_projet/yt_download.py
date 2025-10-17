from pytube import YouTube

try:
    link = input("Insert your YouTube link: ")
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    print("Téléchargement en cours...")
    stream.download()
    print("✅ Téléchargement terminé avec succès !")
except Exception as e:
    print("❌ Une erreur est survenue :", e)
