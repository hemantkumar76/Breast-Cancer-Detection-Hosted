function predictCancer() {
  const clumpThickness = document.getElementById("clump-thickness").value;
  const uniformityCellSize = document.getElementById("uniformity-cell-size").value;
  const uniformityCellShape = document.getElementById("uniformity-cell-shape").value;
  const marginalAdhesion = document.getElementById("marginal-adhesion").value;
  const singleEpithelialCellSize = document.getElementById("single-epithelial-cell-size").value;
  const bareNuclei = document.getElementById("bare-nuclei").value;
  const blandChromatin = document.getElementById("bland-chromatin").value;
  const normalNucleoli = document.getElementById("normal-nucleoli").value;
  const mitoses = document.getElementById("mitoses").value;

  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      clumpThickness,
      uniformityCellSize,
      uniformityCellShape,
      marginalAdhesion,
      singleEpithelialCellSize,
      bareNuclei,
      blandChromatin,
      normalNucleoli,
      mitoses,
    }),
  })
    .then(response => response.json())
    .then(data => {
      const resultModal = document.getElementById('resultModal');
      const resultText = document.getElementById('resultText');
      
      resultText.textContent = data.result;

      resultModal.style.display = "flex"; // Changed from "block" to "flex"
      resultModal.style.justifyContent = "center"; // Added to center the modal horizontally
      resultModal.style.alignItems = "center"; // Added to center the modal vertically

      const closeBtn = document.querySelector('.close-btn');
      closeBtn.onclick = function () {
          resultModal.style.display = "none";
      };
  
      window.onclick = function (event) {
          if (event.target == resultModal) {
              resultModal.style.display = "none";
          }
      };
  })
    .catch((error) => {
      console.error('Error:', error);
    });
}