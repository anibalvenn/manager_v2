function handleRankedSeriesFileSelection() {
  const fileInput = document.getElementById('fileInput');
  fileInput.click(); // This will trigger the file dialog to open

  // Listen for changes in the file input
  fileInput.addEventListener('change', function (event) {
    const selectedFile = event.target.files[0];
    console.log(event.target.files[0].webkitRelativePath)
    // Send the selected file to the backend using AJAX
    const selectedFileName = selectedFile.name; // Extract the file name

    fetch('/handle-ranked-series', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Specify the content type as JSON
      },
      body: JSON.stringify({ fileName: selectedFileName }), // Convert the file name to a JSON string
    })
      .then(response => {
        if (response.ok) {
          // Handle successful response
          console.log('ranked-series upload successful');
        } else {
          // Handle error response
          console.error('ranked-series upload failed');
        }
      })
      .catch(error => {
        console.error('Error uploading file:', error);
      });
  });
}

function handleAddResultsFileSelection() {
  const fileInput = document.getElementById('fileInput');
  fileInput.click(); // This will trigger the file dialog to open

  // Listen for changes in the file input
  fileInput.addEventListener('change', function (event) {
    const selectedFile = event.target.files[0];
    console.log(event.target.files[0].webkitRelativePath)
    // Send the selected file to the backend using AJAX
    const selectedFileName = selectedFile.name; // Extract the file name

    fetch('/handle-add-results', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Specify the content type as JSON
      },
      body: JSON.stringify({ fileName: selectedFileName }), // Convert the file name to a JSON string
    })
      .then(response => {
        if (response.ok) {
          // Handle successful response
          console.log('add-results upload successful');
        } else {
          // Handle error response
          console.error('add-results upload failed');
        }
      })
      .catch(error => {
        console.error('Error uploading file:', error);
      });
  });
}

function toggleVisibility(divId) {
  const newChampionshipDiv = document.getElementById('newChampionship');
  const existingChampionshipDiv = document.getElementById('existingChampionship');

  if (divId === 'newChampionship') {
    newChampionshipDiv.classList.remove('hidden');
    existingChampionshipDiv.classList.add('hidden');
  } else {
    newChampionshipDiv.classList.add('hidden');
    existingChampionshipDiv.classList.remove('hidden');
  }
}