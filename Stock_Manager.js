const fs = require('fs');
const readline = require('readline');

// Define the filename for the persistent data
const DATA_FILE = 'stock_inventory.txt';
// Global variable to hold the stock data in memory
let stock = {};

// Helper function for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// --- File Handling Functions ---

function loadStock() {
    console.log('🛒 Attempting to load stock...');
    try {
        if (!fs.existsSync(DATA_FILE)) {
            console.log("🗄️ No existing inventory file found. Starting fresh.");
            return;
        }

        const data = fs.readFileSync(DATA_FILE, 'utf8');
        // Parse the JSON string from the file back into a JavaScript object
        stock = JSON.parse(data);
        console.log(`✅ Loaded ${Object.keys(stock).length} items from ${DATA_FILE}.`);

    } catch (error) {
        console.error(`❌ Error loading stock from file: ${error.message}. Starting fresh.`);
        stock = {};
    }
}

function saveStock() {
    try {
        // Convert the JavaScript object into a JSON string for easy saving
        const data = JSON.stringify(stock, null, 2);
        fs.writeFileSync(DATA_FILE, data, 'utf8');
        console.log(`💾 Stock successfully saved to ${DATA_FILE}.`);
    } catch (error) {
        console.error(`❌ Error saving stock to file: ${error.message}`);
    }
}

// --- Stock Management Functions ---

function displayStock() {
    console.log('\n' + '='.repeat(40));
    console.log('      🏪 Current Stock Availability');
    console.log('='.repeat(40));

    const keys = Object.keys(stock);
    if (keys.length === 0) {
        console.log('--- Inventory is currently empty. ---');
    } else {
        keys.forEach(product => {
            console.log(`${product}: **${stock[product]}** units`);
        });
    }
    console.log('='.repeat(40));
}

function restockItem(productName, quantityAdded) {
    // Standardize capitalization and ensure quantity is a number
    const product = productName.trim().charAt(0).toUpperCase() + productName.trim().slice(1);
    const quantity = parseInt(quantityAdded);

    if (quantity > 0) {
        if (stock[product]) {
            stock[product] += quantity;
            console.log(`✅ RESTOCK SUCCESS: Added ${quantity} units of ${product}.`);
        } else {
            stock[product] = quantity;
            console.log(`✅ NEW ITEM ADDED: ${product} added with initial stock of ${quantity} units.`);
        }
        saveStock(); // Save changes
    } else {
        console.log('⚠️ Quantity must be a positive number.');
    }
}

function recordSale(productName, quantitySold) {
    const product = productName.trim().charAt(0).toUpperCase() + productName.trim().slice(1);
    const quantity = parseInt(quantitySold);

    if (quantity <= 0) {
        console.log('⚠️ Quantity must be a positive number.');
        return;
    }

    if (!stock[product]) {
        console.log(`❌ ERROR: Product '${product}' is not tracked in the inventory.`);
        return;
    }

    if (stock[product] >= quantity) {
        stock[product] -= quantity;
        console.log(`✅ SALE SUCCESS: Sold ${quantity} units of ${product}.`);

        // Check for low stock alert
        if (stock[product] < 10 && stock[product] > 0) {
            console.log(`⚠️ LOW STOCK ALERT! ${product} is now at ${stock[product]} units.`);
        } else if (stock[product] === 0) {
            console.log(`🚨 OUT OF STOCK ALERT! ${product} is now completely sold out.`);
        }

        saveStock(); // Save changes
    } else {
        console.log(`❌ ERROR: Cannot sell ${quantity} units of ${product}. Only ${stock[product]} available.`);
    }
}

// --- Main Application Logic ---

function showMenu() {
    displayStock();

    console.log('\n--- Available Actions ---');
    console.log('1: **Restock** (Add stock Input)');
    console.log('2: **Record Sale** (Subtract stock Output)');
    console.log('3: **Exit** system');
    
    rl.question('Enter your choice (1, 2, or 3): ', handleAction);
}

function handleAction(action) {
    action = action.trim();

    if (action === '1') {
        rl.question('Enter product name to restock: ', (product) => {
            rl.question('Enter quantity to add: ', (quantity) => {
                restockItem(product, quantity);
                showMenu(); // Return to menu
            });
        });
    } else if (action === '2') {
        rl.question('Enter product name sold: ', (product) => {
            rl.question('Enter quantity sold: ', (quantity) => {
                recordSale(product, quantity);
                showMenu(); // Return to menu
            });
        });
    } else if (action === '3') {
        console.log('\n👋 System shutting down. Your latest changes are saved!');
        rl.close();
    } else {
        console.log('❌ Invalid choice. Please enter 1, 2, or 3.');
        showMenu(); // Show menu again
    }
}

function runSupermarketSystem() {
    console.log("🛒 Starting Supermarket Stock Management System...");
    loadStock();
    showMenu();
}

// Execute the main function
runSupermarketSystem();
