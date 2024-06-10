document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent default anchor click behavior
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth' // Smooth scroll to the target section
        });
    });
});

// Event listener for search bar input
document.getElementById('searchBar').addEventListener('keyup', function() {
    var filter = this.value.toUpperCase(); // Get the search query and convert to uppercase
    var lis = document.querySelectorAll('.tracks-li, .time-range-section ul li'); // Get all list items

    // Loop through all list items and hide those that don't match the search query
    lis.forEach(li => {
        var text = li.textContent || li.innerText; // Get the text content of the list item
        if (text.toUpperCase().indexOf(filter) > -1) {
            li.style.display = ""; // Show the list item
        } else {
            li.style.display = "none"; // Hide the list item
        }
    });
});