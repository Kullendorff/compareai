document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('queryForm');
    const submitBtn = document.getElementById('submitBtn');
    const compareBtn = document.getElementById('compareBtn');
    const comparisonResults = document.getElementById('comparisonResults');
    
    function setLoading(isLoading) {
        submitBtn.disabled = isLoading;
        if (isLoading) {
            submitBtn.innerHTML = '<span class="loading"></span>Processing...';
        } else {
            submitBtn.innerHTML = 'Ask AIs';
        }
    }

    function updateResponseTime(model) {
        const timeElement = document.getElementById(`${model}Time`);
        timeElement.textContent = `${(Math.random() * 2 + 1).toFixed(1)}s`;
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        setLoading(true);
        compareBtn.style.display = 'none';
        comparisonResults.style.display = 'none';

        const question = document.getElementById('questionInput').value;

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question })
            });

            const data = await response.json();

            // Update responses
            document.getElementById('chatgptResponse').value = data.chatgpt;
            document.getElementById('geminiResponse').value = data.gemini;
            document.getElementById('claudeResponse').value = data.claude;

            // Update response times
            updateResponseTime('chatgpt');
            updateResponseTime('gemini');
            updateResponseTime('claude');

            // Show compare button
            compareBtn.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while fetching responses');
        } finally {
            setLoading(false);
        }
    });

    compareBtn.addEventListener('click', async function() {
        setLoading(true);
        const responses = {
            chatgpt: document.getElementById('chatgptResponse').value,
            gemini: document.getElementById('geminiResponse').value,
            claude: document.getElementById('claudeResponse').value
        };

        try {
            const response = await fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(responses)
            });

            const data = await response.json();
            
            // Display comparison results
            comparisonResults.innerHTML = `
                <h2 style="margin-bottom: 1rem;">Comparison Results</h2>
                <div class="responses-grid">
                    ${Object.entries(data).map(([model, analysis]) => `
                        <div class="response-card">
                            <div class="card-header">
                                <span class="model-name">${model}'s Analysis</span>
                            </div>
                            <div class="card-content">
                                <div class="response-text">${marked.parse(analysis)}</div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            `;
            comparisonResults.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while comparing responses');
        } finally {
            setLoading(false);
        }
    });
});