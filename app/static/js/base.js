// ===================================================================
// Toggles display of sub navigation elements
// ===================================================================
var navDisplay = {
    display: 'flex',
    flexDirection: 'row'
};

$('.dropbtn').click(function (event) {
    event.stopPropagation();        // Prevent the click event from propagating to the document

    const menu = $(this).next('.dropdown-element'); // Get display element
    $('.dropdown-element').not(menu).hide();        // Hide any other elements displaying
    
    // Toggle the display when clicked
    if(menu.is(':visible')) {
        menu.hide();
    } else {
        menu.css(navDisplay).show();
    }

    // Add an event listener to hide the dropdown when clicking outside
    $(document).on('click', function (event) {
        // Check if the click is inside the dropdown or on the button
        if (!menu.is(event.target) && menu.has(event.target).length === 0 && !$(event.target).hasClass('dropbtn')) {
            menu.hide();
            $(document).off('click'); // Remove the event listener after hiding the dropdown
        }
    });
});

// ===================================================================
// Toggles display for different coding languages [Data Types]
// ===================================================================
var codeDisplay = {
    backgroundColor: "#272822",
    paddingLeft: "1rem"
}

// Default to Python code example when loaded
$('.code-example').not($('#sel-py-code')).not($('#code')).hide();
$('#sel-py').css({ backgroundColor: "#272822" }).show();

$('.sel-code').click(function() {
    var id = '#' + $(this).attr('id');

    $('.code-example').not($(id + '-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $(id).css({ backgroundColor: "#272822" }).show();
    $(id + '-code').css(codeDisplay).show();
});

// ===================================================================
// Toggles display for different coding examples [Languages]
// ===================================================================
var exampleDisplay = {
    backgroundColor: "#272822",
    padding: "1rem"
}

// Default to example 1 code when loaded
$('.code').not($('#ex-1-code')).not($('#ex-1-output')).hide();
$('#ex-1').css({ backgroundColor: "#5ba95e" }).show();

$('.sel-code').click(function() {
    var id = $(this).attr('id');                                // Get id of clicked element
    $('.sel-code').css({ backgroundColor: "#317233" }).show();  // Remove background
    $('#' + id).css({ backgroundColor: "#5ba95e" }).show();     // Highlight element backgroun
    
    var code = '#' + id + '-code';
    var output = '#' + id + '-output';
    $('.code').not($(code)).not($(output)).hide();              // Hide other examples
    $(code).css(exampleDisplay).show();                         // Style code
    $(output).css(exampleDisplay).show();                       // Style output
});