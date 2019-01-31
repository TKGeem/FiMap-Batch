# -*- coding: utf-8 -*-

import urllib.request
from requests import get  # to make GET request
import json
import csv

wifi = "https://www.hokoukukan.go.jp/download/jta_free_wifi.csv"
file_name = 'jta_free_wifi.csv'
url = 'http://192.168.1.15:3020/api/wifi/addPoints'
method = 'POST'
datas = []
key_list = ['スポットID', 'スポット名（日本語）', 'スポット名（英語）', 'スポットステータス', 'カテゴリー', '利用可能場所', '郵便番号', '都道府県', '住所（日本語）', '住所（英語）',
            '施設電話番号', '施設営業時間', 'SSID名称', '利用時間・回数等', '利用手続き', '多言語対応', '対応言語', 'ウェブサイトのURL', '緯度', '経度', '場所情報コード']



def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def make_dict():
    with open('jta_free_wifi.csv', 'r', encoding='shift_jisx0213') as csvfile:
        f = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        print(f)

        for value in f:
            h_data = {}

            h_data["name"] = str(value['スポット名（日本語）'])
            h_data["ssid"] = str(value['SSID名称'])
            h_data["address"] = str(value['住所（日本語）'])
            h_data["postCode"] = str(value['郵便番号'])
            h_data["hpUrl"] = str(value['ウェブサイトのURL'])
            h_data["latitude"] = float(value['緯度'])
            h_data["longitude"] = float(value['経度'])
            datas.append(h_data)


def upload_list():
    data = {
        'datas': datas,
    }
    headers = {
        'Content-Type': 'application/json',
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body)


if __name__ == '__main__':
    print("downloading...")
    #download(wifi, file_name)
    make_dict()
    print("uploading...")
    upload_list()
    print("finish")