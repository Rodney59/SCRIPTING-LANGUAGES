const EXCHANGE_RATE = 0.93;

function usdToEur(amount) {
    return amount * EXCHANGE_RATE;
}

function eurToUsd(amount) {
    return amount / EXCHANGE_RATE;
}

function currencyConverter() {
    let resultDiv = document.getElementById("result");

    let amount = parseFloat(prompt("Enter amount to convert: "));

    let typeInput = prompt("Enter starting currency (USD or EUR): ");
    if (typeInput === null) return;

    let type = typeInput.toUpperCase();

    if (isNaN(amount) || amount < 0) {
        resultDiv.textContent = "Please enter a valid positive number for the amount.";
        return;
    }

    if (type === "USD" || type === "EUR") {
        let convertedAmount;
        let targetUnit;

        if (type === "USD") {
            convertedAmount = usdToEur(amount);
            targetUnit = "EUR";
        } else {
            convertedAmount = eurToUsd(amount);
            targetUnit = "USD";
        }

        resultDiv.textContent = `${amount.toFixed(2)} ${type} is equal to ${convertedAmount.toFixed(2)} ${targetUnit}`;
    } else {
        resultDiv.textContent = "Invalid currency type. Please enter 'USD' or 'EUR'.";
    }
}