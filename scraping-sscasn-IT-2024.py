# https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend=5101087&pengadaan_kd=2&offset=0

import requests
import csv
import time

headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'api-sscasn.bkn.go.id',
        'Origin': 'https://sscasn.bkn.go.id',
        'Pragma': 'no-cache',
        'Referer': 'https://sscasn.bkn.go.id/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
}

total_data = 9541
limit = 10
kode_ref_pend = '5101087'
pengadaan_kd = '2'

all_data = []

session = requests.Session()

for offset in range(0, total_data, limit):
    url = f"https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend={kode_ref_pend}&pengadaan_kd={pengadaan_kd}&offset={offset}"
    print(f"Fetching data offset {offset} ...")

    try:
        response = session.get(url, headers=headers)
        data = response.json()

        for row in data['data']['data']:
            all_data.append([
                row.get('ins_nm', ''),
                row.get('jp_nama', ''),
                row.get('formasi_nm', ''),
                row.get('jabatan_nm', ''),
                row.get('lokasi_nm', ''),
                row.get('jumlah_formasi', ''),
                row.get('gaji_min', ''),
                row.get('gaji_max', ''),
                row.get('jumlah_ms', '')
            ])

    except Exception as e:
        print(f"Gagal mengambil data di offset {offset}: {e}")

    time.sleep(0.3)

# Simpan ke CSV
with open("formasi_sscasn_2024.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Instansi", "Jabatan", "Lokasi", "Pendidikan", "Jumlah Formasi"])
    writer.writerows(all_data)

print(f"\n✅ Selesai! Total data terkumpul: {len(all_data)}")

import pandas as pd
# Buat DataFrame
df = pd.DataFrame(all_data, columns=["Instansi", "Jenis_Pengadaan", "Jenis_Formasi", "Jabatan", "Lokasi_Unit_Kerja", "Jumlah_Formasi", "Gaji_MIN", "Gaji_MAX","jumlah_Lulus_Verif"])
df
