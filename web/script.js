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
    return padding + (x - xMin) / (xMax - xMin) * (canvas.width - 2 * padding);
}

function toCanvasY(y) {
    return (
        canvas.height -
        padding -
        (y / maxHeight) * (canvas.height - 2 * padding) -
        r
    );
}


function drawAxes() {
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 1;
    ctx.font = "12px Arial";
    ctx.fillStyle = "#000";

    ctx.beginPath();
    ctx.moveTo(padding, padding - r);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    for (let i = 0; i <= 5; i++) {
        const yVal = (maxHeight / 5) * i;
        const yPos = toCanvasY(yVal);

        ctx.beginPath();
        ctx.moveTo(padding - 5, yPos);
        ctx.lineTo(padding + 5, yPos);
        ctx.stroke();

        ctx.fillText(yVal.toFixed(0), padding - 40, yPos + 4);
    }

    for (let i = -1; i <= 1; i += 0.5) {
        const xPos = toCanvasX(i);

        ctx.beginPath();
        ctx.moveTo(xPos, canvas.height - padding - 5);
        ctx.lineTo(xPos, canvas.height - padding + 5);
        ctx.stroke();
        ctx.fillText(i.toFixed(1), xPos - 10, canvas.height - padding + 20);
    }

}

startBtn.addEventListener("click", () => {
    y = Number(document.getElementById("h0").value);
    maxHeight = y;
    e = Number(document.getElementById("e").value);
    v = 0;

    bounceCount = 0;
    bounceText.textContent = bounceCount;

    stopped = false;

    if (animationId) cancelAnimationFrame(animationId);
    update();
});

resetBtn.addEventListener("click", () => {
    bounceCount = 0;
    bounceText.textContent = bounceCount;
    logBody.innerHTML = ""; 
});

y = Number(document.getElementById("h0").value);
draw();

fetch("data/hasil_pengukuran.csv")
    .then(response => response.text())
    .then(csv => {
        const rows = csv.trim().split("\n").slice(1);
        const tbody = document.querySelector("#timeTable tbody");

        let waktu = {};

       rows.forEach(row => {
            const cols = row.split(",");

            const metode = cols[0];
            const nilaiWaktu = parseFloat(cols[1]); 

            waktu[metode] = nilaiWaktu;

            if (metode !== "Selisih") {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${metode}</td>
                    <td>${nilaiWaktu.toFixed(8)}</td>
                `;
                tbody.appendChild(tr);
            }
        });

        if (waktu["Selisih"] !== undefined) {
            document.getElementById("selisihText").innerText =
                "Selisih waktu eksekusi: " + waktu["Selisih"].toFixed(8) + " detik";
        }
    });