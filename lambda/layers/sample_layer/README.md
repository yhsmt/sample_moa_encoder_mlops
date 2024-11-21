# cdk-base sample layer

## テスト

### 環境変数ファイルを置く

`env`という名前のファイルを下記の要領で置いておく。

```
CDK_APP_STAGE=dev-hoge
AWS_ACCESS_KEY_ID=hogehoge
AWS_SECRET_ACCESS_KEY=fugafuga
AWS_DEFAULT_REGION=us-west-2
```

### local実行

```bash
# テスト実行に必要なパッケージ類をインストール
# boto3はAWSのランタイム環境に含まれているので入れなくても良い
$ docker run -it --rm -v "$PWD":/var/task lambci/lambda:build-python3.8 pip install -r requirements.txt -t .

# test
$ docker run --env-file=env -it --rm -v "$PWD":/var/task:ro,delegated lambci/lambda:python3.8 python -m unittest -v

# run
$ docker run --env-file=env -it --rm -v "$PWD":/var/task:ro,delegated lambci/lambda:python3.8 function.handler `cat sample_event.json`
```

local実行に必要な環境変数は`env`ファイルに用意してdockerコンテナ実行時に使用。
`sample_event.json` は適当なeventデータのサンプルを用意すること。`handler` 関数の第１引数になっているオブジェクト。
