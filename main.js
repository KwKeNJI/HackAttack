document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners
    document.getElementById('getPlanButton').addEventListener('click', handleGetPlan);
    document.getElementById('translateButton').addEventListener('click', handleTranslate);
    document.getElementById('updateBudgetButton').addEventListener('click', handleUpdateBudget);

    // Load cultural guide on page load
    loadCulturalGuide();
});

async function handleGetPlan() {
    const plan = await getPersonalizedPlan();
    displayPlan(plan);
}

async function handleTranslate() {
    const text = document.getElementById('textToTranslate').value;
    const translatedText = await translateText(text, 'ms');  // 'ms' is the language code for Malay
    document.getElementById('translatedText').textContent = translatedText;
}

async function handleUpdateBudget() {
    const amount = document.getElementById('budgetAmount').value;
    const result = await updateBudget(amount);
    displayBudget(result.remainingBudget);
}

async function loadCulturalGuide() {
    const guide = await getCulturalGuide();
    displayCulturalGuide(guide);
}

function displayPlan(plan) {
    const planElement = document.getElementById('personalizedPlan');
    planElement.innerHTML = `
        <h3>Your Personalized Plan:</h3>
        <p>Destinations: ${plan.destinations.join(', ')}</p>
        <p>Duration: ${plan.duration}</p>
        <p>Budget: ${plan.budget}</p>
    `;
}

function displayBudget(remainingBudget) {
    document.getElementById('remainingBudget').textContent = `Remaining Budget: ${remainingBudget} MYR`;
}

function displayCulturalGuide(guide) {
    const guideElement = document.getElementById('culturalGuide');
    guideElement.innerHTML = `
        <h3>Cultural Guide:</h3>
        <h4>Customs:</h4>
        <ul>${guide.customs.map(custom => `<li>${custom}</li>`).join('')}</ul>
        <h4>Festivals:</h4>
        <ul>${guide.festivals.map(festival => `<li>${festival}</li>`).join('')}</ul>
    `;
}