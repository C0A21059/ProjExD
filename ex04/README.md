# 第4回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- タイマー機能の追加：左上に黒色でタイマーが進む。
- 爆弾にあった際に「GameOver」の文字を描画。描画時間を確保するため、2秒間描画したらウィンドウ画面がなくなるようになっている。
- 爆弾を一定時間ごとに複数個追加：「pg.time.get_ticks()%5000 >= 4990」によって5秒ごとに10msの間だけ爆弾が追加される。処理が追いつく限り追加されるため、いくつ追加されるのかもある程度ランダムになっている。
- deepcopyを用いてそれぞれ、別オブジェクトで管理することでそれぞれの爆弾の位置の設定を容易にした。
- 左上か右上にランダムに爆弾が追加。そのため、上にいすぎると当たる確率が増える。
- 追加爆弾の方向性もランダムに実装

### 関数
- check_bound関数：壁にあたった場合、壁を貫通しないように設定
- bomb_copy関数：爆弾の追加を行う
- main関数：「にげろ！こうかとん」のプログラムの全体の流れを担当する

### 処理方法を変化
- 辞書形式で矢印キーの判定を行うようにした。キーの判定がTrue出会った場合、それぞれに対応した移動量のリストが渡される。
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] スタートのタイミングを追加
- [ ] 着弾するとこうかとん画像が切り替わる
- [ ] 爆弾の大きさを変更する
### メモ
- pygame.time.get_ticks()でミリ秒単位で時間を取得。
- Surfaceの生成後、Rectを作成する癖を付ける。
- tori_rct.colliderect(rect)で当たり判定を追加できる