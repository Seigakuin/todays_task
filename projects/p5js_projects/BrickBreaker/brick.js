class Brick {
  constructor() {
    this.r = random(20, 80)
    // brickができる初期位置の設定
    // 作成される場所が端っこになりすぎないように100のオフセットを作る
    // brickができる高さは上部から400px下がったところまでにする
    this.pos = createVector(random(100, width - 100), random(100, height - 400))
  }

  display() {
    square(this.pos.x, this.pos.y, this.r)
  }
}
