1. VENVで動くようにしてください。

  メニューバーの
    Pycharm -> Preference
  
  ダイアログの左ペインの
    Project:boto3s3
      Project Interpreter 

      Project Interpreter のプルダウンの歯車アイコンからAddして、プルダウンに追加されたら、それをプルダウンから選択する。


2. モジュールをインストールしてください。

  $ pip install awscli boto3

3. キーの設定をしてください。~/.aws　に設定されます。

  $ aws configure
  
4. スクリプト内でbucketを定義しています。