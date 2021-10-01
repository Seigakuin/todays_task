let yHitPoint = 90
let yMagicPoint = 45
let mHitPoint = 250

let yHitPointEl = document.getElementById("y-hp")
let yMagicPointEl = document.getElementById("y-mp")
let mHitPointEl = document.getElementById("m-hp")

let battleScriptEl = document.getElementById("battle-script")

let battleScriptText = ""

function handleFight() {
  let damage = Math.floor(Math.random() * 10) + 1
  mHitPoint -= damage
  mHitPointEl.innerHTML = mHitPoint
  battleScriptText =
    `<p>勇者はモンスターに${damage}のダメージを与えました！</p>` +
    battleScriptText
  battleScriptEl.innerHTML = battleScriptText

  console.log("Fight")
}

function handleGuard() {
  console.log("Guard")
}

function handleSpecial() {
  console.log("Special")
}
