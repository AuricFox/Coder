// ===================================================================
// Toggles display of sub navigation elements
// ===================================================================
// Display first level of dropdown elements
$('.dropbtn').hover(function () {
    // Hide all dropdown elements
    $('.dropdown-element').hide();
    // Get current highlighted element
    const menu = $(this).next('.dropdown-element');
    menu.show();

    // Hide the dropdown when the mouse leaves the dropdown or the button
    menu.on('mouseleave', function () {
        menu.hide();
    });
});

// Display second level of dropdown elements

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