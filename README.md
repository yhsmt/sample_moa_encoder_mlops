# Sample - MoA Encoder MLOps

MoA Encoder MLOps の試作

## 最初に確認すること

```
$ cdk doctor
...
  - CDK_APP_STAGE = dev-<ユーザー名>
  - CDK_DEFAULT_ACCOUNT = <AWS アカウントID>
  - CDK_DEFAULT_REGION = us-west-2
```

必ず上記3つの環境変数が適切に設定されている状態を確認してから、使用すること。
また、`CDK_APP_STAGE = prod`は使用しないこと。

**`cdk deploy`の前には、必ず`cdk doctor`で各種の向き先を確認すること。**

## セットアップ

```
# virtualenv 開始
$ cd cdk-base
$ python3 -m venv .venv
$ pipenv install
```

## 使い方

### lambda/function および lambda/layers ディレクトリ下のpythonモジュールをインストールしておく

`lambda`ディレクトリ以下で、stackをdeployする前に予め`pip install`をやっておく必要のあるディレクトリがある。各ディレクトリのREADMEを参照。

### 基本的な使い方

```
# virtualenv
$ cd sample_moa_encoder_mlops
$ pipenv shell

# generate template and deploy
$ cdk ls
$ cdk diff <stack名>
$ cdk deploy <stack名>
```

**stackをdeployする際、S3 Bucket名が他のstackのものと重複するとdeployに失敗するので注意する。**

### スタック削除

stackにdeployされたS3 Bucketの中身はすべて消してからstackを削除する。

**ファイルが残っているとbucketの削除に失敗するので注意する。**

```
$ aws s3 rm --recursive s3://<CDK_APP_STAGE>-xxxx-bucket/
$ cdk destroy <stack名>
```

## ディレクトリの説明

主要なディレクトリだけリストアップ

```
.
├── cdk
│   └── stacks.py
├── cdk.out
├── lambda
│  ├─── functions
│  │    └── sample_function
│  │         └── tests
│  │            └── fixtures
│  └──── sample_layer
└── tests
    └── app
```

| path             | description                                                                        |
|:-----------------|:-----------------------------------------------------------------------------------|
| cdk/             | CDKのコード                                                                        |
| cdk.out/         | CDKが生成、実行するCFnテンプレート                                                    |
| lambda/          | Lambda関連                                                                        |
| lambda/functions | Lambda関数                                                                        |
| lambda/layers    | Lambda Layer                                                                     |
| tests/           | CDKのテストコード                                                                  |

