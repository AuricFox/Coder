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
// Toggles code display for corresponding pages
// ===================================================================

var codeDisplay = {
    backgroundColor: "rgba(255, 255, 255, 0.1)",
    color: "white",
    display: "block",
    whiteSpace: "pre-line",
    fontFamily: "monospace",
    paddingLeft: "2rem"
}

// Default to Python code example when loaded
$('.code-example').not($('#py-code')).hide();
$('#sel-py').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();

// Show Python code example
$('#sel-py').click(() => {
    $('.code-example').not($('#py-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-py').css({backgroundColor: "rgba(255, 255, 255, 0.1"}).show();
    $('#py-code').css(codeDisplay).show();
});

// -------------------------------------------------------------------------
// Show C code example
$('#sel-c').click(() => {
    $('.code-example').not($('#c-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-c').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $('#c-code').css(codeDisplay).show();
});

// -------------------------------------------------------------------------
// Show C++ code example
$('#sel-cpp').click(() => {
    $('.code-example').not($('#cpp-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-cpp').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $('#cpp-code').css(codeDisplay).show();
});

// -------------------------------------------------------------------------
// Show C# code example
$('#sel-cs').click(() => {
    $('.code-example').not($('#cs-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-cs').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $('#cs-code').css(codeDisplay).show();
});

// -------------------------------------------------------------------------
// Show Java code example
$('#sel-java').click(() => {
    $('.code-example').not($('#java-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-java').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $('#java-code').css(codeDisplay).show();
});

// -------------------------------------------------------------------------
// Show JavaScript code example
$('#sel-js').click(() => {
    $('.code-example').not($('#js-code')).hide();
    $('.sel-code').css({ backgroundColor: "transparent" }).show();
    $('#sel-js').css({ backgroundColor: "rgba(255, 255, 255, 0.1" }).show();
    $('#js-code').css(codeDisplay).show();
});