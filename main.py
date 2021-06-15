import os
import glob
from util import download, unzip
from make_dialogue_corpus import write_data

def main():
    raw_dir = './raw/'
    output_dir = './dbdc/'
    zip_file = './raw.zip'
    if not os.path.exists(raw_dir):
        os.mkdir(raw_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    # ファイルのダウンロード
    url = 'https://sites.google.com/site/dialoguebreakdowndetection/chat-dialogue-corpus/projectnextnlp-chat-dialogue-corpus.zip?attredirects=0&d=1'
    print('Downloading zip file...')
    download(url, zip_file)
    print('Done.')
    print('Unzipping the zip file...')
    unzip(zip_file, raw_dir)
    print('Done.')

    # ダウンロードしたデータからコーパスを作成
    file_list = glob.glob(raw_dir + 'json/*/*.json')
    print('Writing...')
    write_data(file_list, output_dir)
    print('Done.')


if __name__ == '__main__':
    main()