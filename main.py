import ffmpeg
import os
import time

def optymalizuj_wideo_kompatybilne(sciezka_wejsciowa, sciezka_wyjsciowa, poziom_jakosci=23):
    """
    Kompresuje wideo przy użyciu uniwersalnego kodeka H.264.
    
    Parametry:
    - poziom_jakosci: dla H.264 wartości 18-24 dają świetną jakość i małą wagę.
                      23 to domyślny, bezpieczny złoty środek.
    """
    if not os.path.exists(sciezka_wejsciowa):
        print(f"Błąd: Plik {sciezka_wejsciowa} nie istnieje!")
        return

    rozmiar_przed = os.path.getsize(sciezka_wejsciowa) / (1024 * 1024)
    print(f"🎬 Rozpoczynam optymalizację (Wersja uniwersalna H.264): {sciezka_wejsciowa}")
    print(f"📊 Rozmiar początkowy: {rozmiar_przed:.2f} MB")
    
    start_time = time.time()

    try:
        (
            ffmpeg
            .input(sciezka_wejsciowa)
            .output(
                sciezka_wyjsciowa, 
                vcodec='libx264',         # Zmiana na ultra-kompatybilny kodek
                crf=poziom_jakosci, 
                preset='medium', 
                pix_fmt='yuv420p',        # KLUCZOWE: ten format pikseli wymusza kompatybilność z przeglądarkami i telefonami
                acodec='copy'
            )
            .overwrite_output()
            .run(quiet=True)
        )

        czas_trwania = time.time() - start_time
        rozmiar_po = os.path.getsize(sciezka_wyjsciowa) / (1024 * 1024)
        oszczednosc = ((rozmiar_przed - rozmiar_po) / rozmiar_przed) * 100

        print("\n✅ Sukces! Optymalizacja zakończona.")
        print(f"⏱️ Czas operacji: {czas_trwania:.1f} sekund")
        print(f"📉 Nowy rozmiar: {rozmiar_po:.2f} MB")
        print(f"💎 Zaoszczędzono miejsce o: {oszczednosc:.1f}%")

    except ffmpeg.Error as e:
        print("\n❌ Wystąpił błąd podczas pracy FFmpeg:")
        print(e.stderr.decode('utf8'))

# --- URUCHOMIENIE ---
if __name__ == "__main__":
    plik_wejsciowy = 'film_testowy.mp4'  # Wrzuć tu swój plik
    plik_wyjsciowy = 'zmniejszony_kompatybilny.mp4'
    
    optymalizuj_wideo_kompatybilne(plik_wejsciowy, plik_wyjsciowy)