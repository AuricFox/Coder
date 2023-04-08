// ===================================================================
// Toggles display of sub navigation elements
// ===================================================================

var navDisplay = {
    display: 'flex',
    flexDirection: 'column'
};

$('#data-pages').click(() => {
    $('.sub-nav').not($('#data-nav')).hide();

    if($('#data-nav').is(':visible')) {$('#data-nav').hide();}
    else {$('#data-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#struct-pages').click(() => {
    $('.sub-nav').not($('#struct-nav')).hide();

    if ($('#struct-nav').is(':visible')) { $('#struct-nav').hide(); }
    else { $('#struct-nav').css(navDisplay).show(); }
});

// ----------------------------------------------------------
$('#lang-pages').click(() => {
    $('.sub-nav').not($('#lang-nav')).hide();

    if($('#lang-nav').is(':visible')) {$('#lang-nav').hide();}
    else {$('#lang-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#algo-pages').click(() => {
    $('.sub-nav').not($('#algo-nav')).hide();

    if($('#algo-nav').is(':visible')) {$('#algo-nav').hide();}
    else {$('#algo-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#math-pages').click(() => {
    $('.sub-nav').not($('#math-nav')).hide();

    if($('#math-nav').is(':visible')) {$('#math-nav').hide();}
    else {$('#math-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#tools-pages').click(() => {
    $('.sub-nav').not($('#tools-nav')).hide();

    if($('#tools-nav').is(':visible')) {$('#tools-nav').hide();}
    else {$('#tools-nav').css(navDisplay).show();}
});

// ===================================================================
// Toggles display for different coding languages [Data Types]
// ===================================================================

var codeDisplay = {
    backgroundColor: "rgba(255, 255, 255, 0.1)",
    color: "white",
    display: "block",
    whiteSpace: "pre-wrap",
    fontFamily: "monospace",
    paddingLeft: "1rem"
}

// Default to Python code example when loaded
$('.code-example').not($('#sel-py-code')).not($('#code')).hide();
$('#sel-py').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();

$('.sel-code').click(function() {
    var id = '#' + $(this).attr('id');

    $('.code-example').not($(id + '-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $(id).css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $(id + '-code').css(codeDisplay).show();
});


// ===================================================================
// Toggles display for different coding examples [Languages]
// ===================================================================

var exampleDisplay = {
    backgroundColor: "rgba(255, 255, 255, 0.1)",
    color: "white",
    display: "block",
    whiteSpace: "pre-wrap",
    fontFamily: "monospace",
    padding: "1rem"
}

// Default to example 1 code when loaded
$('.code').not($('#ex-1-code')).not($('#ex-1-output')).hide();
$('#ex-1').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();

$('.sel-code').click(function() {
    var id = $(this).attr('id');                                        // Get id of clicked element
    $('.sel-code').css({ backgroundColor: "transparent" }).show();      // Remove background
    $('#' + id).css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();   // Highlight element backgroun
    
    var code = '#' + id + '-code';
    var output = '#' + id + '-output';
    $('.code').not($(code)).not($(output)).hide();                      // Hide other examples
    $(code).css(exampleDisplay).show();                                 // Style code
    $(output).css(exampleDisplay).show();                               // Style output
});