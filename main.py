import requests
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Yanıtın başarılı olup olmadığını kontrol et (status code 200)
    if response.status_code == 200:
        # JSON verisini al
        data = response.json()

        # JSON verisinin bir dizi (array) olup olmadığını kontrol et
        if isinstance(data, list):
            print("JSON verisi bir dizi (array) dir.")

            # Gerekli alanların var olup olmadığını kontrol et
            for post in data:

                if all(key in post for key in ['userId', 'id', 'title', 'body']):
                    print(f"Post ID {post['id']} geçerli.")
                else:
                    print(f"Post ID {post['id']} eksik alanlar içeriyor.")
        else:
            print("JSON verisi bir dizi (array) içermiyor.")
    else:
        print(f"HTTP isteği başarısız oldu. Status Code: {response.status_code}")

    # 'title' değerini kontrol et
    post = next((item for item in data if item['id'] == 1), None)
    if post:
        expected_title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        if post['title'] == expected_title:
            print(f"ID 1 olan gönderinin title değeri doğrulandı: {post['title']}")
        else:
            print(
                f"ID 1 olan gönderinin title değeri doğrulanamadı! (Beklenen: '{expected_title}', Gerçek: '{post['title']}')")
    else:
        print("ID 1 olan gönderi bulunamadı.")

    # Dizinin uzunluğunu kontrol et
    if len(data) >= 10:
        print(f"JSON dizisi en az 10 öğe içeriyor. Toplam öğe sayısı: {len(data)}")
    else:
        print(f"JSON dizisi 10 öğeden daha az içeriyor. Toplam öğe sayısı: {len(data)}")

    # Her bir öğede 'userId' alanının pozitif tamsayı olup olmadığını kontrol et
    if isinstance(data, list):
        all_positive_userIds = True
        for post in data:
            userId = post.get('userId', None)

            # 'userId' değeri pozitif tamsayı mı?
            if not isinstance(userId, int) or userId <= 0:
                print(f"Geçersiz userId bulundu: {userId} (ID: {post['id']})")
                all_positive_userIds = False

        # Sonuç
        if all_positive_userIds:
            print("Tüm 'userId' değerleri pozitif tamsayılardır.")
        else:
            print("Bazı 'userId' değerleri geçersiz veya negatif.")

