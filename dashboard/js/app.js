/*
==========================================================
IndoBERT Dashboard
==========================================================
*/

const API_URL =
"https://uas-bert-api-production.up.railway.app";

const inputText = document.getElementById("inputText");
const predictBtn = document.getElementById("predictBtn");

const loadingBox = document.getElementById("loadingBox");
const resultCard = document.getElementById("resultCard");

const labelResult = document.getElementById("labelResult");
const confidenceResult = document.getElementById("confidenceResult");

const probabilityBox = document.getElementById("probabilityBox");

const copyBtn = document.getElementById("copyBtn");

/* ========================================= */

predictBtn.addEventListener("click", predictSentiment);

inputText.addEventListener("keydown", function (e) {

    if (e.ctrlKey && e.key === "Enter") {

        predictSentiment();

    }

});

/* ========================================= */

async function predictSentiment() {

    const text = inputText.value.trim();

    if (text === "") {

        alert("Masukkan kalimat terlebih dahulu.");

        return;

    }

    loadingBox.classList.remove("hidden");

    resultCard.classList.add("hidden");

    predictBtn.disabled = true;

    predictBtn.innerHTML = "Menganalisis...";

    try {

        const response = await fetch(`${API_URL}/predict`,{

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                text: text

            })

        });

        if (!response.ok) {

            throw new Error("API Error");

        }

        const result = await response.json();

        showResult(result);

    }

    catch(error){

    console.error(error);

    if(error instanceof TypeError){

        alert("Tidak dapat menghubungi server Railway.");

    }else{

        alert("Terjadi kesalahan saat memproses data.");

    }

}

    finally {

        loadingBox.classList.add("hidden");

        predictBtn.disabled = false;

        predictBtn.innerHTML = "Analisis Sentimen";

    }

}

/* ========================================= */

function showResult(result) {

    resultCard.classList.remove("hidden");

    labelResult.innerHTML = capitalize(result.label);

    confidenceResult.innerHTML =
        (result.confidence * 100).toFixed(2) + "%";

    labelResult.className = "label-result";

    if (result.label === "positive") {

        labelResult.classList.add("positive");

    }

    else if (result.label === "negative") {

        labelResult.classList.add("negative");

    }

    else {

        labelResult.classList.add("neutral");

    }

    probabilityBox.innerHTML = "";

    Object.entries(result.probability).forEach(([label, value]) => {

        const percent = (value * 100).toFixed(2);

        let color = "#38bdf8";

        if (label === "positive") {

            color = "#22c55e";

        }

        if (label === "negative") {

            color = "#ef4444";

        }

        if (label === "neutral") {

            color = "#f59e0b";

        }

        probabilityBox.innerHTML += `

        <div class="probability-item">

            <div class="probability-header">

                <span>${capitalize(label)}</span>

                <span>${percent}%</span>

            </div>

            <div class="progress">

                <div

                    class="progress-bar"

                    style="width:${percent}%;background:${color};">

                </div>

            </div>

        </div>

        `;

    });

}

/* ========================================= */

copyBtn.addEventListener("click", function () {

    const text =

`Label      : ${labelResult.innerText}
Confidence : ${confidenceResult.innerText}`;

    navigator.clipboard.writeText(text);

    copyBtn.innerHTML = "Berhasil Disalin";

    setTimeout(() => {

        copyBtn.innerHTML = "Copy Hasil";

    }, 2000);

});

/* ========================================= */

function capitalize(text) {

    return text.charAt(0).toUpperCase() + text.slice(1);

}
async function checkAPI(){

    try{

        const response = await fetch(API_URL);

        if(response.ok){

            console.log("API Connected");

        }else{

            console.log("API Error");

        }

    }

    catch(error){

        console.log(error);

        alert("Backend Railway sedang offline.");

    }

}

checkAPI();
const controller = new AbortController();

const timeout = setTimeout(()=>{

controller.abort();

},30000);

clearTimeout(timeout);
