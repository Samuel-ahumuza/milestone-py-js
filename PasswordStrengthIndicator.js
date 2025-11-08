// --- Get DOM Elements ---
const passwordInput = document.getElementById('password');
const strengthBar = document.getElementById('strength-bar');
const overallFeedback = document.getElementById('overall-feedback');

// Get all individual feedback messages
const requirements = {
    length: document.getElementById('msg-length'),
    lower: document.getElementById('msg-lower'),
    upper: document.getElementById('msg-upper'),
    number: document.getElementById('msg-number'),
    symbol: document.getElementById('msg-symbol')
};

// --- Password Strength Criteria (Regular Expressions) ---
const criteria = [
    { name: 'length', regex: /.{8,}/, element: requirements.length }, // At least 8 characters
    { name: 'lower', regex: /[a-z]/, element: requirements.lower },    // At least one lowercase letter
    { name: 'upper', regex: /[A-Z]/, element: requirements.upper },    // At least one uppercase letter
    { name: 'number', regex: /[0-9]/, element: requirements.number },  // At least one number
    { name: 'symbol', regex: /[^a-zA-Z0-9\s]/, element: requirements.symbol } // At least one symbol
];

// --- Core Function: Check and Update Strength ---
function checkPasswordStrength() {
    const password = passwordInput.value;
    let score = 0;
    let criteriaMet = 0;

    // 1. Check each criteria using Regex
    criteria.forEach(item => {
        const passed = item.regex.test(password);
        
        // Update the score and count
        if (passed) {
            score += 20; // 20 points per criteria met
            criteriaMet++;
        }
        
        // 2. Update the individual feedback text visual
        item.element.classList.toggle('pass', passed);
        item.element.classList.toggle('fail', !passed);
        item.element.innerHTML = passed ? `✅ ${item.element.textContent.substring(2)}` : `❌ ${item.element.textContent.substring(2)}`;
    });

    // 3. Update the Strength Bar width and color
    strengthBar.style.width = `${score}%`;
    
    let strengthText = "Very Weak";
    let barColor = "#e74c3c"; // Red

    if (criteriaMet >= 5) {
        strengthText = "Excellent";
        barColor = "#2ecc71"; // Green
        overallFeedback.className = "strong-text";
    } else if (criteriaMet >= 3) {
        strengthText = "Medium";
        barColor = "#f39c12"; // Orange
        overallFeedback.className = "medium-text";
    } else {
        // Less than 3 or empty
        overallFeedback.className = "weak-text";
    }
    
    // Handle empty input explicitly
    if (password.length === 0) {
        score = 0;
        strengthText = "Strength: None";
        barColor = "#eee";
        overallFeedback.className = "";
    } else {
        strengthText = `Strength: ${strengthText}`;
    }

    strengthBar.style.backgroundColor = barColor;
    overallFeedback.textContent = strengthText;
}

// --- Event Listener ---
// Run the check function every time the user types a character
passwordInput.addEventListener('input', checkPasswordStrength);

// Initial call to set the bar to None when the page loads
checkPasswordStrength();
