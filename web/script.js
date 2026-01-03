console.log("SCRIPT TERLOAD");

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const startBtn = document.getElementById("startBtn");
const resetBtn = document.getElementById("resetBtn");
const bounceText = document.getElementById("bounceCount");
const logBody = document.querySelector("#logTable tbody");

let y, v, e;
const g = 0.8;
const r = 20;
const padding = 50;        
const xMin = -1;
const xMax = 1;

const MIN_BOUNCE_VELOCITY = 1.5;

let animationId;
let bounceCount = 0;
let stopped = true;
let maxHeight = Number(document.getElementById("h0").value);

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawAxes();

    const x = 0; 
    const cx = toCanvasX(x);
    const cy = toCanvasY(y);

    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.fillStyle = "#0077cc";
    ctx.fill(); 
}

function update() {
    if (stopped) return;

    v += g;
    y -= v;

    if (y <= 0) {
        y = 0;

        if (Math.abs(v) > MIN_BOUNCE_VELOCITY) {
            v = -v * e;
            bounceCount++;
            bounceText.textContent = bounceCount;

            const tinggiPantulan = (v * v) / (2 * g);

            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${bounceCount}</td>
                <td>${tinggiPantulan.toFixed(2)}</td>
            `;
            logBody.appendChild(row);

        } else {
            stopped = true;
            v = 0;
            draw();
            return;
        }
    }

    draw();
    animationId = requestAnimationFrame(update);
}

function toCanvasX(x) {
  
}

function toCanvasY(y) {

}


function drawAxes() {


    for (let i = 0; i <= 5; i++) {

    }

        for (let i = -1; i <= 1; i += 0.5) {

        }

}

startBtn.addEventListener("click", () => {

});

resetBtn.addEventListener("click", () => {

});

y = Number(document.getElementById("h0").value);
draw();



