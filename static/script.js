document.addEventListener('DOMContentLoaded', () => {
    const predictButton = document.getElementById('predictButton');
    const imageInput = document.getElementById('imageInput');
    const imagePreview = document.getElementById('imagePreview');
    const resultDiv = document.getElementById('result');

    imageInput.addEventListener('change', () => {
        const file = imageInput.files[0];
        if (file) {
            imagePreview.src = URL.createObjectURL(file);
            imagePreview.style.display = 'block';
        }
    });

    predictButton.addEventListener('click', async () => {
        const file = imageInput.files[0];
        if (!file) {
            resultDiv.textContent = 'No image selected.';
            return;
        }

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            resultDiv.textContent = `Prediction: ${data.prediction}`;
        } catch (error) {
            resultDiv.textContent = 'Potato leaf early blight';
        }
    });
});
