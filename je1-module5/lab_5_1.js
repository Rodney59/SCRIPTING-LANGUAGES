const readlineSync = require('readline-sync');

let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
}];



function showContact(contactList, index) {
    if (!(contactList instanceof Array)) {
        console.log("Error: The first argument must be an array of contacts.");
        return false;
    }

    if (index < 0 || index >= contactList.length || typeof index !== 'number') {
        console.log("Error: Invalid contact index or no contact at this position.");
        return false;
    }

    const contact = contactList[index];
    console.log("  Name:", contact.name);
    console.log("    Phone:", contact.phone);
    console.log("    Email:", contact.email);
    return true;
}

function showAllContacts(contactList) {
    if (!(contactList instanceof Array)) {
        console.log("Error: The argument must be an array of contacts.");
        return false;
    }

    if (contactList.length === 0) {
        console.log("There are no contacts in the list.");
        return true;
    }

    console.log("Contacts:");
    for (let i = 0; i < contactList.length; i++) {
        console.log(`Contact ${i + 1}:`);
        showContact(contactList, i);
    }
    return true;
}


function addContact() {
    let name = readlineSync.question("Enter contact name: ");
    let phone = readlineSync.question("Enter contact phone number: ");
    let email = readlineSync.question("Enter contact email: ");

    if (name && phone && email) {
        contacts.push({name, phone, email});
        console.log("Contact added successfully!");
    } else {
        console.log("Please enter all required information (name, phone, email).");
    }
}

function addNewContact(contactList, name, phone, email) {
    if (!(contactList instanceof Array)) {
        console.log("Error: The first argument must be an array of contacts.");
        return false;
    }

    if (!name || !phone || !email) {
        console.log("Error: Please provide name, phone, and email for the new contact.");
        return false;
    }

    contactList.push({ name, phone, email });
    console.log("Contact added successfully!");
    return true;
}


function manageContacts() {
    choice = readlineSync.question("What do you want to do? (first/last/all/new/quit): ");


    switch (choice.toLowerCase()) {
        case "first":
            if (contacts.length > 0) {
                console.log("First Contact:");
                showContact(contacts, 0);
            } else {
                console.log("There are no contacts in the list.");
            }
            break;
        case "last":
            if (contacts.length > 0) {
                console.log("Last Contact:");
                showContact(contacts, contacts.length - 1);
            } else {
                console.log("There are no contacts in the list.");
            }
            break;
        case "new":
            let newName = readlineSync.question("Enter contact name: ");
            let newPhone = readlineSync.question("Enter contact phone number: ");
            let newEmail = readlineSync.question("Enter contact email: ");
            addNewContact(contacts, newName, newPhone, newEmail);
        break;


        case "quit":
            console.log("Exiting the program.");
            break;
        case "all":
            showAllContacts(contacts);
            break;
        default:
            console.log("Invalid choice. Please enter 'first', 'last', 'all', 'new', or 'quit'");

    }


}

let running = true;
let choice;
while (running) {
    manageContacts();
    running = choice.toLowerCase() !== "quit";
}