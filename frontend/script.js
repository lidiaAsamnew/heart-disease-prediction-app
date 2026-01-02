const API_BASE_URL = "https://heart-disease-prediction-app-lfsn.onrender.com";

// Get DOM elements
const resultsSection = document.getElementById("resultsSection");
const errorMessage = document.getElementById("errorMessage");

document.getElementById("predictionForm").addEventListener("submit", async e => {
  e.preventDefault();

  // Hide previous results and errors
  resultsSection.style.display = "none";
  errorMessage.style.display = "none";

  // Show loading state
  const submitBtn = e.target.querySelector('button[type="submit"]');
  const btnText = submitBtn.querySelector('.btn-text');
  const btnLoader = submitBtn.querySelector('.btn-loader');
  const originalText = btnText.textContent;
  btnText.textContent = "Predicting...";
  btnLoader.style.display = "inline-block";
  submitBtn.disabled = true;

  const data = {
    age: +document.getElementById("age").value,
    sex: +document.getElementById("sex").value,
    cp: +document.getElementById("cp").value,
    trestbps: +document.getElementById("trestbps").value,
    chol: +document.getElementById("chol").value,
    fbs: +document.getElementById("fbs").value,
    restecg: +document.getElementById("restecg").value,
    thalach: +document.getElementById("thalach").value,
    exang: +document.getElementById("exang").value,
    oldpeak: +document.getElementById("oldpeak").value,
    slope: +document.getElementById("slope").value,
    ca: +document.getElementById("ca").value,
    thal: +document.getElementById("thal").value
  };

  try {
    const res = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(data)
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || "Prediction failed");
    }

    const result = await res.json();
    displayResults(result);

  } catch(err) {
    showError(err.message || "An error occurred. Please try again.");
  } finally {
    btnText.textContent = originalText;
    btnLoader.style.display = "none";
    submitBtn.disabled = false;
  }
});

function displayResults(data){
  const lr = data.logistic_regression;
  const dt = data.decision_tree;
  
  const lrClass = lr.prediction === 1 ? "result-positive" : "result-negative";
  const dtClass = dt.prediction === 1 ? "result-positive" : "result-negative";
  
  const r = `
    <div class="result-card ${lrClass}">
      <h3>Logistic Regression</h3>
      <p class="prediction-label"><b>${lr.prediction_label}</b></p>
      <p class="probability">Confidence: ${(lr.probability*100).toFixed(1)}%</p>
    </div>
    <div class="result-card ${dtClass}">
      <h3>Decision Tree</h3>
      <p class="prediction-label"><b>${dt.prediction_label}</b></p>
      <p class="probability">Confidence: ${(dt.probability*100).toFixed(1)}%</p>
    </div>
  `;
  document.getElementById("results").innerHTML = r;
  resultsSection.style.display = "block";
}

function showError(msg){
  errorMessage.textContent = msg;
  errorMessage.style.display = "block";
}
