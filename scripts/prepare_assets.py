from pathlib import Path
from PIL import Image, ImageOps

SOURCE = Path("/Users/daraastahova/Downloads/drive-download-20260817T172806Z-1-001")
HEIC = Path("/Users/daraastahova/Desktop/гид по кейптауну/tmp/ql")
TMP = Path("/Users/daraastahova/Desktop/гид по кейптауну/tmp")
TELEGRAM = Path("/Users/daraastahova/Downloads/telegram download")
DOWNLOADS = Path("/Users/daraastahova/Downloads")
OUT = Path(__file__).resolve().parents[1] / "public" / "images"

ASSETS = {
    "hero.webp": SOURCE / "0 кампс обложка.png",
    "why.webp": SOURCE / "1 этот тур.jpg",
    "hosts.webp": HEIC / "2 кто мы.HEIC.png",
    "promise.webp": SOURCE / "3 что ждет.jpg",
    "day-1.webp": HEIC / "кампс бэй.HEIC.png",
    "day-2.webp": SOURCE / "вертолет.jpg",
    "day-3.webp": SOURCE / "винодельни .jpg",
    "day-4.webp": SOURCE / "пингвины.jpg",
    "day-5.webp": SOURCE / "тауншип 1.jpg",
    "day-6.webp": SOURCE / "патерностер.jpg",
    "day-7.webp": SOURCE / "Тусовка первый четверг.jpg",
    "day-8.webp": SOURCE / "сафари 9.jpg",
    "day-9.webp": SOURCE / "киты.jpg",
    "day-10.webp": SOURCE / "парад уток.jpg",
    "cape-point.webp": SOURCE / "мыс ДН.jpg",
    "flowers.webp": SOURCE / "ботанический сад.jpg",
    "table-mountain.webp": SOURCE / "Столовая гора.jpg",
    "bo-kaap.webp": SOURCE / "цветные домики BO KAAP.jpg",
    "stay-cape.webp": SOURCE / "жилье Distant 1.jpg",
    "stay-langebaan.webp": SOURCE / "жилье Langebaan 1.jpg",
    "stay-farm.webp": SOURCE / "жилье Kersefontein 1.webp",
    "stay-stellenbosch.webp": SOURCE / "жилье Life and Leisure 1 .jpg",
    "whale-festival.webp": TELEGRAM / "киты фест.jpg",
    "julian-estate.webp": TELEGRAM / "IMG_8174.JPG",
    "paternoster-oysters.webp": TELEGRAM / "IMG_8292.JPG",
    "day-3-alt.webp": HEIC / "винодельня 4.HEIC.png",
    "township-guide.webp": HEIC / "Тауншип ГИД.HEIC.png",
    "safari-zebras.webp": DOWNLOADS / "сафари 2.jpg",
    "table-mountain-day.webp": DOWNLOADS / "Столовая гора.png",
    "helicopters-day.webp": DOWNLOADS / "вертолеты 2.jpg",
    "julian-dinner.webp": TELEGRAM / "IMG_8894.PNG",
    "party-day.webp": DOWNLOADS / "тусовка первый четверг 2.jpg",
    "stay-cape-1.webp": TMP / "stay-extracted" / "Im94.jpg",
    "stay-cape-2.webp": TMP / "stay-extracted" / "Im96.jpg",
    "stay-langebaan-1.webp": TMP / "stay-extracted" / "Im104.jpg",
    "stay-langebaan-2.webp": TMP / "stay-extracted" / "Im107.jpg",
    "stay-farm-1.webp": TMP / "stay-extracted" / "Im115.jpg",
    "stay-farm-2.webp": TMP / "stay-extracted" / "Im118.jpg",
    "stay-stellenbosch-1.webp": TMP / "stay-extracted" / "Im127.jpg",
    "stay-stellenbosch-2.webp": TMP / "stay-extracted" / "Im129.jpg",
}

OUT.mkdir(parents=True, exist_ok=True)
for name, source in ASSETS.items():
    if not source.exists():
        continue
    image = Image.open(source)
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail((2000, 2000), Image.Resampling.LANCZOS)
    image.save(OUT / name, "WEBP", quality=84, method=6)
    print(f"{name}: {image.width}x{image.height}")
