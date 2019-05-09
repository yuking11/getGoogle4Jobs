# Get Result Google for Jobs

## About

selenium／webdriverを使って、Googleしごと検索の結果を20件程度取得する。

## Env

| macOS | python | pip |
|:-----:|:------:|:---:|
| High Sierra 10.13.6 | 3.6.4 | 19.0.1 |

## How to

1. python／pipの実行環境を構築（適当にググってください
1. `pip install selenium` でseleniumをインストール
1. OS／環境に合わせて[geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.24.0)をDL、解凍後、カレントディレクトリに配置
1. カレントディレクトリで `python jobs.py "キーワード"` を実行
